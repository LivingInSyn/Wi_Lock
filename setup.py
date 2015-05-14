'''
By Jeremy Mill

jeremymill@gmail.com
github.com/livinginsyn

licensed until the GPL V2
'''
import shutil
import os
import subprocess
#setup.py

failed = False

#check python version
if sys.version_info >= (3,0):
    print("you must run this with python v2")
    failed = True

#check if we're root/sudo
if not failed:
    if os.geteuid() != 0:
        print("You must be root!")
        failed = True

#check dependencies
'''#needs upstar / needs wpacli / needs gsettings'''
if not failed:
    print('checking dependencies')
    #not that initctl **IS** upstart
    depenencies = ['gsettings','wpacli','initctl']
    for depend in dependencies:
        try:
            subprocess.call([depend])
        except OSError:
            print("Failed on "+depend+"\n")
            failed = True

    
#make directory structure
'''/etc/wi_lock'''
print("creating directories")
if not failed:
    if not os.path.exists('/etc/wi_lock'):
        os.makedirs('/etc/wi_lock')
    else:
        print("directory already exists, overwriting file in the directory")
    

#copy files to etc
files = ['config_handler.py','lock_manager.py','post_stop.py','wifi_handler.py','wi_lock.cfg','wi_lock.py']
destination = "/etc/wi_lock/"
for tocopy in files:
    if not failed:
        try:
            print("Copying "+tocopy+"\n")
            shutil.copy(tocopy,destination)
        except IOError:
            print("missing file "+tocopy+"\n")
            print("installation failed\n")
            failed = True

#copy conf to etc/init
if not failed:
    try:
        shutil.copy('wi_lock.conf','/etc/init/')
    except IOError:
        print("missing conf file\n")
        print("program can still be launched manually, but can't start as a service")

print("You can start the service by running 'sudo service wi_lock start'\n")


print("Done")
