import boto3

vpcClient=boto3.client("ec2",region_name="ap-southeast-2")
sgId="sg-08c2670561a3b9002"
# sgId="sg-034522349034616a1"
IPP1={
    "IpProtocol":"tcp",
    "FromPort":80,
    "ToPort":80,
    "IpRanges":[{"CidrIp":"0.0.0.0/0"}]
    }
# IPP2={
#     "IpProtocol":"tcp",
#     "FromPort":22,
#     "ToPort":22,
#     "IpRanges":[{"CidrIp":"0.0.0.0/0"}]
#     }
response=vpcClient.authorize_security_group_ingress(
    GroupId=sgId,
    IpPermissions=[IPP1]
)
import json
print(json.dumps(response,indent=4))
