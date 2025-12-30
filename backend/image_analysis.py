# image_analysis.py
from PIL import Image
import requests
from io import BytesIO

def analyze_image(url):
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        # Placeholder for AI analysis
        return "This image looks aesthetic and trendy."
    except:
        return "Image analysis failed."
