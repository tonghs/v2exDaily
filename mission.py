#!/usr/bin/evn python
#coding:utf-8

import urllib
import urllib2


login_url = "http://www.v2ex.com/signin"
daily_url = "http://www.v2ex.com/mission/daily"
u = "tonghuashuai"
post_data = urllib.urlencode({
    "u": "tonghuashuai",
    "p": "tonghuashuai"
})

def login():
    req = urllib2.Request(login_url, data=post_data)
    content = urllib2.urlopen(req).read()
    content = urllib2.urlopen(daily_url).read()
    print content


if __name__ == "__main__":
    login()
