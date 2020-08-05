from selenium import webdriver
import time

driver = webdriver.Chrome(
    executable_path="../webdriver/chromedriver.exe"
)

url = "https://www.instagram.com/explore/tags/스노우보드/"
driver.get(url)
time.sleep(5)
pageString = driver.page_source

print(pageString)
driver.close()