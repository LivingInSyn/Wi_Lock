import time 
import config_handler
import wifi_handler
import lock_manager

class Wi_Lock:
    def __init__(self):
        #create the config_handler, wifi_handler, lock_manager
        self.c_handler = config_handler.Config_Handler()
        self.w_handler = wifi_handler.Wifi_Manager()
        self.l_manager = lock_manager.Lock_Manager()
        
        #pull the config file and read it
        self.c_handler.read_config('wi_lock.cfg')
        self.trusted_networks = self.c_handler.get_networks()
        self.trust_time = self.c_handler.get_trusted_time()
        self.no_trust_time = self.c_handler.get_no_trust_time()
        self.trust_screen_time = self.c_handler.get_trusted_screen_time()
        
        #ignore for now
        #pull the current screen saver time
        #self.screen_time = self.l_manager.get_screen_saver_time()
        
        
        
    def run(self):
        a=0
        while 1:
            #get the current ssid
            current_network = self.w_handler.current_network()
            f = open('debug1','w')
            f.write('i hope this appears')
            f.close()          
            #if it's in trusted networks, do this
            if(current_network in self.trusted_networks):
                self.l_manager.set_locktime(self.trust_time)
                self.l_manager.set_screen_saver_time(self.trust_screen_time)
                f = open('debug_no','w')
                f.write('shouldnt appear')
                f.close()
                #print('trusted network')
            
            #if it's not in the whitelist, do this
            else:
                self.l_manager.set_locktime(self.no_trust_time)
                self.l_manager.set_screen_saver_time(0)
                f = open('debug_yes','w')
                f.write('i hope this appears')
                f.close()
                #print('not trusted network')
            
            #for debugging
            
            
            #wait 30 seconds and poll again
            time.sleep(30)
            print('debug_ping '+str(a))
            a=a+1
            
            
            
if __name__ == '__main__':
    main_app = Wi_Lock()
    main_app.run()


