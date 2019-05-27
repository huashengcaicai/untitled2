import setuptools

# 字符串首字母大写
'this is apple'.capitalize()
# 子串在母串的个数
'abccdd'.count()
# 是否已子串结尾
'aabddddon'.endswith('on')
# 是否已子串开始
'lllhhauus'.startswith()
# 把tab的字符替换成空格
'hah\dhdh'.expandtabs()
# 子串（子串[开始位置][]）,当没有的时候返回-1 rfind,没有返回-1
'abcd'.find('c')
#
'abcccd'.index('b')
# format,使用{}代替args参数
'my name is {0},age is{1}'.format('张三' ,28)

# format.map() 用映射关系格式化{
'my name is {name},age is{age}'.format_map({'name':'张三','age':28})
# isalnum 判断是不是数字或字母，返回true
'11233'.isalnum()
# isalnum 判断是否是字母，是返回true
'aaad'.isalpha()
# 判断是全部是数字，返回true
'1222'.isdecimal()
# 是否全是小写，返回true
'abb'.islower()
# 是否全是大写
'DDD'.isupper()
# 是否全是空格
'    '.isspace()

#
'abc'.ljust()
