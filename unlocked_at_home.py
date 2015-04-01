'''
By Jeremy Mill

jeremymill@gmail.com
github.com/livinginsyn

licensed until the GPL V3
'''

import glib
import dbus
from dbus.mainloop.glib import DBusGMainLoop
import subprocess


def extract_ssid():
    info = subprocess.check_output(['wpa_cli','status'])
    start_index = info.find("\nssid")+6
    stop_index = info.find("\n",51)
    ssid = info[start_index:stop_index]
    return ssid      


def notifications(bus, message):
    print(message.get_member())
    if(message.get_member() == 'LockRequested'):
        print("Call lock policy to 5 minutes")
    elif(message.get_member() == 'UnlockRequested'):
        print("check wifi here and change lock time appropriately")
        
        
        


DBusGMainLoop(set_as_default=True)

bus = dbus.SessionBus()

bus.add_match_string_non_blocking("eavesdrop=true, interface='com.canonical.Unity.Session'")

bus.add_message_filter(notifications)

mainloop = glib.MainLoop()
mainloop.run()
