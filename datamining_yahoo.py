import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://tw.news.yahoo.com/finance"

headers = {
    "user-agent":"user-agent"
}

resp =requests.get(url, headers = headers, timeout=3)

soup = BeautifulSoup(resp.text,"lxml")

title_list = []
link_list = []
elem = soup.find_all("h3", class_="Mb(5px)")
for e in elem:
    link_list.append(e.find("a").get('href'))
    title_list.append(e.text)

df = pd.DataFrame({"title":title_list, "link":link_list})
df.to_csv("Yahoo_news.csv", index=0)