# -*- coding: utf-8 -*-

'''
python 文件读写
'''

#定义变量
test_filename = './python_baidu.txt'

#打开文件
'''
参数说明 'r' 代表文件的访问模式为只读(r)
还有 rb r+ rb+ 等方式
'''
file_obj = open(test_filename, 'r', encoding='utf-8')

# 读取整个文件内容
all_content = file_obj.read()
#关闭文件
# file_obj.close()
print(all_content)
print('-------------')

# * 逐行读取

# In[9]:
# 打开文件
file_obj = open(test_filename, 'r', encoding='utf-8')
# 逐行读取
line1 = file_obj.readline()
print(line1)
# 继续读下一行
line2 = file_obj.readline()
print(line2)

