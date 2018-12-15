import boto3

# import from elsewhere
# Django "settings" module

AWS_ACCESS_KEY_ID = 'AKIAJMLS2HKIPMBXJMMA' 
AWS_SECRET_ACCESS_KEY = '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'
AWS_S3_REGION_NAME = 'us-east-1'
AWS_STORAGE_BUCKET_NAME = 'aws-cfe-intro'

class AWS:
    access_key      = AWS_ACCESS_KEY_ID
    secret_key      = AWS_SECRET_ACCESS_KEY
    region          = AWS_S3_REGION_NAME
    bucket          = AWS_STORAGE_BUCKET_NAME

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_s3_client(self):
        s3_client = boto.client('s3'
                aws_access_key_id=self.access_key,
                aws_secret_access_key=self.secret_key,
                region_name = self.region
            )
        return s3_client

    def get_download_url(self):
        return 

    def presign_post_url(self):
        return 


# AWS().get_download_url()

