import pywren
#from redis import Redis

def my_function(x):
    from redis import Redis
    
    gateway_ip = '54.212.247.168'
    gateway_port = 8888
    bind_port = 50001
    redis = Redis(gateway_ip, int(gateway_port), bind_port=int(bind_port))

    result = []
    foo = redis.get('foo')
    result.append( foo)
    foo = redis.get('boo')
    result.append(foo)
   
    return result

wrenexec = pywren.default_executor()
future = wrenexec.call_async(my_function, 3)

print future.result()



