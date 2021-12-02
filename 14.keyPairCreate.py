import boto3

# ec2=boto3.resource("ec2")
# key_pair=ec2.KeyPair("kp02mujahed")
# print(key_pair)

ec2=boto3.client("ec2",region_name="ap-southeast-2")
myKeyName="biljo098"
response=ec2.create_key_pair(KeyName=myKeyName)
with open(myKeyName+".pem","w") as f:
    f.write(response["KeyMaterial"])
print(response)
