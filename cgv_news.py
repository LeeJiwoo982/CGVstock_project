#일반 뉴스
URL = "https://n.news.naver.com/mnews/article/008/0004893680?sid=101"
def get_news(URL) :
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
    res = requests.get(URL, headers=headers)
    bs = BeautifulSoup(res.text, "html.parser")

    title = bs.select_one("h2").text.strip()
    date = bs.select_one(".media_end_head_info_datestamp_time ").text.split()[0]
    media = bs.select_one(".media_end_head_top img").attrs['alt']
    content = bs.select_one("#newsct_article").text.strip()

    return(title, date, media, content)