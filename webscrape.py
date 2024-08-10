from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os
import requests
from PIL import Image
from io import BytesIO

fruits = ['bananas', 'strawberries', 'apples', 'grapes', 'melons', 'avocados', 'mandarins', 'oranges', 'peaches', 'pineapple']
vegetables = ['potatoes', 'onions', 'tomatoes', 'lettuce', 'carrots', 'peppers', 'cucumbers', 'celery', 'brocolli']


def download_images(object, number, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    driver = webdriver.Firefox()
    driver.get("https://images.google.com")

    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys(object)
    search_box.send_keys(Keys.RETURN)

    def scroll():
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Wait for images to load
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                try:
                    load_more_button = driver.find_element_by_css_selector('.mye4qd')
                    if load_more_button.is_displayed():
                        load_more_button.click()
                except Exception:
                    break
            last_height = new_height
    
    scroll()

    # Download images
    images = driver.find_elements(By.CLASS_NAME, "YQ4gaf")
    images = images[2:]
    downloaded = 0

    for i, img in enumerate(images):
        if downloaded >= number:
            break
        try:
            img_url = img.get_attribute('src')
            if img_url.startswith('http'):
                img_data = requests.get(img_url).content
                img_file = os.path.join(folder, f"{object}_{i+1}.jpg")
                
                with open(img_file, 'wb') as f:
                    f.write(img_data)
                
                downloaded += 1
                print(f"Downloaded {downloaded}/{number} images")
        except Exception as e:
            print(f"Failed to download image {i+1}: {e}")
