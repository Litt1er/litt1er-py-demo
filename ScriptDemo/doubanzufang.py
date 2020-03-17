#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import bs4
import send_mail
import schedule
import time


request_url = 'https://www.douban.com/group/shanghaizufang/discussion?start=start_index'


def get_renting_info():
    renting_list = []
    start_index = 0
    while start_index < 1000:
        url = request_url.replace('start_index', str(start_index))
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
        response = requests.get(url,headers=headers)
        response.encoding = 'utf-8'
        response = response.text
        soup = bs4.BeautifulSoup(response, 'lxml')
        titles = soup.select('td.title > a')
        links = soup.select('td.title > a')
        for title, link in zip(titles, links):
            if ('娄山关路' in title.get('title')):
                data = title.get('title')+link.get('href')
                renting_list.append(data)

        start_index = start_index + 25

    return renting_list

# 定义定时任务
def my_job():
    send_mail.send('fandu@pinduoduo.com', '豆瓣租房推送', get_renting_info())

if __name__ == '__main__':
    schedule.every(5).minutes.do(my_job)
    while True:
        schedule.run_pending()
        time.sleep(1)
