'''
By Jeremy Mill

jeremymill@gmail.com
github.com/livinginsyn

licensed until the GPL V2
'''

import glib
import dbus
from dbus.mainloop.glib import DBusGMainLoop
import subprocess
import time
import atexit
import ConfigParser
import sys
import os

#init vars with some default values, just in case something goes wrong. These should be 'safe values'
#trusted_time is safe at 0 by default because trusted_networks is empty by default
trusted_networks = []
trusted_time = 0
no_trust_time = 300

def extract_ssid():
    info = get_wpa_cli_status()
    start_index = info.find("\nssid")+6
    if(start_index != -1):
        stop_index = info.find("\n",start_index)
        ssid = info[start_index:stop_index]
        return ssid
    else:
        ssid = None
        return ssid

def get_wpa_cli_status():
    info = subprocess.check_output(['wpa_cli','status'])
    return info
    
def set_locktime(lock_time):
    subprocess.call(['gsettings','set','org.gnome.desktop.session','idle-delay',lock_time])

def exit_handler():
    set_locktime(no_trust_time)
    
def find_current_dir():
        #returns the correct current working directory for exe's or py files
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)
        return application_path
    
def pull_config():
    #open up the config parser, and the cfg file
    config = ConfigParser.ConfigParser()
    path = find_current_dir()
    config_path = os.path.join(path,"wi_lock.cfg")
    config.read(config_path)
    #gotta get that global declaration
    global trusted_networks, trusted_time, no_trust_time
    #pull the config values
    trusted_networks = config.get('Networks','networks',0).split(',')
    trusted_time = int(config.get('Times','trusted_time',0))
    no_trust_time = int(config.get('Times','no_trust_time',0))
    
    

#set the initial locktime
set_locktime(300)

pull_config()

#create the main loop:
while 1:
    #polling interval
    time.sleep(3)
    #get the current SSID
    ssid = extract_ssid()
    if(ssid in trusted_networks):
        #will be in a conf file
        set_locktime(trusted_time)
    else:
        #will be in a conf file
        set_locktime(no_trust_time)

#attempt to reset to no_trust_time if the program exits
atexit.register(exit_handler)
