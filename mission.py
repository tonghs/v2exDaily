#!/usr/bin/evn python
#coding:utf-8

import requests
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

index_url = "http://www.v2ex.com"
login_url = "http://www.v2ex.com/signin"
daily_url = "http://www.v2ex.com/mission/daily"
headers = {
    "User-Agent": "UA",
    "Host": "v2ex.com",
    "Origin": "http://v2ex.com",
    "Referer": "http://www.v2ex.com/signin"
}

s = requests.Session()


def get_once_value():
    once_value = ''
    login_page = s.get(login_url, headers=headers, verify=False).text
    p_once = """<input type="hidden" value="\d+" name="once" />"""
    once_html = re.findall(p_once, login_page)

    if once_html:
        once_value = once_html[0]
        once_value = once_value.replace('<input type="hidden" value="', '')
        once_value = once_value.replace('" name="once" />', '')

    return once_value


def get_post_data():
    once_value = get_once_value()
    post_data = {
        "next": "/",
        "u": "tonghuashuai",
        "p": "tonghuashuai",
        "once": once_value ,
        "next": "/"
    }

    return post_data


def login():
    print "正在登录..."
    post_data = get_post_data()
    r = s.post(login_url, data=post_data, headers=headers, verify=False)
    get_balance()


def get_balance():
    balanch = 0
    r = s.get(index_url, headers=headers, verify=False)
    html= r.text
    with open("/Users/tonghs/Documents/git/v2exDaily/1.log", "w") as f:
        f.write(html)
    p = '<a href="/balance" class="balance_area" style="">.*?</a>'
    target = re.findall(p, html)
    if target:
        print "登录成功，获取账户余额..."
        txt = target[0]
    else:
        print "登录失败!!!"

    return balanch
    
if __name__ == "__main__":
    login()
