import pywren
#from redis import Redis

def my_function(x):
    from redis import Redis
    
    gateway_ip = '54.212.247.168'
    gateway_port = 8888
    bind_port = 50001
    redis = Redis(gateway_ip, int(gateway_port), bind_port=int(bind_port))
    
    a = redis.set('foo', 'a')
    foo = redis.get('foo')
    
    return "Redis get reply: ", foo

wrenexec = pywren.default_executor()
future = wrenexec.call_async(my_function, 3)

print future.result()



