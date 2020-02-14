import requests
import xlrd

#### 下载文件
url = 'https://style.youkeda.com/img/ham/course/py2/h.txt'
response = requests.get(url)
fo = open('h.txt','w')
fo.write(response.text)
fo.close()
fo = open('h.txt','r')
lines = fo.read()
print(lines)

url = 'https://style.youkeda.com/img/ham/course/py2/xzq_201907.xlsx'
response = requests.get(url)
fo = open('xzq_201907.xlsx','wb')
fo.write(response.content)
fo.close()
print('下载成功！')

#### 下载图片
#### 和上面调用二进制一样
url = 'http://photo.yupoo.com/vibius/GkRSowXr/medish.jpg'
headers = {'Referer': 'http://photo.yupoo.com/' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
response = requests.get(url,headers=headers)
fo = open('xzq_201907.jpg','wb')
fo.write(response.content)
fo.close()
print('下载成功！')

#### 解析excel
## 必须先打开 excel 文件
x1 = xlrd.open_workbook('xzq_201907.xlsx')
x1 = x1.sheet_by_name('Sheet1')
rows = x1.nrows
cols = x1.ncols
print(rows)
## sheet_by_index()方法获取到 sheet 对象，参数是位置坐标
for i in range(0,rows-1):
    print(str(x1.cell(i,0).value) + ' ' + str(x1.cell(i,1).value) + ' ' + str(x1.cell(i,2).value) + ' ' + str(x1.cell(i,3).value)  +
          ' ' + str(x1.cell(i,4).value) + ' ' + str(x1.cell(i,5).value))
