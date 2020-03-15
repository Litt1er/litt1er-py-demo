#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import bs4
import re
import send_mail



express_itmes = ['sfexpress','yunda','sto','yto','zto','ems','ttdex','htky','qfkd','chinapost']
request_url = 'http://m.46644.com/express/result.php?typetxt=%D6%D0%CD%A8&type=express_type&number=express_number'


def get_express_info_with_number(number):
    express_info = []
    for item in express_itmes:
        url = request_url.replace('express_type', item).replace('express_number',number)
        response = requests.get(url)
        response.encoding = 'gb18030'
        response = response.text
        soup = bs4.BeautifulSoup(response, 'html.parser', from_encoding='utf-8')
        for i in soup.findAll(name='div', attrs={'class': 'icontent'}):
            desc_text = i.get_text()
            if '错误' not in desc_text and '不存在' not in desc_text:
                express_info.append(i.get_text())
                continue
    return express_info


if __name__ == '__main__':
    ifno = get_express_info_with_number('YT9107697526961')
    send_mail.send('litt1er@163.com', '快递物流进度推送', ifno)
    print(ifno)