from selenium import webdriver
import time
from libs.secret_key import my_pw,my_id
import bs4

url = "http://www.hungryboarder.com/index.php?mid=Openmarket11"
rootPath = ".."
driver = webdriver.Chrome(
    executable_path="{}/webdriver/chromedriver.exe".format(rootPath)
)
driver.get(url)

driver.find_element_by_xpath("//*[@id='access']/div[2]/p/a[2]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='uid']").send_keys(my_id)
driver.find_element_by_xpath("//*[@id='upw']").send_keys(my_pw)
driver.find_element_by_xpath("//*[@id='fo_member_login']/fieldset/div[2]/input").click()
shop = bs4.BeautifulSoup(driver.page_source,"html.parser")

shop_item1 = shop.findAll("tr",{"class":"bg1"})
shop_item2 = shop.findAll("tr",{"class":"bg2"})

for item in shop_item1:
    shop_item_title = item.find("td",{"class":"title"})
    shop_item_category = shop_item_title.find("strong",{"class":"category"}).text
    shop_item_name = shop_item_title.find("a").text
    shop_item_price = item.find("td",{"class":"price"}).text
    print(shop_item_category,shop_item_name,shop_item_price)


