import boto3
import base64
import json
import uuid
from PIL import Image, ImageOps
from io import BytesIO

s3 = boto3.client('s3')
S3_BUCKET = 'your-s3-bucket-name'

def lambda_handler(event, context):
    body = event['body']
    is_base64_encoded = event.get("isBase64Encoded", False)

    if is_base64_encoded:
        body = base64.b64decode(body)
    else:
        return {"statusCode": 400, "body": json.dumps({"error": "Image not base64 encoded."})}

    image = Image.open(BytesIO(body)).convert('RGB')
    stylized = ImageOps.posterize(image, 3)  # Example stylization

    # Save to buffer
    buffer = BytesIO()
    stylized.save(buffer, format='PNG')
    buffer.seek(0)

    image_key = f"imageedit/{uuid.uuid4()}.png"
    s3.put_object(Bucket=S3_BUCKET, Key=image_key, Body=buffer.getvalue(), ContentType='image/png')
    image_url = f"https://{S3_BUCKET}.s3.amazonaws.com/{image_key}"

    return {
        'statusCode': 200,
        'body': json.dumps({
            'image_url': image_url
        })
    }
