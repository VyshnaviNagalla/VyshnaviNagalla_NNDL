# -*- coding: utf-8 -*-
"""Assignment_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YJoE1up7Gb0FU3hFaIMTIMn7DH4tcOT8
"""

str = input()
lenth = len(str)
l = len(str)-1
Remove_last = str[:l - 2]
Remove_last = Remove_last+str[lenth-1]
print(Remove_last[::-1])
num1, num2 = int(input()), int(input())
print('sum of num1 and num2 =')
print (num1+num2)
print('sub of num1 and num2 =')
print(num1-num2)
print('mul of num1 and num2 =')
print(num1*num2)
print('div of num1 and num2 =')
print(num1/num2)

str = "I love playing with python"
print(str.replace("python", "pythons"))

x = int(input("What is the exam score?"))
if x >= 90:
    print('A')
elif x >= 80:
    print('B')
elif x >= 70:
    print('C')
elif x >= 60:
    print('D')
elif x<60:
    print('F')