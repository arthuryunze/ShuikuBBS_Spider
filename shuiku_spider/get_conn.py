import requests


def get_conn(url):
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
    html = requests.get(url,headers=header)
    html.raise_for_status()
    html.encoding=html.apparent_encoding
    return html