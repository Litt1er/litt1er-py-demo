#!/usr/bin/python
# -*- coding: UTF-8 -*-

mail_url = 'zsanjing@foxmail.com'
mail_host = 'smtp.qq.com'
password = 'mfvglfqyycfrcacg'


import yagmail


def send(target_mail, title, content):
    yag = yagmail.SMTP(user=mail_url, password=password, host=mail_host)
    yag.send(target_mail, title, content)
    print('邮件发送成功')


if __name__ == '__main__':
    send('litt1er@163.com', 'test', 'test!!!')