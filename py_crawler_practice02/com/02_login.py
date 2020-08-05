from selenium import webdriver
from libs.MY_IDPW import my_id,my_pw
rootPath = ".."
driver = webdriver.Chrome(
    executable_path = "{}/webdriver/chromedriver.exe".format(rootPath)
)

url = "https://www.facebook.com/"
driver.get(url)

driver.find_element_by_id("email").send_keys(my_id)
#driver.find_element_by_id("pass").send_keys("")
driver.find_element_by_xpath("//*[@id='pass']").send_keys(my_pw)
driver.find_element_by_id("u_0_e").click()