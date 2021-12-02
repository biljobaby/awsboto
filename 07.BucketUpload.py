import boto3
import pathlib

BASE_DIR=pathlib(__file__).parent.resolve()
bucket_name="xyz098"
file_name="requirement.txt"
objects_name=file_name

s3client=boto3.client("s3")
s3client.upload_file("C:\Users\Administrator\Desktop\boto\awsboto\requirement.txt",bucket_name,object_name)
print("file uploaded")