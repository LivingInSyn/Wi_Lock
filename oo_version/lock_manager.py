import subprocess

class Lock_Manager:
    def __init__(self):
        def_locktime = 300
    
    #the locktimes are how long until gnome thinks it's been idle        
    def set_locktime(self,lock_time):
        subprocess.call(['gsettings','set','org.gnome.desktop.session','idle-delay',str(lock_time)])
        
    def get_locktime(self):
        locktime = subprocess.call(['gsettings','get','org.gnome.desktop.session','idle-delay'])
        return locktime
    
    #the screensaver time is how long until it waits to go tothe screensaver. For the lock to work, 
    #the screensaver must come up when idle.
    def get_screen_saver_time(self):
        screen_time = subprocess.call(['gsettings','get','org.gnome.desktop.screensaver','lock-delay'])
    
    def set_screen_saver_time(self,screen_time):
        subprocess.call(['gsettings','set','org.gnome.desktop.session','idle-delay',str(lock_time)])
