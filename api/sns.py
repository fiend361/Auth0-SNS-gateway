
import boto3
from botocore.exceptions import ClientError

sns_resource = boto3.resource('sns')

def publish_text_message(phone_number, message):
    try:
        response = sns_resource.meta.client.publish(
            PhoneNumber=phone_number, Message=message)
        message_id = response['MessageId']
        
    except ClientError:
        raise
    
    else:
        return message_id