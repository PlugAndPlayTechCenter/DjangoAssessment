import ptvsd

def wait_debug():
    ptvsd.enable_attach(address = ('0.0.0.0', 3001))
    print('wait for attach')
    ptvsd.wait_for_attach()
    print('attached')
