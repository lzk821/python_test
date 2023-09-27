import urllib.request
# https://www.baidu.com/s?wd=迪迦
# http/https    www.baidu.com      80/443      s     w = 迪迦    #
#  协议            主机              端口号     路径     参数       锚点
# http 80 / https 443  / mysql 3306 /oracle 1521/ redis 6379 / mongodb 27017
url = "https://www.baidu.com"

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

# 因为urlopen方法中不能存储字典 所以headers不能传递进去
# 请求对象的定制
# 注意 因为参数顺序的问题 不能直接写url 和 headers 中间还有data 所以我们需要关键字传参
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')
print(content)