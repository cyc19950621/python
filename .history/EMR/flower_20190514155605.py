import os
import time
from random import randint
 
 
for i in range(1, 35):  # 打印抬头
    print('')
 
heartStars = [2,4,8,10,14,20,26,28,40,44,52,60,64,75]  # *的位置
heartBreakLines = [13, 27, 41, 55, 69, 76]  # 空格的位置
flowerBreakLines = [7, 15, 23, 31, 39, 46]#玫瑰的空列位置
 
def addSpaces(a):#添加空列
    count = a
    while count > 0:
        print(' ', end='')
        count -= 1
 
 
def newLineWithSleep():#添加空行
    time.sleep(0.3)
    print('\n', end='')
 
 
play = 0
while play == 0:
    Left_Spaces = randint(8, 80)
    addSpaces(Left_Spaces)
 
    for i in range(0, 77):#比心的形状
        if i in heartBreakLines:
            newLineWithSleep()
            addSpaces(Left_Spaces)
        elif i in heartStars:
            print('*', end='')
        elif i in (32, 35):
            print('球', end='')
        elif i == 34:
            print('', end='')
        else:
            print(' ', end='')
 
    newLineWithSleep()
    addSpaces(randint(12, 80))
    print("         520快乐 !           ", end='')
    newLineWithSleep()
    newLineWithSleep()
 
 
 
    Left_Spaces = randint(12, 80)
    addSpaces(Left_Spaces)
    for i in range(0, 47):#献花
        if i in flowerBreakLines:
            newLineWithSleep()
            addSpaces(Left_Spaces)
        elif i in (2, 8, 12, 18):
            print('{', end='')
        elif i in (3, 9, 13, 19):
            print('_', end='')
        elif i in (4, 10, 14, 20):
            print('}', end='')
        elif i in (27, 35, 43):
            print('|', end='')
        elif i in (34, 44):
            print('~', end='')
        elif i == 11:
            print('o', end='')
        else:
            print(' ', end='')
 
    print('\n', end='') 