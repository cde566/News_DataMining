# News_DataMining
Data mining the public news from website in Python.

## Install
```shell
pip install beautifulsoup4 requests
```

## Start
The details are shown in [資料探勘(Data Mining)網路新聞](https://cde566.medium.com/python-%E7%B6%B2%E8%B7%AF%E6%96%B0%E8%81%9E%E7%9A%84data-mining-72bf15519a6d).

Here are two examples of data mining from news websites.
### ETtoday
Data mining the news from `ETtoday`.
Run `datamining_ettoday.py` to find out the `title` & `URL`, then results are saved in `ETtoday_news.csv`.
```sh
python datamining_ettoday.py
```

Data mining the news from `Yahoo News`.
Run `datamining_yahoo.py` to find out the `title` & `URL`, then results are saved in `Yahoo_news.csv`.
```sh
python datamining_yahoo.py
```
