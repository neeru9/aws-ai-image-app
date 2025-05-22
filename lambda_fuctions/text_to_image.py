import json
import boto3
import requests
import uuid
from datetime import datetime

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
TABLE_NAME = 'PromptGallery'
S3_BUCKET = 'your-s3-bucket-name'
CONTROLNET_SERVER = 'http://your-ec2-endpoint:5000/generate'

def lambda_handler(event, context):
    body = json.loads(event['body'])
    prompt = body['prompt']

    # Send request to EC2 ControlNet server
    response = requests.post(CONTROLNET_SERVER, json={'prompt': prompt})
    if response.status_code != 200:
        return {"statusCode": 500, "body": json.dumps({"error": "ControlNet server error."})}

    image_data = response.content
    image_key = f"text2img/{uuid.uuid4()}.png"

    # Upload image to S3
    s3.put_object(Bucket=S3_BUCKET, Key=image_key, Body=image_data, ContentType='image/png')
    image_url = f"https://{S3_BUCKET}.s3.amazonaws.com/{image_key}"

    # Save metadata to DynamoDB
    table = dynamodb.Table(TABLE_NAME)
    table.put_item(Item={
        'id': str(uuid.uuid4()),
        'prompt': prompt,
        'image_url': image_url,
        'timestamp': datetime.utcnow().isoformat()
    })

    return {
        'statusCode': 200,
        'body': json.dumps({
            'image_url': image_url
        })
    }