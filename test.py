
# fp = open(r'C:\Users\simon\Desktop\testfor.txt')
# i = 0
# for eachline in fp:
#     # if -1 >= eachline.find('#'):
#     #     print(eachline) 
#     i += 1
#     if 4 == i:
#         break   
#     print(eachline, end='')    
# fp.close()

f = open(r'C:\Users\simon\Desktop\testfor.txt')
for i in range(5):
    print(f.readline().strip())
 
