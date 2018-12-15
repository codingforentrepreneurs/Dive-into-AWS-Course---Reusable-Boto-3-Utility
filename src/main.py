import boto3

# import from elsewhere
# Django "settings" module
AWS_ACCESS_KEY_ID = None
AWS_SECRET_ACCESS_KEY = None
AWS_S3_REGION_NAME = None
AWS_STORAGE_BUCKET_NAME = None

class AWS:
    access_key = AWS_ACCESS_KEY_ID

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_s3_client(self):
        return boto.client('s3')


