import re

# 웹크롤링 지원 API
from bs4 import BeautifulSoup
from urllib.request import urlopen
from html import unescape
import requests

import cx_Oracle
import os


url = 'https://movie.naver.com/movie/running/current.nhn#'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)


movie = []
for movie_info in soup.html.select('.tit > a'):

    title = movie_info.string
    url = 'https://movie.naver.com' + movie_info["href"]

    # print(title)
    # print(url)



    movie.append({'title':title, 'url':url})
print(movie)