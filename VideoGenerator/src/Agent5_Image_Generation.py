import requests
from PIL import Image
import io
import openai

class ImageGenerator:
    def __init__(self, api_key):
        """
        Initializes the ImageGenerator with the OpenAI API key.
        """
        openai.api_key = api_key

    def generate_images(self, video_outline):
        """
        Generates image URLs based on the video outline.
        """
        image_prompts = [
            f"A visually appealing image for the opening scene of: {video_outline}",
            f"An image for the main content of: {video_outline}",
            f"An image for the closing scene of: {video_outline}"
        ]

        image_urls = []
        for prompt in image_prompts:
            response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="512x512"
            )
            image_urls.append(response['data'][0]['url'])
        return image_urls

    def download_images(self, image_urls):
        """
        Downloads images from the provided URLs and returns them as PIL Image objects.
        """
        image_files = []
        for url in image_urls:
            response = requests.get(url)
            img = Image.open(io.BytesIO(response.content))
            image_files.append(img)
        return image_files