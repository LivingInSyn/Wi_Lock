import atexit
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
        
    def run(self):
        while 1:
            current_network = self.w_handler.current_network()
            if(current_network in self.trusted_networks):
                self.l_manager.set_locktime(self.trust_time)
                print('trusted network')
            else:
                self.l_manager.set_locktime(self.no_trust_time)
                print('not trusted network')
            time.sleep(30)
            print('debug_ping')



if __name__ == '__main__':
    main_app = Wi_Lock()
    main_app.run()



#NEED AN EXIT HANDLER
'''
def exit_handler():
    print("hit the exit handler")
    set_locktime(no_trust_time
'''
