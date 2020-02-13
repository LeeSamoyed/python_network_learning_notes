import requests

url = 'http://www.weather.com.cn/data/sk/101040200.html'

response = requests.get(url)
response.encoding = 'utf-8'
#print(response.json())
#print(response.json()['weatherinfo'])
print(str(response.json()['weatherinfo']['city']) + '风向' + str(response.json()['weatherinfo']['WD']))
#response.encoding('utf-8')
#print(response.text)


#### 发送邮件