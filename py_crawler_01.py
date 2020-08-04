import bs4
import requests

def get_bs_obj():
    url = "https://finance.naver.com/item/main.nhn?code=005930"
    result = requests.get(url)
    bs_obj = bs4.BeautifulSoup(result.content,"html.parser")
    return bs_obj

def get_price(bs_obj):
    no_today = bs_obj.find("p", {"class": "no_today"})
    blind_now = no_today.find("span", {"class": "blind"})
    return blind_now.text

bs_obj = get_bs_obj()
price = get_price(bs_obj)
print(price)