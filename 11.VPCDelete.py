import boto3
import logging

#Logger Configuration
logger=logging.getLogger()
logging.basicConfig(level=logging.INFO,format='%(asctime)s:%(levelname)s: %(message)s')


vpcClient=boto3.client("ec2",region_name="ap-southeast-2") #vpc-0b5f3a16a5c5aac9e, ap-southeast-2  

def fnVPCDelete(vpcId):
    from botocore.exceptions import ClientError
    vpc=None
    try:
        vpc=vpcClient.delete_vpc(VpcId=vpcId)
        logger.info("Listing VPC Done")
    except ClientError as ce:
        print("Found Error: ",ce)
        logger.exception("Not Possible")
    return vpc

#Driver Code- Workflow
if __name__=="__main__":
    vpc=fnVPCDelete(vpcId="vpc-0b5f3a16a5c5aac9e")    
    print("deleted")