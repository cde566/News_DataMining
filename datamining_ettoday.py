import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.ettoday.net/news/focus/3C%E5%AE%B6%E9%9B%BB/"

headers = {
    "user-agent":"user-agent"
}

resp =requests.get(url, headers = headers)  ##http requests

soup = BeautifulSoup(resp.text,"lxml") ##get html

elem = soup.find_all("div", class_="piece clearfix")


title_list = []
link_list = []
for e in elem:
    if e.select("a")[0].get('href').startswith("/new"):
        link_list.append(e.select("a")[0].get('href'))
        title_list.append(e.select("a")[0].get('title'))
  
df = pd.DataFrame({"title":title_list, "link":link_list})
df.to_csv("ETtoday_news.csv", index=0)