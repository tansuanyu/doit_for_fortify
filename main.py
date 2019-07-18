#coding=utf-8

'''
作者：董某
最后更改时间：2019.07.18
'''
import os
import sys
sys.path.append(r'./') 
from operation import choose

#此文件为主函数
#进包含文件入口，获取输入文件，转到操作选择选项

xmlname = input()
print(xmlname)
#将文件名传入选择目录，进行输出定制
choose.utilChoose(xmlname)

print('测试结束')