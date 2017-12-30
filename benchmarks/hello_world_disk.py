import pywren
import numpy as np
import subprocess
import boto3
import os

def my_function(x):
    result = []

    p = subprocess.Popen(["du", "-sh", "/tmp/runtimes"], stdout=subprocess.PIPE)
    p.wait()
    result.append(p.communicate()[0])
 
    p = subprocess.Popen(["ls", "-al", "/tmp/runtimes/2d348b9ce3eb659e7f6e281b80ca9688-15/condaruntime/bin"], stdout=subprocess.PIPE)
    p.wait()
    result.append(p.communicate()[0])
    '''
    size = os.stat("/tmp/pymodules").st_size   
    result.append("size of pymodules " + str(size))

    size = os.stat("/tmp/runtimes").st_size   
    result.append("size of runtimes " + str(size))

    p = subprocess.Popen(["df", "-h"], stdout=subprocess.PIPE)
    p.wait()
    result.append(p.communicate()[0])

    p = subprocess.Popen(["rm", "/tmp/runtimes"], stdout=subprocess.PIPE)
    p.wait()
    p = subprocess.Popen(["rm", "/tmp/condaruntime"], stdout=subprocess.PIPE)
    p.wait()
    p = subprocess.Popen(["rm", "/tmp/data.pickle"], stdout=subprocess.PIPE)
    p.wait()
    p = subprocess.Popen(["rm", "/tmp/func.pickle"], stdout=subprocess.PIPE)
    p.wait()
    p = subprocess.Popen(["rm", "/tmp/output.pickle"], stdout=subprocess.PIPE)
    p.wait()
    p = subprocess.Popen(["rm", "/tmp/pymodules"], stdout=subprocess.PIPE)
    p.wait()
    result.append(p.communicate()[0])


    p = subprocess.Popen(["ls", "-al", "/tmp"], stdout=subprocess.PIPE)
    p.wait()
    result.append(p.communicate()[0])

    p = subprocess.Popen(["df", "-h"], stdout=subprocess.PIPE)
    p.wait()
    result.append(p.communicate()[0])


    #p = subprocess.Popen(["rm", "-rf", "/tmp"], stdout=subprocess.PIPE)
    p = subprocess.Popen(["rm", "-rf", "/tmp/pymodules"], stdout=subprocess.PIPE)
    p.wait()
    result.append(p.communicate()[0])

    p = subprocess.Popen(["ls", "-al", "/tmp"], stdout=subprocess.PIPE)
    p.wait()
    result.append(p.communicate()[0])

    p = subprocess.Popen(["df", "-h"], stdout=subprocess.PIPE)
    p.wait()
    result.append(p.communicate()[0])
    '''


    return result 


wrenexec = pywren.default_executor()
future = wrenexec.call_async(my_function, 3)
#r = future.result()
for r in future.result():
    print r

