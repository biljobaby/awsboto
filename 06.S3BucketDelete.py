import boto3

# s3client=boto3.client("s3")
# s3client.delete_bucket(Bucket="mytestbkt2020202020")
# print("bucket deleted")
s3resource=boto3.resource("s3")
bucketName="fdghjklmdfghjk"
Bucket=s3resource.Bucket(bucketName)

def cleanup_bucket_objects(myBucket):
    for obj in myBucket.objects.all():
        obj.delete()
    for objver in myBucket.object_versions.all():
        obj.delete()

cleanup_bucket_objects(Bucket)

Bucket.delete()
