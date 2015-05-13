import subprocess
from subprocess import check_output
import re
import time

class Lock_Manager:
    def __init__(self):
        def_locktime = 300
    
    #the locktimes are how long until gnome thinks it's been idle        
    def set_locktime(self,lock_time):
        current_locktime = self.get_locktime()
        print("Current Locktime is " + str(current_locktime))
        print("Trying to change it to " + str(lock_time))
        if(current_locktime != lock_time):
            print("setting locktime to "+str(lock_time))
            subprocess.call(['gsettings','set','org.gnome.desktop.session','idle-delay',str(lock_time)])
        else:
            print("locktimes are equal")
        
    def get_locktime(self):
        #locktime = subprocess.call(['gsettings','get','org.gnome.desktop.session','idle-delay'])
        out = check_output(['gsettings','get','org.gnome.desktop.session','idle-delay'])
        return(int(out.split(" ")[1]))
    
    #the screensaver time is how long until it waits to go tothe screensaver. For the lock to work, 
    #the screensaver must come up when idle.
    def get_screen_saver_time(self):
        out = check_output(['gsettings','get','org.gnome.desktop.screensaver','lock-delay'])
        return(int(out.split(" ")[1]))
    
    def set_screen_saver_time(self,screen_time):
        current_screen_time = self.get_screen_saver_time()
        if(current_screen_time != screen_time):
            subprocess.call(['gsettings','set','org.gnome.desktop.screensaver','lock-delay',str(screen_time)])
            print("setting screen time to "+str(screen_time))
        else:
            print("screen times are equal")
