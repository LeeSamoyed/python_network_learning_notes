import requests
#### 响应状态和内容
response = requests.get('https://www.baidu.com/')
print('http 响应状态是：' + str(response.status_code))
print('API调用结果：' + response.text)


#### get方法
params = {
  'word' : 'teacher',
  'submit' : '查询'
}
response = requests.get('http://dict-co.iciba.com/search.php',params = params)
print('http 响应状态是：' + str(response.status_code))
print('API调用结果：' + response.text)


#### 响应类型
response = requests.get('https://style.youkeda.com/img/ham/course/py2/douban2.png')
print('http 响应状态是：')
print(str(response.status_code))
print('API调用结果的数据类型：')
print(type(response.content))


#### json格式
response = requests.get('https://api.apiopen.top/searchMusic', params = {'name' : '左手指月'})
print('http 响应状态是：')
print(response.status_code)
print('API调用结果：')
print(response.json())
print('API调用结果的数据类型：' + str(type(response.content)))


#### 解析字典 打印json中message值
param = {'name': '左手指月'}
response = requests.get('https://api.apiopen.top/searchMusic', params=param)
print('http 响应状态是：')
print(response.status_code)
print('API调用结果：')
print(response.json())
print('API调用结果的数据类型：')
print(type(response.json()))
print('API调用结果的 message 值：' + str(response.json()['message']))


#### 解析列表
param = {'name': '左手指月'}
response = requests.get('https://api.apiopen.top/searchMusic', params=param)
print('http 响应状态是：')
print(response.status_code)
print('API调用结果：')
print(response.json())
print('API调用结果的数据类型：')
print(type(response.json()))
print('API调用结果的 message 值：')
print(response.json()['message'])
print('API调用结果的 第三首歌的标题：' + str(response.json()['result'][2]['title']))
print('API调用结果的 第三首歌的演唱者：' + str(response.json()['result'][2]['author']))