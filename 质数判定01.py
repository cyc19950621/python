#输入数据
n = input('输入大于1的整数:')
#if判定是否为大于一的整数
if type(int(n)) == int and int(n) >1:
#判定质数
    for i in range(2,int(n)):
        if (int(n) % i)==0:
            print(n,"不是质数")
            break
        else:
            print(n,"是质数")
else:
        print("请输入大于1的整数")
#当输入2 时无对应值,且输入带小数点的整数无法正确识别
