# Wi_Lock
change the lock-screen time depending on what wifi network you are connected to

Wi_Lock uses python and upstart to monitor the wifi connection and make changes to the gnome lock screen time and
screensaver time based off of a list of trusted wifi networks. For instance, you can set your computer to never lock
at home, but lock after 3 minutes while anywhere else. 

Wi_Lock leverages gsettings to monitor desktop settings and make changes to them, wpa_cli to monitor the wifi 
connection and upstart to run as a service.

To Install:
Download the files to a directory and run 'sudo python setup.py', this will copy the neccesary files to /etc/wi_lock
and create an upstart service that will run at user logon. 
