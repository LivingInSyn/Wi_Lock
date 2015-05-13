import config_handler
import lock_manager

class Post_Stop:
    def __init__(self):
        self.c_handler = config_handler.Config_Handler()
        self.l_manager = lock_manager.Lock_Manager()
        
        self.c_handler.read_config('wi_lock.cfg')
        self.no_trust_time = self.c_handler.get_no_trust_time()
        
        self.no_trust_settings()
        
        
    def no_trust_settings(self):
        self.l_manager.set_locktime(self.no_trust_time)
        self.l_manager.set_screen_saver_time(0)

if __name__=='__main__':
    main_app = Post_Stop()
