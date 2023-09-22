import requests
from bs4 import BeautifulSoup
import pandas as pd

#뉴스 한 페이지 불러오기 #연예
# def get_Enews(URL) :
def get_Enews(URL) :
# URL ="https://entertain.naver.com/read?oid=112&aid=0003639934"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
    res = requests.get(URL, headers=headers)
    bs = BeautifulSoup(res.text, "html.parser")

    title = bs.select_one("h2.end_tit").text.strip()
    date = bs.select_one(".author em").text.split()[0]
    media = bs.select_one(".press_logo img").attrs['alt']
    content = bs.select_one("#articeBody").text.replace("\xa0","").strip()

    return(title, date, media, content, URL)

# 함수 실행이 안됨 왤까
# get_Enews("https://entertain.naver.com/read?oid=112&aid=0003639934")