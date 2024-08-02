import requests
import io
from PIL import Image
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

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

def download_class(wd, delay, max_images):
    def scroll(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)

    url = "https://www.google.com/search?sca_esv=8c773456dd65c168&sca_upv=1&rlz=1C1RXQR_enCA1003CA1003&sxsrf=ADLYWIJ2h6MBLUFXjFXybZmGkdS0b06LMg:1722569590851&q=diseased+banana+tree&udm=2&fbs=AEQNm0CvspUPonaF8UH5s_LBD3JPX4RSeMPt9v8oIaeGMh2T2D1DyqhnuPxLgMgOaYPYX7OtOF4SxbM4YPsyWUMdeXRPnkQc3caC_NEMjyGZlBqX7YDVSc-lk14rE2h7j-ln6ORWjT4WxqVC6FS82YpEwEqqnkJJKpHqKGrk5ZhbNsOcE3i19GRoFANVfwr_gZS3oWcL17KMyupN4i8_p5OTUvqC1CSN_g&sa=X&ved=2ahUKEwiT58Dkr9WHAxUgkokEHQwXChYQtKgLegQIFBAB&biw=766&bih=694&dpr=2.5"
    wd.get(url)

    image_urls = set()

    while len(image_urls) < max_images:
        scroll(wd)

        thumbnails = wd.find_elements(By.CLASS_NAME, "YQ4gaf")

        for img in thumbnails[len(image_urls): max_images]:
            try:
                img.click()
                time.sleep(delay)
            except:
                continue

            images = wd.find_element(By.CLASS_NAME, "mNsIhb")

            for img in images:
                if img.get_attribute('src') and 'http' in img.get_attribute('src'):
                    image_urls.add(img.get_attribute('src'))
                    print(f"found {len(image_urls)}")

#download_image("", image_url, "test.jpg")
    return image_urls

urls = download_class(driver, 2, 3)
print(urls)
fruits = ['bananas', 'strawberries', 'apples', 'grapes', 'melons', 'avocados', 'mandarins', 'oranges', 'peaches', 'pineapple']
vegetables = ['potatoes', 'onions', 'tomatoes', 'lettuce', 'carrots', 'peppers', 'cucumbers', 'celery', 'brocolli']
