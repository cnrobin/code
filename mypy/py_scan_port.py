# -*- coding: utf-8 -*-
from socket import *
import re
from pip._vendor.distlib.compat import raw_input

def portscaner(host,port):                 
  try:
    s = socket(AF_INET, SOCK_STREAM)  # 实例化socket
    s.connect((host,port))        #对对应主机的对应端口发起连接
    print('主机%s的%s端口处于打开状态'%(host,port))
    s.close()     #关闭连接
    Export_Data(port)      #调用Export_Date
  except Exception as e:
    pass            #利用异常处理，对无法建立连接的端口pass掉


def ChecK_Host(host):                  #利用正侧表达式匹配host，判断是否符合IP地址的格式   并且输入不为空 
  compile_ip = re.compile(   
      '^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
  if compile_ip.match(host) and len(host)!=0:   #host符合IP地址的格式且不为空值返回True，否则返回False
    return True
  else:
    return False


def Export_Data(port):      #导出数据
  port = str(port)         #将port转换为字符串类型
  date = open('Active_Port.txt', 'a')  #在文件尾部写入数据，Active_Port.txt,若不存在就新建文件
  date.write(port+'\n')           #将port并行写入文件
  date.close()                    #不要忘了关闭文件



def main(host):                          #主模块
  if ChecK_Host(host):                 #通过ChecK_Host()函数return 的布尔值进行判断输入的IP地址是否有误
    for port in range(1,65536):         #这里可以改成1024
      portscaner(host, port)
    print('\n')
    print('已将结果导出到 Active_Port.txt')
  else:
    print('IP地址无错误，请重新输入！！！')



if __name__ == '__main__':
  print('<' * 12 + '单线程端口扫描器' + '>' * 12)
  host = input('请输入有效的目标IPv4地址：')
  main(host)

raw_input('Press Enter to exit...')       #当脚本执行完后，等待键入Enter回车才退出程序（可有可无，主要是为了封装成exe可执行文件后，执行完程序dos界面不自动退出）
