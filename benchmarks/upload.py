import boto3
#boto3 already configured 

# configuration 
num_workers = 1
bucket_name = 'terasort-yawen'

# the file to be sorted should be partitioned into "num_worker" number of files 
# as inputs to the map stage; 
# specify directory that contains files to be sorted: input1, input2, etc. 
path_local = 'input_files/' 
path = "input_1_160K/"
file_name = 'input'
concat_file_name = path_local + path + file_name


s3_client = boto3.client('s3')

# upload n input files to S3 (inputs to the mapper stage)
for i in range(num_workers):
    result = s3_client.put_object(
        Bucket = bucket_name,
        Body = open(concat_file_name + str(i), 'rb'),
        Key = path + file_name + str(i)
    )


