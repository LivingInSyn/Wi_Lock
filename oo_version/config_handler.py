import ConfigParser
import sys
import os

class Config_Handler:
    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.path = self.find_current_dir()
        
    def read_config(self,config_file):
        self.config_path = os.path.join(self.path,config_file)
        self.config.read(self.config_path)
        self.trusted_networks = self.config.get('Networks','networks',0).split(',')
        self.trusted_time = int(self.config.get('Times','trusted_time',0))
        self.no_trust_time = int(self.config.get('Times','no_trust_time',0))
        self.trusted_screen_time = int(self.config.get('Times','trusted_screen_time',0)
        
    def get_networks(self):
        return self.trusted_networks
        
    def get_trusted_time(self):
        return self.trusted_time
        
    def get_no_trust_time(self):
        return self.no_trust_time
        
    def get_trusted_screen_time(self):
        return self.trusted_screen_time
        
    def find_current_dir(self):
        #returns the correct current working directory for exe's or py files
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)
        return application_path

