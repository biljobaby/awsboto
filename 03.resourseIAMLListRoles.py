import boto3

objeResource=boto3.resource('iam')

for r in objeResource.roles.all():
    print(r.name)