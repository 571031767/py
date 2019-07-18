from bs4 import BeautifulSoup
import requests ,json ,time ,sys


if __name__ == '__main__':
    # target = 'http://gitbook.cn'
    target = 'https://unsplash.com/napi/feeds/home'
    headers = {'authorization':'Client-ID c94869b36aa272dd62dfaeefed769d4115fb3189a9d1ec88ed457207747be626'}
    req = requests.get(url=target,headers = headers  )
    html = json.loads(req.text)
    next_page = html['next_page']
    for each in  html['photos']:
        filaname = each['id']
        print('图片id'+ each['id'])


        time.sleep(1)

    # bf = BeautifulSoup(html)
    # texts = bf.find_all('div',class_ = "goods-list")
    print(html)
    # texts = texts[0].text

    # print(texts.repalce('\xa0'*8,'\n\n'))  #去掉八个空格符


