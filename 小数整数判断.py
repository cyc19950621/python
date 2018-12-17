n=input("输入数据:")
def check_float(n):
  #支付时，输入的金额可能是小数，也可能是整数
 s = str(n)
 if s.count('.') == 1: # 判断小数点个数
     sl = s.split('.') # 按照小数点进行分割
    left = sl[0] # 小数点前面的
    right = sl[1] # 小数点后面的

    if left.startswith('-') and left.count('-') == 1 and right.isdigit():

      lleft = left.split('-')[1] # 按照-分割，然后取负号后面的数字

      if lleft.isdigit():

        return False

    elif left.isdigit() and right.isdigit():

      # 判断是否为正小数

      return True

  elif s.isdigit():

    s = int(s)

    if s != 0:

      return True

  return False