import requests

#### 判断浏览器类型
url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=热门&page_limit=5&page_start=0'
response = requests.get(url)
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'})
print('API调用结果：')
print(str(response.json()))


#### 打印每个电影名
print('热门电影分别是：')
for key in response.json()['subjects']:
    print(key['title'])

#### 防盗链
url = 'http://sug.qianqian.com/info/suggestion?format=json&version=2&from=0&word=刺心&third_type=0&client_type=0'
headers = {'Referer': 'http://photo.yupoo.com/'}
response = requests.get(url,headers=headers)
print('http 响应状态码是：')
print(response.status_code)
print('http 响应的 URL 是：')
print(response.url)

####
url = 'http://sug.qianqian.com/info/suggestion?format=json&version=2&from=0&word=刺心&third_type=0&client_type=0'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
           'Referer': 'http://sug.qianqian.com/'}
response = requests.get(url,headers=headers)
print('http 响应状态是：')
print(response.status_code)
print(str(response.json()))
print('歌曲名字：')
for key in response.json()['data']['song']:
    print(key['songname'] + ' - ' + key['artistname'])