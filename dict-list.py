# 两个字典合并
# d1 = {'apple': 12, 'banana': 2}
# d2 = {'orange': 2, 'banana': 4}
# # d3 = dict(d1, **d2)
# '''
# z = d1.copy()
# z.update(d2)
# '''
# d3 = {**d1, **d2}  #python3.5 PEP448 新的使用方法
# print(d3)

# 创建字典，并根据字母顺序输出键值
# d1 = {'apple': 14, 'oragne': 14, 'banana': 5}
# print(sorted(d1.keys()))
# print([(i, d1[i]) for i in sorted(d1.keys())])

# 将两个长度相同的列表合并成一个字典
l1 = [1, 2, 3, 4, 5]
l2 = ['a', 'b', 'c', 'd', 'e']
d1 = dict(zip(l1, l2))
print(d1)