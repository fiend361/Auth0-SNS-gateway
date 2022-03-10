import os

import boto3
from botocore.exceptions import ClientError

IAM_USER_ACCESS_KEY_ID = os.environ['IAM_USER_ACCESS_KEY_ID']
IAM_USER_SECRET_ACCESS_KEY = os.environ['IAM_USER_SECRET_ACCESS_KEY']

sns_resource = boto3.resource('sns',
                              aws_access_key_id=IAM_USER_ACCESS_KEY_ID, 
                              aws_secret_access_key=IAM_USER_SECRET_ACCESS_KEY)

def publish_text_message(phone_number, message):
    try:
        response = sns_resource.meta.client.publish(
            PhoneNumber=phone_number, Message=message)
        message_id = response['MessageId']
        status_code = response['ResponseMetadata']['HTTPStatusCode']
        
    except ClientError:
        raise
    
    else:
        return message_id, status_code