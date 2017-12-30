import boto3
import os
import subprocess

# configuration 
num_workers = 1
bucket_name = 'terasort-yawen'

# the file to be sorted should be partitioned into "num_worker" number of files 
# as inputs to the map stage; 
# specify directory that contains files to be sorted: input1, input2, etc. 
path_local = 'input_files/' 
path = "100_100M_1/"
file_name = 'input'
concat_file_name = path_local + path + file_name
s3_client = boto3.client('s3')

for j in range(100):
    # generate 100 100MB 
    begin_file_index = str(j*100)
    begin_record_index = str(j*100000000)
    p = subprocess.call(["sh", "data_gen.sh", "100", "100000000", "100_100M_1", begin_record_index, begin_file_index])
    	
    # upload n input files to S3 (inputs to the mapper stage)
    num_workers = 100
    for i in range(num_workers):
        result = s3_client.put_object(
            Bucket = bucket_name,
            Body = open(concat_file_name + str(i+j*100), 'rb'),
            Key = "1TB/" + file_name + str(i+j*100)
        )

    p = subprocess.call(["rm", "-rf", path_local+path])


