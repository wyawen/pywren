import pywren
import numpy as np
import redis
from rediscluster import StrictRedisCluster

def my_function_simple(x):
    return x + 7


def my_function(x):
    # cluster mode disabled: connect to node endpoint 
    #client = redis.Redis(host="rediscluster.a9ith3.clustercfg.usw2.cache.amazonaws.com", port=6379)
    
    # cluster mode enabled: connect to configuration endpoint 
    startup_nodes = [{"host": "rediscluster.a9ith3.clustercfg.usw2.cache.amazonaws.com", "port": "6379"}]
    client = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True, skip_full_coverage_check=True)

    key = "foo"+str(x)
    client.set(key, str(x))
    r = client.get(key)
    if (r is None):
        print "no such key"
        return -1
    if r == str(x):
        return "success! " + str(r)
    
    return "error " + str(r)


wrenexec = pywren.default_executor()
future = wrenexec.call_async(my_function, 3)
r = future.result()
print r 

futures = wrenexec.map(my_function, range(10))
r = pywren.get_all_results(futures)
print r


