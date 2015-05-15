'''
By Jeremy Mill

jeremymill@gmail.com
github.com/livinginsyn

licensed until the GPL V2
'''

import subprocess
from subprocess import check_output
import re
import time
import os

class Lock_Manager:
    def __init__(self):
        def_locktime = 'bob'
    
    #the locktimes are how long until gnome thinks it's been idle        
    def set_locktime(self,lock_time):
        uid = self.get_uid_current()
        gid = self.get_gid_current()
        user=self.get_current_user()
        current_locktime = self.get_locktime(user)
        print("Current Locktime is " + str(current_locktime))
        print("Trying to change it to " + str(lock_time))
        if(current_locktime != lock_time):
            #get the current user so we can call the right sudo
            
            
            #this is the basic command we're going to run
            #sudo -u bobo -i dbus-launch --exit-with-session gsettings set org.gnome.desktop.session idle-delay 300 >/dev/null 2>&1
            cmd = ['sudo','-u',user,'-i','dbus-launch','--exit-with-session','gsettings','set','org.gnome.desktop.session','idle-delay',str(lock_time)]
            
            print("setting locktime to "+str(lock_time))
            FNULL = open(os.devnull, 'w')
            a = subprocess.call(cmd,stdout=FNULL,stderr=subprocess.STDOUT)
        else:
            print("No Change to Locktime")
        
    def get_locktime(self,user):
        #locktime = subprocess.call(['gsettings','get','org.gnome.desktop.session','idle-delay'])
        cmd =  ['sudo','-u',user,'-i','dbus-launch','--exit-with-session','gsettings','get','org.gnome.desktop.session','idle-delay']
        out = subprocess.check_output(cmd)
        print(out)
        return(int(out.split(" ")[1]))
    
    #the screensaver time is how long until it waits to go tothe screensaver. For the lock to work, 
    #the screensaver must come up when idle.
    def get_screen_saver_time(self,uid,gid):
        cmd = ['gsettings','get','org.gnome.desktop.screensaver','lock-delay']
        out = subprocess.check_output(cmd,preexec_fn=self.demote(uid,gid))
        #print(out)
        return(int(out.split(" ")[1]))
    
    def set_screen_saver_time(self,screen_time):
        uid = self.get_uid_current()
        gid = self.get_gid_current()
        current_screen_time = self.get_screen_saver_time(uid,gid)
        if(current_screen_time != screen_time):
            cmd = ['gsettings','set','org.gnome.desktop.screensaver','lock-delay',str(screen_time)]
            subprocess.call(cmd,preexec_fn=self.demote(uid,gid))
            print("setting screen time to "+str(screen_time))
        else:
            #print("screen times are equal")
            pass

    def get_current_user(self):
        out = subprocess.check_output(['users'])
        return(out.split(" ")[0])
        
    def get_gid_current(self):
        user = self.get_current_user()
        gid = subprocess.check_output(['id','-g',user])
        return(int(gid))
        
    def get_uid_current(self):
        user = self.get_current_user()
        uid = subprocess.check_output(['id','-u',user])
        return(int(uid))
        
    def demote(self,uid,gid):
        def set_ids():
            os.setgid(gid)
            os.setuid(uid)
        return set_ids
