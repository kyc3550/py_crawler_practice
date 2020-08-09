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
html = bs4.BeautifulSoup(driver.page_source,"html.parser")

# shop_item1 = shop.findAll("tr",{"class":"bg1"})
# shop_item2 = shop.findAll("tr",{"class":"bg2"})

# for item in shop_item1:
#     shop_item_title = item.find("td",{"class":"title"})
#     shop_item_category = shop_item_title.find("strong",{"class":"category"}).text
#     shop_item_name = shop_item_title.find("a").text
#     shop_item_price = item.find("td",{"class":"price"}).text
#     print(shop_item_category,shop_item_name,shop_item_price)

shop = html.find("table",{"class":"boardList"})
item_list = shop.find("tbody")
items=item_list.select("tr.bg1,tr.bg2")
list = []
i=0
for item in items:
    try:
        shop_item_category = item.find("strong",{"class":"category"}).text
        shop_item_name = item.find("a").text
        shop_item_price = item.find("td", {"class": "price"}).text

        list.append(shop_item_name)
        print(shop_item_category,list[i],shop_item_price)
        i += 1
    except:
        shop_item_name = item.find("a").text
        shop_item_price = item.find("td", {"class": "price"}).text
        print("\t",shop_item_name,shop_item_price)
