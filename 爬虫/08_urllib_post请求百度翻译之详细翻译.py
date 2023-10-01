import urllib.request
import urllib.parse
url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
'Accept':'*/*',
# 'Accept-Encoding':'gzip, deflate, br, zstd',
'Accept-Language':'zh-CN,zh;q=0.9',
# 'Acs-Token':'1696096808817_1696147401532_k/G3E4YpgNi8pTjK30CQ4AJvZ2wzEExlQiez4aJxXaG7ulKFD5BKpAahdQ6OD2Dyemm93nQXHUkXzPkHp5lL3vBztvZYwa3qtBlOmO4RnmxEfSKXClznxgGUGxoSF2nCEocLQTTNFLmxHrW4mr+LtVVSWSboOVl4lgzR+k9tg+2TccDZWPLfDXOuXc+h9GuQL9/U7UFOrZRMku+1BiO+EHN6ouJhQACFWgG77TNK+dDilnqETbpoIFd4YuTkskFdVT0W4yUXQUoq1fISH2p+MKeTuUGUUo6eI9vIxtdz5y0uh7Jtwg/eOsioCsmIRpR+Hm4olrbBdP3TYDZx8pMi2Rbm6F8HXe4pDnEX2S1DcI6RLjTrydG1DcfTcKsfLgzhaBGbnAHPIGFaA7bVI0s+r/Y9ULIX3fAKI2XftSxgZJ77PKPR31CFfZQNvmJm5MbhKHrQ90c1jpD8ebudYeMe9ytKDXrw1+7ZyUqSdXp0m+ie4QrdN0SwO8NHKkSP2XH1',
'Connection':'keep-alive',
'Content-Length':'153',
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie':'BIDUPSID=7C6EA9B1B09990F355E6AC308ADF794B; PSTM=1695735466; BAIDUID=7C6EA9B1B09990F33A484FECB6E3D2B7:FG=1; BAIDUID_BFESS=7C6EA9B1B09990F33A484FECB6E3D2B7:FG=1; ZFY=:BBlvgrmwsE03Uwn3eGFJ7ZwQv1GTbTembhOH7RwyYF0:C; BA_HECTOR=ag0h812h05252l2k0gal852c1ihfuh21p; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[Zh1eoDf3ZW3]=mk3SLVN4HKm; delPer=0; PSINO=6; ZD_ENTRY=baidu; H_PS_PSSID=39220_39354_39390_39348_39407_39097_39438_39358_39451_39465_39233_39403_26350_39430; APPGUIDE_10_6_5=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1696145381; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1696147009',
'Host':'fanyi.baidu.com',
'Origin':'https://fanyi.baidu.com',
'Referer':'https://fanyi.baidu.com/?aldtype=16047',
'Sec-Ch-Ua':'"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
'Sec-Ch-Ua-Mobile':'?0',
'Sec-Ch-Ua-Platform':'"Windows"',
'Sec-Fetch-Dest':'empty',
'Sec-Fetch-Mode':'cors',
'Sec-Fetch-Site':'same-origin',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
'X-Requested-With':'XMLHttpRequest'
}

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'spider',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '63766.268839',
    'token': 'bcedeea09a4bfa817fc0da0bbc723557',
    'domain': 'common',
    'ts': '1696147401510'
}
#post请求的参数，必须要进行编码 并且要调用encode方法
data = urllib.parse.urlencode(data).encode('utf-8')
# 请求对象的定制
request = urllib.request.Request(url=url,data=data,headers=headers)
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
# 获取响应的数据
content = response.read().decode('utf-8')

import json
obj = json.loads(content)
print(obj)