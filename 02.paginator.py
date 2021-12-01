import boto3

objClient=boto3.client('iam')
objPaginator=objClient.get_paginator('list_roles')

for page in objPaginator.paginate():
    for r in page['Roles']:
        print(r["RoleName"])
        
#     print(page)    
# print (objPaginator)
