from __future__ import print_function
import os
import sys
import argparse
import boto3
import time
import mimetypes
from botocore.exceptions import ClientError


def upload_to_s3(str_bucket, artifact):
    try:
        print('Bucket path:', str_bucket)
        s3 = boto3.resource(
            's3',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )

        arr_bucket = str_bucket.split('/', 1)
        bucket_name = arr_bucket[0]
        bucket_key = arr_bucket[1]

        bucket = s3.Bucket(bucket_name)

        mimetypes.add_type('text/html',  '.mst')
        mimetypes.add_type('text/html',  '.hbs')
        mimetypes.add_type('font/woff2', '.woff2')
        mimetypes.add_type('application/json', '.map')
        mimetypes.add_type('text/markdown', '.md')
        mimetypes.add_type('text/x-scss', '.scss')
    except ClientError as err:
        print("Failed to create boto3 client.\n" + str(err))
        return False

    for root, dirs, files in os.walk(artifact, topdown=False):
        for file in files:
            try:
                print('Caminho no bucket:', os.path.join(root.replace(artifact, bucket_key), file))
                print('MimeType:', mimetypes.guess_type(file)[0])

                object = s3.Object(bucket_name, os.path.join(root.replace(artifact, bucket_key), file))

                response = object.put(
                    ACL='public-read',
                    Body=open(os.path.join(root, file), 'rb'),
                    Metadata={'uploadDate': time.strftime("%Y-%m-%d")},
                    ContentType=mimetypes.guess_type(file)[0]
                )

                # print('Response:', response, "\n")
            except ClientError as err:
                print("Failed to upload artifact to S3.\n" + str(err))
                return False
            except IOError as err:
                print("Failed to access artifact in this directory.\n" + str(err))
                return False
            except Exception as err:
                print(str(err))
                return False

    cf = boto3.client(
        'cloudfront',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )

    result = cf.create_invalidation(
        DistributionId=os.getenv('AWS_CF_DISTRIBUTION_ID'),
        InvalidationBatch={
            'Paths': {
                'Quantity': 1,
                'Items': [
                    '/*',
                ]
            },
            'CallerReference': str(time.time())
        }
    )

    while result['Invalidation']['Status'] != 'Completed':
        print('Waiting the invalidation to complete...\n')

        time.sleep(3)

        result = cf.get_invalidation(
            DistributionId=os.getenv('AWS_CF_DISTRIBUTION_ID'),
            Id=result['Invalidation']['Id']
        )

    print('Invalidation completed!\n')

    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("bucket_path", help="Name of the existing S3 bucket")
    parser.add_argument("artifact", help="Name of the artifact to be uploaded to S3")
    args = parser.parse_args()

    if not upload_to_s3(args.bucket_path, args.artifact):
        sys.exit(1)

if __name__ == "__main__":
    main()
