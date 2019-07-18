#coding=utf-8

'''
作者：董某
最后更改时间：2019.07.18
'''

#此文件进行具体操作
import os

def theSort(s):
	new_s = sorted(s)
	return new_s

def theOnly(s):
	new_s = []
	for line in s:
		if line not in new_s:
			new_s.append(line)
	return new_s

def basics(file,filename,utilState):

	theFilePath = []

	for line in open(filename + '.xml',encoding = "utf-8"):
		#判断是否是显示漏洞数量标签
		if (" <GroupingSection count=" in line):
			if len(theFilePath) :
				if utilState[0] == 1:
					theFilePath = theSort(theFilePath)
				if utilState[1] == 1:
					theFilePath = theOnly(theFilePath)
				for line in theFilePath:
					file.write(line)
			theFilePath = []
			line = ''.join(line)
			file.write("漏洞数量为：" + line[44:-3] + "\r")
	
		#判断是否是显示漏洞名称的标签
		if ("<groupTitle>" in line):
			line = ''.join(line)
			file.write("漏洞名称为：" + line[36:-14] + "\r")

		#判断是否是显示漏洞位置和行数的标签
		if ("<FilePath>" in line):
			line = ''.join(line)
			filePath =line[10:-12] + " 第"
		if ("<LineStart>" in line):
			line = ''.join(line)
			linePath = line[11:-13] + "行 \r"
			theFilePath.append(filePath + linePath)


def doExtract(filename,utilState):
	print('生成的文件名：')
	outputName = input()
	file = open(outputName + '.txt','w+') 

	basics(file,filename,utilState)