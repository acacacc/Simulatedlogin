# -*- coding:utf-8 _*-
"""
@Author:qzx 
@File:{NAME}.py
@Time:NAME.py@Time:{DATE} 下午 08:07

"""

import sys
import sys_gui
import io
import hashlib
import re
import random
import requests
import pymysql
from urllib import  request
from http import cookiejar
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

global g_cookie

def getCookieByRequestUrl(response):
    """
    根据请求的响应获取cookie信息
    """
    cookiejar = response.cookies

    # 将CookieJar转为字典：
    cookiedict = requests.utils.dict_from_cookiejar(cookiejar)

    return cookiedict['ASP.NET_SessionId']

def getYZMImage(url):
    """
    请求验证码的网址，下载验证码信息
    """
    cookievalue = 'ASP.NET_SessionId=' + str(g_cookie)

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Cookie': cookievalue,
        'Host': '',
        'Origin': '',
        'Referer': '',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    captcha(response.content)

def md5(str):
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    return m.hexdigest()

def captcha(data):
    """
    保存验证码图片到本地
    """
    with open('code.jpg', 'wb') as fp:
        fp.write(data)
    pix = QPixmap("code.jpg")
    ui.code_pic.setPixmap(pix)

def get_cookie():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
        'Cookie': 'name=value; UM_distinctid=1748faead8613a-0c46b93b56a09d-3323767-144000-1748faead88203; name=value;ASP.NET_SessionId=f5ikta2pgnizenn0042aga45'
    }
    response = requests.get("", headers=headers)
    global g_cookie
    g_cookie = getCookieByRequestUrl(response)


def login():
    loginhomeheaders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
        'Cookie': g_cookie,
        'Referer': ''
    }

    response = requests.get("", headers=loginhomeheaders)
    VIEWSTATE = re.search(r'<input type="hidden" name="__VIEWSTATE" value="(.*)"', response.text).group(1)

    userid = ui.UserName.text()
    pwd = ui.PassWord.text()
    verty_text = ui.code_de.text()

    dsdsdsdsdxcxdfgfg = md5(userid + md5(pwd)[:30].upper() + "10000")[:30].upper()  # userid为用户账号，即学号
    fgfggfdgtyuuyyuuckjg = md5(md5(verty_text.upper())[:30].upper() + "10000")[:30].upper()  # verty_text为验证码
    #组拼 data
    login_data  = {
        '__VIEWSTATE':VIEWSTATE,
        'pcInfo':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36undefined5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36 SN:NULL',
        'txt_mm_expression':'',
        'txt_mm_length': '',
        'txt_mm_userzh': '',
        'typeName':'%D1%A7%C9%FA',
        'dsdsdsdsdxcxdfgfg': dsdsdsdsdxcxdfgfg,
        'fgfggfdgtyuuyyuuckjg':fgfggfdgtyuuyyuuckjg,
        'Sel_Type': 'STU',
        'txt_asmcdefsddsd':userid,
        'txt_pewerwedsdfsdff':'',
        'txt_psasas':'%C7%EB%CA%E4%C8%EB%C3%DC%C2%EB',
        'txt_sdertfgsadscxcadsads':'',
    }

    cookievalue = 'ASP.NET_SessionId=' + str(g_cookie)
    login_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
        'Cookie':cookievalue,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '6442',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host':'',
        'Origin': '',
        'Referer': '',
        'Upgrade-Insecure-Requests': '1'
    }

    loginurl = ""

    session = requests.session()
    response = session.post(url=loginurl,data=login_data,headers=login_headers)

    getinfoheaders = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
        'Cookie': cookievalue,
        'Referer': '',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Host': '',
        'Upgrade-Insecure-Requests': '1'
    }
    response1 = session.get(url="",headers=getinfoheaders)
    pattern = re.compile('''姓&ensp;&ensp;&ensp;&ensp;名</td><td colspan='2'>(.*?)<br>''')
    m = pattern.findall(response1.text)
    print(m)
    compare(m,userid)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = QMainWindow()
    ui = sys_gui.Ui_Form()
    ui.setupUi(Window)
    Window.show()

    get_cookie()
    url = "" + str(random.randint(0, 999))
    getYZMImage(url=url)
    
    ui.log_in.clicked.connect(login)

    sys.exit(app.exec_())



