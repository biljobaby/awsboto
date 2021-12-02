import boto3

ec2=boto3.resource("ec2",region_name="ap-southeast-2")

keyPairName="biljo098" 
imageId="ami-0bd2230cfb28832f7"

instances=ec2.create_instances(
    MinCount=1,
    MaxCount=1,
    ImageId=imageId,
    InstanceType="t2.micro",
    KeyName=keyPairName,
    TagSpecifications=[{
        "ResourceType":"instance",
        "Tags":[{
            "Key":"Name",
            "Value":"inBiljo"
        }]
    }]
)

for instance in instances:
    print("Instance Created with id as: ",instance.id)

    instance.wait_until_running()
    print("Started")