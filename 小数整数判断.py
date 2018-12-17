def is_float(str):
    if str.count('.') == 1: #小数有且仅有一个小数点
        left = str.split('.')[0]  #小数点左边（整数位，可为正或负）
        right = str.split('.')[1]  #小数点右边（小数位，一定为正）
        lright = '' #取整数位的绝对值（排除掉负号）
        if str.count('-') == 1 and str[0] == '-': #如果整数位为负，则第一个元素一定是负号
            lright = left.split('-')[1]
        elif str.count('-') == 0:
            lright = left
        else:
            print('%s 不是小数'%str)
        if right.isdigit() and lright.isdigit(): #判断整数位的绝对值和小数位是否全部为数字
            print('%s 是小数'%str)
        else:
            print('%s 不是小数'%str)
    else:
        print('%s 不是小数'%str)
n=input(" 输入数据: ")
print(is_float(n))