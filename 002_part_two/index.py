import requests
#### get获取网址返回的结果
result = requests.get('https://api.apiopen.top/musicRankings')
print('API调用结果：')
print(result.text)


#### get带参数
result = requests.get('https://api.apiopen.top/getJoke' , params = {'page' : '1' , 'count' : '2' , 'type' : 'video'})
print('API调用结果：')
print(result.text)


#### post
result = requests.post(
    'http://tcc.taobao.com/cc/json/mobile_tel_segment.htm',
    #data也是一个字典
    data={
        'tel': '15195955126'
        }
    )
print('API调用结果：')
print(result.text)


#### json数据格式
params = {'num': '20190101', 'name': '王陆', 'gender' : '男', 'faculty' : '灵剑派', 'discipline' : '无相剑骨', 'class' : '一年一班', 'startYear' : '2019'}
result=requests.post('https://jsonplaceholder.typicode.com/posts', json=params)
print('API调用结果：')
print(result.text)