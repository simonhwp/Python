# 13-3 对类进行定制，用来将浮点型值转换为金额
# class MoneyFmt(object):
#     def __init__(self, value):
#         self.value = float(value)

#     def updatemoney(self, value):
#         if value is not None:
#             self.value = float(value)
#             print('Value has been updated, the new value is: ', self.value)
#         else:
#             print('Value has not been updated.')

#     def __nonzero__(self):
#         return int(self.value)

#     def __repr__(self):
#         return repr(self.value)

#     def __str__(self):
#         strnum = str(self.value)
#         if strnum[0].isdigit():
#             return (r'$' + format(self.value, ',.2f'))
#         else:
#             return (r'-$' + format(float(strnum[1:]), ',.2f'))

    
# do = MoneyFmt(-1234567.8901)
# print(do.__str__())
# print(do.updatemoney(-1236567.890))
# print(do.__nonzero__())
# print(do.__repr__())

# 用户注册
import time

class DBMnage(object):
    def __init__(self, nm, pw):
        self.name = nm
        self.password = pw
        self.login_time = time.ctime()

    def updatepwd(self, newpwd):
        self.password = newpwd

    def creatlog(self):
        timestr = time.ctime()
        loginfo = 'The login time is' + timestr
        with open(r'C:\Users\simon\Desktop\testfor.txt', 'a') as fp:
            fp.write(loginfo)   

    def readLog():
        '登陆成功，从log文件读取上次时间戳'
        with open(r'C:\Users\simon\Desktop\testfor.txt', 'r') as logFile:
            outfile = logFile.readlines()
            if len(outfile) >= 1:
                print(outfile[-1:])

    def changePWD(username, newpwd):
        '修改用户密码'
        with  open(r'C:\Users\simon\Desktop\testfor.txt', 'w') as credentialFile:
            credentialtxt = username + ' ' + newpwd
            credentialFile.write(credentialtxt)
            print('密码已修改 ... Password updated successfully. \n')

    def adduser(self):
        pass

def main(self):
    # 从这里开始是主程序
    print('欢迎使用最简单的用户管理系统')
    print('尝试用系统中已经存在的用户名和密码登录，有三次机会')
    print('登陆成功后输入 updatepwd 命令可以修改密码，成功后退出系统')
    print('登陆成功后输入 quit 命令退出系统\n')
        
    with open(r'C:\Users\simon\Desktop\testfor.txt') as credentialFile: # 从文本文件中获取用户名和密码
        credentialInfo = credentialFile.readlines()

    usernameinDB = credentialInfo[-1].split()[0] # 这里credentialInfo[-1]是一个字符串，包括用户名和口令，空格隔开的
    passwordindm = credentialInfo[-1].split()[1]

    errorTimes = 3
    while errorTimes:
        print('请输入用户名和密码：')
        input_username = input('Username ... :  ')
        input_password = input('Password ... :  ')
        if input_username == usernameinDB and input_password == passwordindm:
            print('登陆成功  ... Login Successful')
            CurrentUser = DBMnage(input_username, input_password)
            self.readLog()
            self.creatlog(input_username)
            input_command = input('请输入你的命令, quit or updatepwd ... \n')
            if input_command == 'quit':
                del CurrentUser
                print('\n已退出系统  ... Logout successfully.')
                break
            elif input_command == 'updatepwd':
                newpwd = input('\n请输入新密码, new password ... :  ')
                CurrentUser.updatePWD(newpwd)
                self.changPWD(CurrentUser.name, CurrentUser.password)
                del CurrentUser
                print('\n已退出系统  ... Logout successfully.')
                break
            else:
                print('错误命令  ... Wrong Command')
                del CurrentUser
                print('\n已退出系统  ... Logout successfully.')
                break
        else:
            print('用户名或口令错误  ... Wrong Username or Password.\n')
            errorTimes -= 1
            if 0 >= errorTimes: 
                print('已退出系统  ... Logout successfully.')

if __name__ == "__main__":
    main()
            


