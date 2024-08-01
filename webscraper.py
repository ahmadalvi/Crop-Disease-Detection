import requests
import io
from PIL import Image
import time
from selenium import webdriver

driver = webdriver.Chrome()
image_url = "https://cdn.mos.cms.futurecdn.net/KS9aEnYxgn8yS68DgZmE5Z.jpg"

def download_image(download_path, url, filename):
    try:
        img_content = requests.get(url).content
        img_file = io.BytesIO(img_content)
        img = Image.open(img_file)
        file_path = download_path + filename

        with open(file_path, "wb") as f:
            img.save(f, "JPEG")

        print("Success")
    except Exception as e:
        print("FAILED - ", e)

def download_class():
    # TODO: We want to be able to iterate through the different fruits and vegetables to download 1000 image of each 
    return 0


download_image("", image_url, "test.jpg")

fruits = ['bananas', 'strawberries', 'apples', 'grapes', 'melons', 'avocados', 'mandarins', 'oranges', 'peaches', 'pineapple']
vegetables = ['potatoes', 'onions', 'tomatoes', 'lettuce', 'carrots', 'peppers', 'cucumbers', 'celery', 'brocolli']
