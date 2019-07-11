# -*- coding="utf-8" -*-
import requests
from get_conn import *
from save_file import *
from bs4 import BeautifulSoup

url_jichupian = "http://www.shuikult.net/html/meida/"


#取得url的response

#基础篇
def get_need_urls(url):
    m_list = []
    for page in range(1,26):
        url = url+"list_1_"+str(page)+".html"
        m_list.append(url)
    return m_list


# 基础篇的url
# url = url+"list_1_"+str(page)+".html"


num = 0


def analysis(html):
    global num
    rset = []
    soup = BeautifulSoup(html,'html.parser')
    soup = soup.find_all("ul")[1]
    soup = soup.find_all("h3")
    for item in soup:
        rset.append(item.get_text())
        num = num + 1
    return str(rset), num


def get_article(html):
    list = []
    soup = BeautifulSoup(html, 'html.parser')
    soup = soup.find_all("ul")[1]
    soup = soup.find_all("h3")
    for item in soup:
        url = item.find_all("a")[0].get('href')
        list.append("http://www.shuikult.net"+url)
    return list


def save_article(list):
    nm = 1
    for url in list:
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
        html = requests.get(url, headers=header)
        html.encoding=html.apparent_encoding
        soup = BeautifulSoup(html.text, 'html.parser')
        soup = soup.find_all("div",class_="inner")[0]
        soup = soup.find_all("div")[2]
        txt = soup.get_text()
        with open("article/"+str(nm)+".txt", "a", encoding="utf-8") as f:
            f.write(txt)


# 基础篇共25页 试出来
# page = 25
def article_content():
    with open("a.txt", "w", encoding='utf-8') as fa:
        num=0
        txt=""
        tmp=""
        for page in range(1, 26):
            text, num = analysis(get_conn(url_jichupian).text)
            tmp=tmp + text
        txt=txt+"共有"+str(num)+"篇文章"
        txt = txt + tmp

        fa.write(txt)



def get_article_content():
    print("正在获取文章目录...")
    content_list = []
    href_list = []
    txt=""
    for page in range(1,26):
        #取得url内容
        htmltext = get_conn(url_jichupian+"list_1_"+str(page)+".html").text
        soup = BeautifulSoup(htmltext, 'html.parser')
        soup = soup.find_all("ul")[1]
        soup = soup.find_all("h3")
        for item in range(soup.__len__()):
            title = soup[item].get_text()
            content_list.append(title)
    save_list(content_list)


#传入一个list
#list将转化为字符串每项加换行并保存到a.txt中
def save_list(m_list):
    txt = ""
    for item in m_list:
        txt = txt+item+'\n'
    file_name = input("要保存哪个文件:")
    save_out(txt,file_name)


#功能选择界面
def choose_menu():
    while True:
        txt = "选择功能:\n1.获取水库论坛基础篇文章目录\n2.退出程序\n"
        choose = input(txt)
        if choose==str(1):
            get_article_content()
        elif choose==str(2):
            exit()
        else:
            print("\n输入有误,请重新输入!\n")



choose_menu()
