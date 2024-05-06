import requests
import io
from PIL import Image



RealVisXL_V4_checkpoint = "https://api-inference.huggingface.co/models/SG161222/RealVisXL_V4.0"
runwayml_checkpoint= "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
cetusmix_v4 = "https://api-inference.huggingface.co/models/redstonehero/cetusmix_v4"
headers = {"Authorization": "Bearer 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"}



def RealVisXL(text):
	response = requests.post(RealVisXL_V4_checkpoint, headers=headers, json=text)
	return response.content

def runwayml(text):
	response = requests.post(runwayml_checkpoint, headers=headers, json=text)
	return response.content

def cetusmix(text):
	response = requests.post(cetusmix_v4, headers=headers, json=text)
	return response.content


def convert_bytes_to_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    return image