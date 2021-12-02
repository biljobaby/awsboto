import boto3

vpcResource=boto3.resource("ec2",region_name="ap-southeast-2")

groupName="sgsample"
vpcId="vpc-0d062beff90d6598e"

response=vpcResource.create_security_group(
    Description="creating for demo purpose",
    GroupName=groupName,
    VpcId=vpcId,
    TagSpecifications=[{
        "ResourceType":"security-group",
        "Tags":[{'Key':'Name','Value':groupName}]
    }]
    )

print(response.id) #sg-08c2670561a3b9002