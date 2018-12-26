'''
如果把文件指针移动到靠后的位置，那么只要readlines方法返回的list的长度大于2，
那么虽然list第一个元素读取的行可能不完整，但后面的元素读取的行肯定都是完整的了。
而且考虑到了最后一行或多行是空行的情况。 
'''

import os

def get_last_line(inputfile):
    filesize = os.path.getsize(inputfile)
    blocksize = 1024
    dat_file = open(inputfile, 'rb')

    last_line = b""
    lines = []
    if filesize > blocksize:
        maxseekpoint = (filesize // blocksize)#这里的除法取的是floor
        maxseekpoint -= 1 
        dat_file.seek(maxseekpoint * blocksize)
        lines = dat_file.readlines()
        while((len(lines)<2) | ((len(lines)>=2)&(lines[1]==b'\r\n'))):#因为在Windows下，所以是b'\r\n'
            #如果列表长度小于2，或者虽然长度大于等于2，但第二个元素却还是空行
            #如果跳出循环，那么lines长度大于等于2，且第二个元素肯定是完整的行
            maxseekpoint -= 1 
            dat_file.seek(maxseekpoint * blocksize)
            lines = dat_file.readlines()  
    elif filesize:#文件大小不为空
        dat_file.seek(0, 0)
        lines = dat_file.readlines()
    if lines:#列表不为空
        for i in range(len(lines)-1,-1,-1):
            last_line = lines[i].strip()
            if(last_line != b''):
                break#已经找到最后一个不是空行的
    dat_file.close()
    return last_line

#该函数返回的是bytes
last = get_last_line('新建文本文档.txt')
last = last.decode()
print(last)