import smtplib
from email.mime.text import MIMEText
from email.header import Header

## 发送者的邮箱
sender = ''
## 邮件接收，可以有多个，可以是其它邮箱地址
receivers = ['']

## 邮件普通文本内容
mailContent = ''
message = MIMEText(mailContent, '', 'utf-8')
## 发送人名称
message['From'] = Header('', 'utf-8')
## 收件人名称
message['To'] =  Header('', 'utf-8')
## 邮件标题
message['Subject'] = Header('', 'utf-8')

## 邮箱的SMTP 服务
mailHost = ''
## 用户名
mailUser = ''
## 授权码
mailPass = ''

try:
  ## 连接邮箱。465 为 SMTP 端口号，大家需要对照阅读邮箱本身的帮助说明，有可能不一样
  smtpObj = smtplib.SMTP_SSL
  ## 授权认证

  ## 发送邮件

  print("邮件发送成功")
except smtplib.SMTPException:
  print("Error: 无法发送邮件")