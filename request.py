from bs4 import BeautifulSoup
import requests


if __name__ == '__main__':
    # target = 'http://gitbook.cn'
    target = 'http://micuer.com/yhq/'
    req = requests.get(url=target)
    html = req.text
    bf = BeautifulSoup(html)
    texts = bf.find_all('div',class_ = "goods-list")
    print(texts)
    # texts = texts[0].text

    # print(texts.repalce('\xa0'*8,'\n\n'))  #去掉八个空格符


