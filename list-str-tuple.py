# 输入一串数字，并从大到小排序
# num = input('Enter New num:')

# new_num = list(map(int, num.strip().split()))
# print(new_num)
# # new_num.sorted(reverse=False)
# print(sorted(new_num, reverse=True))
# print(new_num.sort(reverse=True))

# 测试得分放到一个列表中，并求出平均值
# num = input('Enter New num:')
# new_num = list(map(int, num.strip().split()))
# total = 0
# for i in range(len(new_num)):
#     total += new_num[i]
# avg_num = total / len(new_num)
# print('The avg is ', avg_num)

# 每次向前向后都显示一个字符串的一个字符
# s1 = input('Enter New string:')

# for i in range(len(s1)):
#     print(s1[i])  #从头开始输出字符
# s2 = s1[::-1]
# for j in range(len(s2)):
#     print(s2[j])  #从尾开始输出字符

# 通过扫描来判断两个字符串是否匹配

# s1, s2 = input('请输入两个字符串，以空格相隔：').split()
# if (len(s1) != len(s2)):
#     print('两个字符串不相符')
# else:
#     tag = True
#     for i in range(len(s1)):
#         if s1[i] != s2[i]:
#             tag = False
#             break
#     if (tag):
#         print('两个字符串相符')
#     else:
#         print('两个字符串不相符')

# 接受一个字符串，去年它的前面和后面的空格
# s1 = input('输入一个字符串：')

# start_index = 0
# end_index = len(s1)

# if ' ' == s1[0]:
#     start_index = 1

# if ' ' == s1[end_index - 1]:
#     end_index -= 1
# print(s1[start_index:end_index])
# print(len(s1[start_index:end_index]), len(s1), start_index, end_index)

# 给出一个整型值，返回代表该值的英文
# num = input('请输入一个整型值：')
# inum = int(num)
# if 0 > inum:
#     print('数值不能为负。')
# if 1000 < inum:
#     print('数值不能超过1000。')
# dnum = [
#     'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
#     'nine'
# ]
# restr = ''
# istrlen = len(num)
# if 1 == istrlen:
#     restr = dnum[int(num)]
#     print(restr)
# else:
#     for i in range(istrlen):
#         temp = dnum[int(num[i])]
#         if i != istrlen - 1:
#             restr += temp + '-'
#         else:
#             restr += temp

#     print(restr)

# 字符串大小反转
# s1 = input('请输入一个字符串：')
# s1_list = list(s1)
# ls1 = len(s1)
# re_s1 = ''
# print(s1_list)
# for i in range(ls1):
#     temp = ''
#     if True == s1_list[i].islower():
#         temp = s1_list[i].upper()
#     elif True == s1_list[i].isupper():
#         temp = s1_list[i].lower()
#     else:
#         temp = s1_list[i]
#     re_s1 += temp

# print(re_s1)

# 改错
# num_str = input('Enter a number:')
# num_num = int(num_str)
# # fac_list = range(1, num_num + 1) 无法直接range赋值List
# fac_list = list(range(1, num_num + 1))
# print('befor list:', fac_list)
# i = 0
# while i < len(fac_list):
#     if num_num % fac_list[i] == 0:
#         del fac_list[i]
#     i = i + 1
# print('after list:', fac_list)

# find(), index()
# print(list(range(10, 0, -1)))

# 随机数，石头、剪刀、布
import random
mychoice = input('请输入石头、剪刀、布中的一样：')
choice_list = ['石头', '剪刀', '布']
myc_index = choice_list.index(mychoice)
computerchoice = random.choice(choice_list)
comp_index = choice_list.index(computerchoice)
print(mychoice, computerchoice, myc_index, comp_index)
if myc_index == comp_index:
    print('平局')
elif (myc_index < comp_index) or (myc_index == 2 and comp_index == 0):
    print('你赢了')
else:
    print('计算机赢了')
