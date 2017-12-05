# PyWren-RedisLambda 

## Setup pywren 
```
git clone https://github.com/wyawen/pywren.git
cd pywren
git checkout redis_lambda
python setupscript.py #all the default settings can be used 
```
Add pywren to your PYTHONPATH by adding the following line to ~/.bashrc
```
export PYTHONPATH="${PYTHONPATH}:/path/to/pywren/" 
```

## Test for redis-lambda storage backend 
 
1. start EC2 gateway
2. start RedisLambda server (scripts located in redis_server)
3. run Pywren RedisLambda client (client benchmarks located in my_test)

## Generate data for terasort
```
cd my_test 
# to generate 10 files each with 100 records (each record is 100 bytes) and place them in the folder input_files
./data_gen.sh 10 100 input_files 
```
