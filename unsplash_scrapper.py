from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time
import requests


# Launch Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://unsplash.com/")

# Let images load
#time.sleep(5)

#scroll-down
height = 0
for i in range(15):
    height = height + 500
    driver.execute_script(f"window.scrollTo(0, {height});")
    time.sleep(1)

# Get and print image URLs immediately (to avoid stale references)
images_tags = driver.find_elements(By.XPATH, "//img[@class='czQTa']")
images_urls = [img.get_attribute('src') for img in images_tags]


##download image
for index, url in enumerate(images_urls[:60]):
    response=requests.get(url,stream=True)
    with open(f'img-{index+1}.jpg','wb')as f:
        for chunk in response.iter_content(chunk_size=128):
            f.write(chunk)

driver.quit()
