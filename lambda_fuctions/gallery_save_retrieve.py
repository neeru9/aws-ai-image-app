import boto3
import json
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = 'PromptGallery'

def lambda_handler(event, context):
    table = dynamodb.Table(TABLE_NAME)

    if event['httpMethod'] == 'GET':
        # Retrieve latest 20 gallery items
        response = table.scan(Limit=20)
        items = sorted(response.get('Items', []), key=lambda x: x.get('timestamp', ''), reverse=True)

        return {
            'statusCode': 200,
            'body': json.dumps({
                'items': items
            })
        }

    return {
        'statusCode': 405,
        'body': json.dumps({'error': 'Method Not Allowed'})
    }
