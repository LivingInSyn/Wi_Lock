import lock_manager

l_manager = lock_manager.Lock_Manager()

#print(l_manager.get_locktime())
print("trying to change locktime now")
l_manager.set_locktime(200)
#print(l_manager.get_locktime())
