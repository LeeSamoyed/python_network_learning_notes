import requests
import importlib
fib = importlib.import_module('006_part_six.utils')

#### cookie
url = 'https://www.douban.com/mine'
header = {'Referer':'https://www.douban.com', 'Host':'www.douban.com', 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
cookies = fib.readCookie()
print(cookies)
response = requests.get(url, headers=header, cookies=cookies)
print('http 响应状态是：')
print(response.status_code)
print('页面请求结果：')
print(response.text)
#### session
## 登陆网站
urlLogin = 'https://passport.mtime.com/member/signinLogin'
## 表单数据
formdata = {
    'loginEmailText': '',
    'loginPasswordText': '',
    'isvcode': 'true',
    'isAutoSign':'false'
}
## 头信息拷贝过来。
header = {'Referer': 'https://passport.mtime.com/member/signin/?redirectUrl=http%3A%2F%2Fwww.mtime.com%2F', 'Host': 'passport.mtime.com',
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
session = requests.Session()
response = session.post(urlLogin, data=formdata, headers=header)
print('http 响应状态是：')
print(response.status_code)
print('登录请求结果：')
print(response.text)


#### 复用session
## 登陆网站
urlLogin = 'https://passport.mtime.com/member/signinLogin'
## 表单数据
formdata = {
    'loginEmailText': '',
    'loginPasswordText': '',
    'isvcode': 'true',
    'isAutoSign':'false'
}
## 头信息拷贝过来。
header = {'Referer': 'https://passport.mtime.com/member/signin/?redirectUrl=http%3A%2F%2Fwww.mtime.com%2F',
          'Host': 'passport.mtime.com',
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
session = requests.Session()
response = session.post(urlLogin, data=formdata, headers=header)
print('http 响应状态是：')
print(response.status_code)
print('登录请求结果：')
print(response.text)
urlOrder = 'http://my.mtime.com/account/ecommerce/orderList/'
headerOrder = {'Host': 'my.mtime.com',
                  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
responseOrder = session.get(urlOrder, headers=headerOrder)
print('页面请求响应状态是：')
print(responseOrder.status_code)
print('页面请求结果：')
print(responseOrder.text)

