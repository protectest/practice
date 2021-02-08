import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}
souce = list()

for i in range(0, 10):
    page = 25*i

    url = "https://movie.douban.com/top250?start=" + str(page)

    data = requests.get(url, allow_redirects=False, headers=headers)

    if data.status_code != 200:
        print("状态码为{}，第{}页请求失败".format(data.status_code, i))
        continue
    else:
        print("正在获取第{}页的内容".format(i))
    soup0 = BeautifulSoup(data.text, 'lxml')
    ol = soup0.find_all(name='ol', attrs='grid_view')
    soup1 = BeautifulSoup(str(ol[0]), 'lxml')
    li = soup1.find_all('li')
    for j in li:
        movie = []
        soup2 = BeautifulSoup(str(j), 'lxml')
        title = soup2.span.string
        movie.append(title)
        try:
            soup3 = BeautifulSoup(str(soup2.find_all(name='p', attrs='')[0]), 'lxml')
            information = str(soup3.p)[12:].replace("<p class="">", "").replace("<br/>", "").replace("</p>", "")\
                .replace("\n", " ")
            movie.append(information)
        except IndexError:
            pass
        try:
            soup3 = BeautifulSoup(str(soup2.find_all(name='p', attrs='quote')[0]), 'lxml')
            quote = soup3.span.string
            movie.append(quote)
        except IndexError:
            pass
        href = soup2.a['href']
        movie.append(href)
        souce.append(movie)

for i in souce:
    print(i)
