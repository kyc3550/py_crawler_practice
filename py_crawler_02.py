import bs4
import requests

def get_bs_obj(company_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code
    result = requests.get(url)
    bs_obj = bs4.BeautifulSoup(result.content,"html.parser")
    return bs_obj

def get_price(company_code):
    bs_obj = get_bs_obj(company_code)
    no_today = bs_obj.find("p", {"class": "no_today"})
    blind_now = no_today.find("span", {"class": "blind"})
    return blind_now.text
# samsung 005930
# print(get_price("005930"))
# #hynix 000660
# print(get_price("000660"))
# kakao 035720
# print(get_price("035720"))

company_codes = ["005930","000660","035720"]
for item in company_codes:
    print(get_price(item))
