'''
By Jeremy Mill

jeremymill@gmail.com
github.com/livinginsyn

licensed until the GPL V2
'''


import subprocess
import sys
import os


class Wifi_Manager:
    def __init__(self):
        #init vars with some default values, just in case something goes wrong. These should be 'safe values'
        #trusted_time is safe at 0 by default because trusted_networks is empty by default
        trusted_networks = []
        trusted_time = 0
        no_trust_time = 300
        
    def current_network(self):
        info = self.get_wpa_cli_status()
        start_index = info.find("\nssid")+6
        if(start_index != -1):
            stop_index = info.find("\n",start_index)
            ssid = info[start_index:stop_index]
            return ssid
        else:
            ssid = None
            return ssid
            
    def get_wpa_cli_status(self):
        info = subprocess.check_output(['wpa_cli','status'])
        return info

