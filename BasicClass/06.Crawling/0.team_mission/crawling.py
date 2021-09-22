from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import json



class Crawling():

    browser = webdriver.Chrome('c:/driver/chromedriver.exe')
    url = "https://youtube-rank.com/board/bbs/board.php?bo_table=youtube"
    # browser.get(url)

    # html = browser.page_source
    # soup = BeautifulSoup(html, 'html.parser')
    # print(soup)

    # channel_list = soup.select('tbody > tr')


    def youtube_totalrank():
        browser = webdriver.Chrome('c:/driver/chromedriver.exe')
        url = "https://youtube-rank.com/board/bbs/board.php?bo_table=youtube"
        results = []
        for page in range(1, 11):
            url = f"https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page={page}"
            browser.get(url)
            time.sleep(2)
            html = browser.page_source
            soup = BeautifulSoup(html, 'html.parser')

            channel_list = soup.select('form > table > tbody > tr')
            for channel in channel_list:
                title = channel.select('h1 > a')[0].text.strip()
                category = channel.select('p.category')[0].text.strip()
                subscriber = channel.select('.subscriber_cnt')[0].text
                view = channel.select('.view_cnt')[0].text
                video = channel.select('.video_cnt')[0].text
                data = [title, category, subscriber, view, video]
                results.append(data)

            # print(results)
        browser.implicitly_wait(3)
        browser.quit()

        df = pd.DataFrame(results)
        print(df)
        df.columns = ['title', 'category', 'subscriber', 'view', 'video']
        df.to_excel('/files/youtube_rank.xlsx', index=False)


    def youtube_300rank_sub():
        browser = webdriver.Chrome('c:/driver/chromedriver.exe')
        url = "https://youtube-rank.com/board/?mid=home"
        results = []

        browser.get(url)
        time.sleep(2)
        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')
        while len(results) < 11:
            channel_list = soup.select('div.info')
            for channel in channel_list:
                title = channel.select('h3 > a')[0].text.strip()
                category = channel.select('p.cate')[0].text.strip()
                subscriber = channel.select('span.subscriber_cnt')[0].text
                view = channel.select('span.view_cnt')[0].text
                video = channel.select('span.video_cnt')[0].text
                data = [title, category, subscriber, view, video]
                results.append(data)

        # print(results)
        browser.implicitly_wait(3)
        browser.quit()

        # df = pd.DataFrame(results)
        # print(df)
        # df.columns = ['title', 'category', 'subscriber', 'view', 'video']
        # df = df.iloc[0:299,:]
        # df.to_excel('./files/youtube_300rank_sub.xlsx', index=False)
        return json.dumps(results)


    def youtube_300rank_video():
        browser = webdriver.Chrome('c:/driver/chromedriver.exe')
        url = "https://youtube-rank.com/board/?mid=home#"
        results = []

        browser.get(url)
        time.sleep(2)
        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')
        while len(results) < 11:
            channel_list = soup.select('div.info')
            for channel in channel_list:
                title = channel.select('h3 > a')[0].text.strip()
                category = channel.select('p.cate')[0].text.strip()
                subscriber = channel.select('span.subscriber_cnt')[0].text
                view = channel.select('span.view_cnt')[0].text
                video = channel.select('span.video_cnt')[0].text
                data = [title, category, subscriber, view, video]
                results.append(data)

        print(results)
        browser.implicitly_wait(3)
        browser.quit()

        # df = pd.DataFrame(results)
        # print(df)
        # df.columns = ['title', 'category', 'subscriber', 'view', 'video']
        # df = df.iloc[0:299,:]
        # df.to_excel('./files/youtube_300rank_sub.xlsx', index=False)
        return json.dumps(results)

    if __name__ == "__main__":
        # youtube_300rank_sub()
        youtube_300rank_video()
