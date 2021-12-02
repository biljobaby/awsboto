import boto3
from botocore.exceptions import ClientError

# vpcClient=boto3.client("ec2")

# vpcId=""
def fnCreatedDefaultVPC(vpcClient):
    try:
        response=vpcClient.create_default_vpc()
        vpcId=response["Vpc"]["VpcId"]
        print("Created Default vpc")
    except ClientError:
        print("not possible to create")
#driver        
if __name__=="__main__":
    vpcclient=boto3.client("ec2")
    vpcId=fnCreatedDefaultVPC(vpcclient)
    print(vpcId)        