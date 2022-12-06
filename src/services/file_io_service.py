import os
import boto3
from botocore.exceptions import ClientError

class FileIOService(object):

    def __init__(self) -> None:
        self.s3_resource = boto3.resource(
            's3',
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
        )
        self.client = boto3.client('s3')
    
    def upload_file(self, file: any, bucket_name: str, file_name: str) -> bool:
        try:
            self.client.upload_file(file, bucket_name, file_name)
        except ClientError:
            return False
        return True

