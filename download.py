import os
import argparse
from PIL import Image, UnidentifiedImageError
from minio import Minio


minio_client = Minio(
        endpoint='127.0.0.0:9000',
    access_key='jsdskfjlskflsdjk',
    secret_key='UDxxm6sz3',
    secure=True  # Set to False for an insecure connection (HTTP instead of HTTPS)
)

buckets = minio_client.list_buckets()
for bucket in buckets:
    print(bucket.name)

# Specify the bucket name, prefix (folder path), and local destination path
bucket_name = 'test'
prefix = 'uploads_test/'
local_path = './my_download/'
file_formats = ['png', 'jpeg', 'jpg']





def download_folder(minio_client, bucket_name, prefix, local_path, file_formats):
    objects = minio_client.list_objects(bucket_name, prefix=prefix, recursive=True)
    for obj in objects:
        if obj.is_dir:
            continue
        file_path = obj.object_name
        file_extension = file_path.split('.')[-1].lower()
        if file_extension not in file_formats:
            continue
        dest_path = file_path.replace(prefix, local_path, 1)
       # minio_client.fget_object(bucket_name, file_path, dest_path)
        minio_client.fget_object(bucket_name, file_path, dest_path, request_headers={'X-Amz-Consumer-Input-Download-Rate-Limit': str(1024)})
        print(f"this source  {file_path} Downloaded")




download_folder(minio_client, bucket_name, prefix, local_path,file_formats)

