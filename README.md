# Wi_Lock
change the lock-screen time depending on what wifi network you are connected to

Wi_Lock uses python and upstart to monitor the wifi connection and make changes to the gnome lock screen time and screensaver time based off of a list of trusted wifi networks. For instance, you can set your computer to never lock at home, but lock after 3 minutes while anywhere else. 

Wi_Lock leverages gsettings to monitor desktop settings and make changes to them, wpa_cli to monitor the wifi connection and upstart to run as a service.

##To Install:
* run 'git clone https://github.com/LivingInSyn/Wi_Lock.git'
* edit wi_lock.cfg
 * Add your trusted wifi networks to networks, such as 'networks=Linksys,Netgear-71,work-network'
 * set the locktime you want for when you're on a trusted network as a number from 0 to 1000, where 0 is never in 'trusted_time'
 * set the locktime you want for untrusted networks as a number from 0 to 1000 where 0 is never in 'no_trust_time'
 * set how long you want your screensaver to wait while on trusted networks as a number from 0 to 10000 in 'trusted_screen_time'
 * save and exit
* run 'sudo python setup.py'
* run 'sudo service wi_lock start'
* Enjoy!
