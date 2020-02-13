def readCookie():
  # 打开保存的cookies内容文件
  f = open('cookie.txt', 'r')
  # 初始化cookies字典变量
  cookies = {}
  # 按照分号 ; 进行划分读取
  for line in f.read().split(';'):
    # 其设置为1就会把字符串拆分成2份
    name, value = line.strip().split('=', 1)
    print(name)
    print(value)
    # 为字典cookies添加内容
    cookies[name] = value

  return cookies