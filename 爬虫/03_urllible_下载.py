import urllib.request

# 下载网页
# url_page = 'https://www.liash.link/'
#
# url代表的是下载的路径 filename文件的名字
# 在python中 可以写变量的名字 也可以直接写值
# urllib.request.urlretrieve(url_page,'baidu.html')
# 下载图片
url_img = 'https://img0.baidu.com/it/u=3751856574,4049408926&fm=253&app=138&size=w931&n=0&f=JPEG&fmt=auto?sec=1695920400&t=d38b2ba787a12ed81c47d40541b0a3db'
urllib.request.urlretrieve(url=url_img,filename='dijia.jpg')
# 下载视频

url_video = 'https://vd4.bdstatic.com/mda-mjue2n3ynvfimfc4/sc/cae_h264_nowatermark/1635502870460266194/mda-mjue2n3ynvfimfc4.mp4?v_from_s=hkapp-haokan-suzhou&auth_key=1695828471-0-0-3055be668497d0507a00c7e0a8dc7495&bcevod_channel=searchbox_feed&pd=1&cr=2&cd=0&pt=3&logid=1671052000&vid=9984819462392257978&klogid=1671052000&abtest=112751_3"'
urllib.request.urlretrieve(url_video,'1.mp4')