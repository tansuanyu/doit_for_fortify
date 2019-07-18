#coding=utf-8

'''
作者：董某
最后更改时间：2019.07.18
'''

#此文件进行输出定制
import os
import sys
sys.path.append(r'/') 
from operation import extract

#此函数获取可定义工具状态，对不需要的功能进行关闭
def custom():
	state = input()
	if state == '0' or state == 'n' or state == 'N':
		return 0
	else :
		return 1

#此函数用于输出可选工具名称
def utilName(num):
	if num == 0:
		name = '排序功能，是否关闭：'
	elif num == 1:
		name = '去重功能，是否关闭：'
	return name

#收参，传参
def utilChoose(getname):
	utils = [] 
	utilNum = 2 #数字为工具数量
	print('默认功能已开启，可选功能输入0或N关闭')
	for num in range(0,utilNum):
		print(utilName(num))
		utils.append(custom())
	#进行提取
	extract.doExtract(getname,utils)


#这里要定义一个数组，每一位对应一个功能的开关
#utils[n](n为功能数-1)
#1开0关
#调用函数传入参数(getname,utils)
#执行功能之前进行utils判定
#在for中使用递增的数字n和switch进行判断执行步骤