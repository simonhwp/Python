# 13-3 对类进行定制，用来将浮点型值转换为金额
class MoneyFmt(object):
    def __init__(self, value):
        self.value = value

    def updatemoney(self, value):
        if value is not None:
            self.value = float(value)
            print('Value has been updated, the new value is: ', self.value)
        else:
            print('Value has not been updated.')

    def __nonzero__(self):
        return int(self.value)

    def __repr__(self):
        return repr(self.value)

    def __str__(self):
        strnum = str(self.value)
        if strnum[0].isdigit():
            return (r'$' + format(self.value, ',.2f'))
        else:
            return (r'-$' + format(float(strnum[1:]), ',.2f'))

    
do = MoneyFmt(-1234567.8901)
print(do.__str__())
print(do.updatemoney(-1236567.890))
print(do.__nonzero__())
print(do.__repr__())

