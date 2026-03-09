import boto3
bucket_name = "anuragmishra-de-project1-data-lake"
file_path = "tips.csv"
s3_key = "raw/tips.csv"

s3 = boto3.client("s3")

try:
    s3.upload_file(file_path, bucket_name, s3_key)
    print(f"Upload successful to s3://{bucket_name}/{s3_key}")
except Exception as e:
    print("Upload failed:", e)
