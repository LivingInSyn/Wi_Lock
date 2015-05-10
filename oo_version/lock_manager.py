import subprocess

class Lock_Manager:
    def __init__(self):
        def_locktime = 300
            
    def set_locktime(self,lock_time):
        subprocess.call(['gsettings','set','org.gnome.desktop.session','idle-delay',str(lock_time)])
        
    def get_locktime(self):
        locktime = subprocess.call(['gsettings','get','org.gnome.desktop.session','idle-delay'])
        return locktime
