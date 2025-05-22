from flask import Flask, request, jsonify, send_file
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel, UniPCMultistepScheduler
from controlnet_aux import OpenposeDetector
import torch
from PIL import Image, ImageOps
from io import BytesIO
import boto3
import base64
import uuid
import json
import time

app = Flask(__name__)

# Load models for Feature 1
controlnet = ControlNetModel.from_pretrained(
    "lllyasviel/sd-controlnet-openpose", torch_dtype=torch.float16
)
pipe = StableDiffusionControlNetPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    controlnet=controlnet,
    torch_dtype=torch.float16
)
pipe.scheduler = UniPCMultistepScheduler.from_config(pipe.scheduler.config)
pipe.enable_model_cpu_offload()
openpose = OpenposeDetector.from_pretrained("lllyasviel/ControlNet")

# AWS Clients
s3 = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")
S3_BUCKET = "your-s3-bucket-name"
DDB_TABLE = dynamodb.Table("PromptGallery")

@app.route("/text2image", methods=['POST'])
def text_to_image():
    data = request.get_json()
    prompt = data.get('prompt', '')

    try:
        image = openpose("pose_sample.png")
        result = pipe(prompt, image=image, num_inference_steps=20).images[0]

        buffer = BytesIO()
        result.save(buffer, format='PNG')
        buffer.seek(0)

        key = f"text2image/{uuid.uuid4()}.png"
        s3.put_object(Bucket=S3_BUCKET, Key=key, Body=buffer.getvalue(), ContentType='image/png')
        image_url = f"https://{S3_BUCKET}.s3.amazonaws.com/{key}"

        return jsonify({"image_url": image_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/image2image", methods=['POST'])
def stylized_edit():
    image_file = request.files.get('image')
    if not image_file:
        return jsonify({'error': 'No image uploaded'}), 400

    image = Image.open(image_file.stream).convert('RGB')
    stylized = ImageOps.posterize(image, 3)

    buffer = BytesIO()
    stylized.save(buffer, format='PNG')
    buffer.seek(0)

    key = f"imageedit/{uuid.uuid4()}.png"
    s3.put_object(Bucket=S3_BUCKET, Key=key, Body=buffer.getvalue(), ContentType='image/png')
    image_url = f"https://{S3_BUCKET}.s3.amazonaws.com/{key}"

    return jsonify({"image_url": image_url})

@app.route("/gallery", methods=['GET'])
def gallery():
    try:
        response = DDB_TABLE.scan(Limit=20)
        items = sorted(response.get('Items', []), key=lambda x: x.get('timestamp', 0), reverse=True)
        return jsonify({"items": items})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/gallery", methods=['POST'])
def save_to_gallery():
    data = request.get_json()
    prompt = data.get('prompt', '')
    image_url = data.get('image_url', '')

    if not prompt or not image_url:
        return jsonify({"error": "Missing prompt or image_url"}), 400

    item = {
        'id': str(uuid.uuid4()),
        'prompt': prompt,
        'image_url': image_url,
        'timestamp': int(time.time())
    }

    try:
        DDB_TABLE.put_item(Item=item)
        return jsonify({"message": "Saved to gallery"})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
