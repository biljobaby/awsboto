import boto3

rds=boto3.client("rds",region_name="ap-southeast-2")

response=rds.create_db_instance(
    AllocatedStorage=5,
    DBInstanceClass="db.t2.micro",
    DBInstanceIdentifier="dbv1biljo",
    Engine="MySQL",
    MasterUserPassword="testpwd0021",
    MasterUsername="admin01"
)

print(response)