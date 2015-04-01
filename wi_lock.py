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

trusted_networks = ['UCONN-SECURE','fake_network']
trusted_time = 0
no_trust_time = 300

def extract_ssid():
    info = subprocess.check_output(['wpa_cli','status'])
    start_index = info.find("\nssid")+6
    stop_index = info.find("\n",start_index)
    ssid = info[start_index:stop_index]
    return ssid
    
def set_locktime(lock_time):
    subprocess.call(['gsettings','set','org.gnome.desktop.session','idle-delay',lock_time])

def exit_handler():
    set_locktime(no_trust_time)

#set the initial locktime
set_locktime(300)

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
