import boto3
# s3=boto3.client("s3")
# response=s3.list_buckets()
# for b  in response["Buckets"]:
#     print (b["Name"],end="")

# for b in response["Buckets"]:

#     if b["Name"] == "stiwari2boto3lab0112221":

#         print (b["Name"])

s3=boto3.resource("s3")
iterator=s3.buckets.all()

for b in iterator:
    print(f"*{b.name}")