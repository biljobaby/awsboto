# import boto3
# from botocore.exceptions import ClientError

# # vpcClient=boto3.client("ec2")

# vpcId="Not set"

# def fnCreateCustomVPC(vpcResource,IpCidr):
#     from botocore.exceptions import ClientError
#     vpcId="Not set"
#     try:
#         response=vpcResource.create_vpc(cdirBlock=IpCidr,
#         InstanceTenancy="default",
#         TagSpecifications=[{"ResourceType":"vpc","Tags":[{'Key':'name','Value':'biljo'}]}]
#         )
#         vpcId=response.id
#         print("Created Default vpc")
#     except ClientError as ce:
#         print("not possible to create",ce)
# #driver   code  

# if __name__=="__main__":
#     vpcclient=boto3.resource("ec2",region_name="eu-central-1")
#     ip_cidr="192.168.0.0/26" #64
#     vpcId=fnCreateCustomVPC(vpcclient,ip_cidr)
#     print(vpcId)        

import boto3



def fnCreateCustomVPC(vpcResource,IpCidr):

    from botocore.exceptions import ClientError

    vpcId="not set"

    try:

        response=vpcResource.create_vpc(CidrBlock=IpCidr,

        InstanceTenancy="default",

        TagSpecifications=[{"ResourceType":"vpc","Tags":[{'Key':'Name','Value':'biljo'}]}]

        )

        vpcId=response.id

        print("create default vpc")

    except ClientError as ce:

        print("not possible to create",ce)

    return vpcId



#driver code- workflow

if __name__=="__main__":

    vpcresource=boto3.resource("ec2",region_name="ap-southeast-2")

    ip_cidr="192.168.2.0/26"

    vpcId=fnCreateCustomVPC(vpcresource,ip_cidr)

    print( vpcId )