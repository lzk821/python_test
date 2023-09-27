import urllib.request

url = 'http://www.baidu.com'

response = urllib.request.urlopen(url)

# 一个类型和六个方法
# response是HTTPResponse的类型

# 按照字节一个一个去读
# content = response.read()
# 返回多少个字节
# content = response.read(5)
# 读取一行
# content = response.readline()
# content = response.readlines()
# print(content)
# 返回状态码，如果是200那么就说明我们的逻辑没有错
# print(response.getcode())
# 返回的是url地址
# print(response.geturl())
# 获取的是一个状态信息
print(response.getheaders())

# 一个类型 HTTPResponse
# 六个方法 read readline readlines getcode geturl getheaders