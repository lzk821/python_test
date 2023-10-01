import urllib.request
import urllib.parse

base_url='https://www.baidu.com/s?'

# 创建一个data字典，将多个参数放进去
data = {
    'wd':'迪迦',
    'sex':'男'
}
# urlencode应用场景：多个参数的时候
new_data = urllib.parse.urlencode(data)
# 拼接
url = base_url+new_data
# 获取agent
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)