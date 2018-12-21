# 两个字典合并
d1 = {'apple': 12, 'banana': 2}
d2 = {'orange': 2, 'banana': 4}
# d3 = dict(d1, **d2)
'''
z = d1.copy()
z.update(d2)
'''
d3 = {**d1, **d2}  #python3.5 PEP448 新的使用方法
print(d3)

# 创建字典，并根据字母顺序输出键值
d1 = {'apple': 14, 'oragne': 14, 'banana': 5}
print(sorted(d1.keys()))
print([(i, d1[i]) for i in sorted(d1.keys())])

# 将两个长度相同的列表合并成一个字典
l1 = [1, 2, 3, 4, 5]
l2 = ['a', 'b', 'c', 'd', 'e']
d1 = dict(zip(l1, l2))
print(d1)

# 翻译
srcstr = 'abc'
ssrc = set(srcstr)
dststr = 'mno'
sdst = set(dststr)
string = 'abcdef'
sstr = set(string)
difstr = sstr - ssrc
sstr.difference_update(ssrc)
print(sstr)
_newstr = sdst | difstr
print(_newstr)

# 加密, 用输入的字符的第13位数字来替代
def string_to_rot13(inpstr):
    result = []
    n = 13
    newinput = list(inpstr)
    lstr = len(newinput)  
    for i in range(lstr):
        if newinput[i].isupper():
            if ord(newinput[i]) < 91-n:
                c = chr(ord(newinput[i]) + n)
                result.append(c)
            else:
                c = chr(ord(newinput[i]) + n - 26)
                result.append(c)
        elif newinput[i].islower():
            if ord(newinput[i]) < 123-n:
                c = chr(ord(newinput[i]) + n)
                result.append(c)
            else:
                c = chr(ord(newinput[i]) + n - 26)
                result.append(c)
        else:
            c = newinput[i]
            result.append(c)
    return result

youstr = input('please enter sting to rot13:')
print('Your string to en was:', youstr)
newstr = list(youstr.split())
lstr = len(newstr)
outstr = []
for i in range(lstr):
    newlstr = string_to_rot13(newstr[i])
    outstr.append(''.join(newlstr))
    print(outstr)
print('The rot13 string is:', ' '.join(outstr))