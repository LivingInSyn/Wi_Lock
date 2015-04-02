import glib
import dbus
from dbus.mainloop.glib import DBusGMainLoop
import subprocess
import time
import atexit
import ConfigParser
import sys
import os

def find_current_dir():
        #returns the correct current working directory for exe's or py files
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)
        return application_path
    
def pull_config():
    config = ConfigParser.ConfigParser()
    path = find_current_dir()
    config_path = os.path.join(path,"wi_lock.cfg")
    config.read(config_path)
    trusted_networks = config.get('Networks','networks',0)
    print(trusted_networks)
    print(type(trusted_networks))
    print(trusted_networks.split(','))
    
pull_config()
#print(trusted_networks)
