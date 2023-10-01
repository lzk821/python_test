import urllib.request
import urllib.parse

url='https://www.baidu.com/s?wd='

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}
# 依赖urllib.parse将‘迪迦’变成unicurlode编码的格式
name = urllib.parse.quote('迪迦')
#拼接
url = url+name
print(url)
# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)