# import boto3
# from botocore.exceptions import PaginationError
# vpcClient=boto3.client("ec2",region_name="ap-northeast-1") #vpc-0ada29c375918795b

# def fnVPCDiscribe(tagKey,tagValues,maxItems=5):
#     from botocore.exceptions import ClientError
#     vpclist=[] 
#     try:

#         paginator=vpcClient.get_paginator("describe_vpcs")
#         response_iterator=paginator.paginate(Filter=[
#             {
#                 'Name':f'tag:{tagKey}',
#                 'Values':tagValues
#             }
#             ],paginationConfig={'MaxItem':maxItems})
#         full_result=response_iterator.build_full_result()
#         for page in full_result["Vpcs"]:
#             vpcList.append(page)
#         print("Listing VPC Done")
#     except ClientError as ce:
#         print("Found Error:",ce)
#     return vpcLists            

# if __name__=="__main__":

#     vpcLists=fnVPCDiscribe(tagKey="Name",tagValues=["biljo"],maxItems=10)
#     for vpc in VpcLists:
#         print( vpcId )        

import boto3

vpcClient=boto3.client("ec2",region_name="ap-southeast-2") #vpc-0ada29c375918795b



def fnVPCDescribe(tagKey,tagValues,maxItems=5):

    from botocore.exceptions import ClientError

    vpcLists=[]

    try:

        paginator=vpcClient.get_paginator("describe_vpcs")

        response_iterator=paginator.paginate(Filters=[

            {'Name':f'tag:{tagKey}',

             'Values':tagValues

            }

            ],PaginationConfig={'MaxItems':maxItems})  
        full_result=response_iterator.build_full_result()

        for page in full_result["Vpcs"]:

            vpcLists.append(page)

        print("Listing vpc done")

    except ClientError as ce:

        print("Found error",ce)

    return vpcLists



#driver code- workflow

if __name__=="__main__":

    vpcLists=fnVPCDescribe(tagKey="Name",tagValues=["biljo"],maxItems=10)

    for vpc in vpcLists:

        print( vpc )
