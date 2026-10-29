"""Send one image to the running service and print the prediction."""
import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('image', help='Path to a PNG or JPEG image')
parser.add_argument('--url', default='http://localhost:8000/predict')
args = parser.parse_args()
with open(args.image, 'rb') as image:
    response = requests.post(args.url, files={'file': image}, timeout=60)
print(response.status_code, response.json())
response.raise_for_status()
