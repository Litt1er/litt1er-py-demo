#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import bs4
import send_mail


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
                # data = {
                #     'title': title.get('title'),
                #     'link': link.get('href')
                # }
                data = f'title='+title.get('title')+'link='+link.get('href')
                renting_list.append(data)

        start_index = start_index + 25

    return renting_list

if __name__ == '__main__':
    send_mail.send('1572503013@qq.com', '豆瓣租房推送', get_renting_info())