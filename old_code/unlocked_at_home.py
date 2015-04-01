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


trusted_networks = ['UCONN-SECURE']

def extract_ssid():
    info = subprocess.check_output(['wpa_cli','status'])
    start_index = info.find("\nssid")+6
    stop_index = info.find("\n",51)
    ssid = info[start_index:stop_index]
    return ssid
    
def set_locktime(lock_time):
    subprocess.call(['gsettings','set','org.gnome.desktop.session','idle-delay',lock_time])


def notifications(bus, message):
    print(message.get_member())
    if(message.get_member() == 'LockRequested'):
        print("Call lock policy to 5 minutes")
    elif(message.get_member() == 'UnlockRequested'):
        #sleep for 30 seconds to let the wifi catch up
        time.sleep(30)
        #grab the ssid
        ssid = extract_ssid()
        #if the ssid is in the list of trusted networks, then set unlock to 0, otherwise, 300
        #these will be configurable in the future
        if(ssid in trusted_networks):
            set_locktime(0)
            #now set the locktime
        else:
            set_locktime(300)
            #now set the locktime
        


#create the main loop for the notification watcher
DBusGMainLoop(set_as_default=True)
#init the bus
bus = dbus.SessionBus()
#set up the string we're looking for
bus.add_match_string_non_blocking("eavesdrop=true, interface='com.canonical.Unity.Session'")
#if we see the string we're looking for, call function notifications
bus.add_message_filter(notifications)

#set the locktime to 300 by default (as to be more failsafe), this will be a conf value in the future
set_locktime(300)

#start tha main loop for the notification watcher
mainloop = glib.MainLoop()
mainloop.run()


