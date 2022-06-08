# for i in range(1,11):
#     print(i)
#

# s = 'suneel'
# s[0]
# print(s[0])


# x = 4
# x = 4.3
# x = 'suneel'
# x = 3
# print(x)


# x = 3
# y = 'suneel'
#
# print(type(x))
# print(type(y))


# x, y, z = 'banana','apple','orange'
# print(z)
# print(y)
# print(x)

# fruits = ['banana','apple','orange']
# x,y,z = fruits
# print(x)


# lst = ['suneel', 5, 8, 'ravi', True]
# lst.insert(1,10)
# print(lst)
# lst.append('hari')
# print(lst)
# del lst[4]
# print(lst)
# lst.extend([1, 'malli'])
# print(lst)
# lst[4]='aaa'
# print(lst)
# lst.remove('malli')
# print(lst)
# lst.pop(0)
# print(lst)


# x = [5, 6, 8, 2, 7, 10, 20, 4]
# x.reverse()
# print(x)
# x.sort()
# print(x)
# x.sort(reverse=True)
# print(x)
# print(min(x))
# print(max(x))
# print(x)

#
# x = int(input('enter a value'))
# z = x**0.5
# print('square root of', x, 'is', z)


# import math
# x = int(input('enter a value :'))
# z = math.sqrt(x)
# print('square root of', x, 'is', z )


# x = (4, 5, 9, 7, 6, 7)
# print(x[0])
# print(x.count(7))


# di = {'a': 5, 'b': 9, 'c': 6, 'd': 7}
# print(di)
# di['a'] = 10
# print(di)
# print(di['b'])

# for i, j in di.items():
#     print(i,',',j)
#
# for i in di.keys():
#     print(i,di[i])

# di = {'a': 5, 'b': 9, 'c': 6, 'd': 7}
# x = {'e':30}
# di.update(x)
# print(di)


# di = {'a': 5, 'b': 9, 'c': 6, 6: 7}
# del di['a']
# di.pop(6)
# print(di)


# l = [4, 9, 8, 6, 2, 7, 10, 20]
# for i in l:
#     print(i)


# z = [4, 9, 8, 6, 2, 7, 10, 20]
# l = len(z)
# i = 0
# while i<l:
#     print(z[i])
#     i+=1


# s = 'suneel is a learner'
# print(s[::-1])
# s1 = ""
# for i in s:
#     s1 = i+s1
# print(s1)


# i = 0
# while i<6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)
#
# i = 0
# while i<6:
#     print(i)
#     if i == 3:
#         break
#     i += 1


# x = ['1','2','3','4','5']
# y = ['a','b','c','e','f']
# for i in range(len(x)):
#     print(x[i] + y[i])
#
# x = [1,2,3,4,5,6,0,-1,-6,10]
# for i in (x):
#     if i<=0:
#         x.remove(i)
# print(x)


# x = [1,2,3,4,5,6,0,-1,-6,10]
# y = [i for i in x if i>0]
# print(y)


# for i in range(1,11,2):
#     print(i)


# x = ['orange', 'banana']
# y = ['suneel', 'anil']
# for i in (x):
#     for j in y:
#         print(i,j)


# def myfunction(food):
#     for x in food:
#         print(x)
# fruits = ['apple','banana','apple','pineapple']
# myfunction(fruits)


# n = input('enter :')
# l = len(n)
# for i in range(len(n)):
#     for j in range(i+1):
#         print(n[j],end="")
#     print()


# n = int(input('enter a value'))
# d = n
# e = n
# for i in range(1,n+1):
#     for j in range(1,n*2):
#         if j<=d:
#             print(j,end="")
#         elif j>=e:
#             print(n*2-j,end="")
#         else:
#             print(" ",end="")
#     print()
#     d-=1
#     e+=1


# def myfunction():
#     print("hi now iam in revision")
# myfunction()


# def myfunction(name):
#     print(name + " is good boy")
#
#
# myfunction("suneel")
# myfunction("srinu")


# def myfunction(fname,lname):
#     print(fname,lname)
# myfunction("suneel","ulasa")


# def myfunction(*kid):
#     print(kid[2],"is the last kid")
# myfunction("suman","suneel","anil")


# def myfunction(child1,child2,child3):
#     print(child3,"is the last kid")
# myfunction(child1="suman",child2="suneel",child3="anil")


# def myfunction(**kid):
#     print(kid["lname"],"is the last name")
# myfunction(fname="suneel",lname="ulasa")


# def myfunction(country="india"):
#     print("iam from ",country)
# myfunction("america")
# myfunction("newyork")
# myfunction("usa")
# myfunction()


# def myfunction(x):
#     c=5*x
#     return c
# print(myfunction(3))
# print(myfunction(5))


# def fun1(a):
#     print("a:",a)
# a=33
# print('locala:',a)
# a=100
# fun1(a)
# print('aoutside fun1:',a)


# def foo(x,y):
#     global a
# a=42
# x,y=y,x
# b=33
# b=17
# c=100
# print(a,b,x,y)
# a,b,x,y=1,15,3,4
# foo(17,4)
# print(a,b,x,y)


#
# def f1(x=[]):
#     x.append(1)
#     return x
# print(f1())
# print(f1())


# s = input("enter")
# upc = 0
# lwc = 0
# for i in s:
#     if i.isupper():
#         upc +=1
#     elif i.islower():
#         lwc +=1
#     else:
#         pass
# print("UPPERCASE:",upc,"LOWERCASE",lwc)


# import datetime
# a = datetime.datetime.now()
# y = a.strftime("%y/%m/%d")
# print(type(y))


# import datetime
# strng = '2022/04/27'
# intg = datetime.datetime.strptime(strng,"%Y/%m/%d")
# print("type of the date :", intg)

#
# import time
# time1 = 5698
# y = time.strftime("%H:%m:%S",time.gmtime(time1))
# print(y)
#


# t1 = (1,2,3)
# t2 = (3,4,5)
# print(dict(zip(t1,t2)))


# l = [1,5,4,87,3,65,48,96,20,0]
#
# largest = l[0]
# scnd_largest = l[0]
#
# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
#     elif l[i] > scnd_largest and l[i] != largest:
#         scnd_largest = l[i]
# print(scnd_largest)
#
# l.sort()
# print(l)


# s = "prudhvinayaka"
# v = ""
# for i in s:
#     v = v+i
#     print(v)


# a = "suneel"
# b = "suneel"
# print(a is b)
#
#
# a = [1,2,3,4,5]
# b = [1,2,3,4,5]
# print(a is b)

import copy

# l1 = [1,2,[3,4],5]
# l2 = l1.copy()
# print(l1)
# l2[2]=10
# print(l2)
# print(l1)

# for i in range(len(l1)):
#     print(l1[i], end="")
#
# for i in range(len(l2)):
#     print(l2[i], end="")
# for i in range(len(l1)):
#     print(l1[i], end="")


# def convert(tup, di):
#     for a,b in tup:
#         di.setdefault(a,[]).append(b)
#     return di
# tup1 = {("s",10), ("u",5) ,("n",6),("e",6 )}
# dic = {}
# print(convert(tup1,dic))
#
# t = (5,4,7,8,13,3,5,4,58)
# l = list(t)
# l.sort()
# print(tuple(l))

#
# year = 2004
# if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
#     print("it is a leap year")
# else:
#     print("it is not is leap year")


# l = [1,2,3,4,5,6,7,8,9]
# for i in range(len(l)):
#     print(l[i])


#
# di = {"a":10, "b":20, "c":50, "d":45, "e":80}
#
# print(di["a"])
# print(di)


# import datetime
# from datetime import timedelta
# beg_date = datetime.datetime.now()
# end_date = beg_date + timedelta(days= 5)
# print("starting date", beg_date)
# print("ending date", end_date)


# import datetime
# from datetime import datetime
# import time
# s = '10-05-22 04:16:55'
# date = datetime.strptime(s ,"%d-%m-%y %H:%M:%S")
# print(date)

# from datetime import datetime
# date = datetime.now()
# print(date)
# s = datetime.strftime(date, ("%Y/%m/%d %H:%M:%S"))
# print(s)
# print(type(s))


# l = [1,2,3,4,5,6]
# largest = l[0]
# scnd_largest = l[0]
# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
#     elif l[i] > scnd_largest and l[i] != largest:
#         scnd_largest = l[i]
# print(scnd_largest)

# li = [1,2,3,4,5,6,7,8,9]
# largest = li[0]
# scndlargest = li[0]
# for i in range(len(li)):
#     if li[i] > largest:
#         largest = li[i]
# for i in range(len(li)):
#     if li[i] > scndlargest and li[i] != largest:
#         scndlargest = li[i]
# print(scndlargest)


# def findLargest(arr):
#     secondLargest = arr[0]
#     largest = arr[0]
#     for i in range(len(arr)):
#         if arr[i] > largest:
#             largest = arr[i]
#
#     for i in range(len(arr)):
#         if arr[i] > secondLargest and arr[i] != largest:
#             secondLargest = arr[i]
#
#     return secondLargest
#
#
# print(findLargest([1,2,3,4,5,6,7,8,9]))

# n = 144
# if (5*n**2-4) == n or (5*n**2+4) == n:
#     print("it is a fibonacci")
# else:
#     print("it is not a fibonacci")


# n = 145
# n1 = str(n)
# sum = 0
# f = 1
# for i in n1:
#     for j in range(1,int(i)+1):
#         if j < 0:
#             print("it is not a integer")
#         elif j <=0:
#             print("factorial of 0 is :1")
#         else:
#             f = f*j
#             sum +=f
#         print(f)
#         print(sum)
# if sum == n:
#     print("it is strong number")
# else:
#     print("it is not a strong number")
#


# n = 45
# n1 = str(n)
# sum = 0
# for i in n1:
#     f = 1
#     for i in range(1, int(n1[i]) + 1):
#         f = f * i
#     print(f)


# s = input("enter string:")
# if s[::-1] == s:
#     print("the given string:",s,"is palindrom ")
# else:
#     print("the given string:",s,"is not a pralindrom ")


# l = [5, 10, 15, 20, 25, 30, 30]
# l1 = len(l)
# for i in range(l1):
#     print(l[i-1] + l[i])


# l = [1,2,3,4,5,6,7]
# l.remove(3)
# print(l)


# numbers = [5, 10, 15, 20, 25, 30, 30]
#
# for i in range(len(numbers)):
#     # if i == 0:
#         # print(numbers[i])
#     # else:
#         print(numbers[i - 1] + numbers[i])


# for i in range(1,11):
#     print(i-1 + i)

# numbers = [5, 10, 15, 20, 25, 30, 30]
# for i in range(len(numbers)):
#     if i == 0:
#         print(numbers[i])
#     else:
#         print(numbers[i-1] + numbers[i])


# s = "suneelyadav"
# print(s[int(input("enter here:")):])


# import datetime
# from datetime import timedelta
# date = datetime.datetime(2020, 2, 25)
# expected_date = date - timedelta(days=7)
# print(expected_date)


# a lottery program by picking the two lucky winners

# import random
# lottry_list = []
#
# for i in range(100):
#     lottry_list.append(random.randrange(1000000000,9999999999))
#
# winner = random.sample(lottry_list,2)
# print("2 lucky winners:",winner)


# def myfunction(a,b):
#     return a+b
# a=4
# b=1
# print(myfunction(a,b))

# import random
# l = []
# numbers = random.randrange(1,101)
# for i in range(numbers):
#     l.append(i)
# print(random.sample(l,25))


# t1 = (1,2,3)
# t2 = (3,4,5)
# com = zip(t1,t2)
# print(dict(com))


# Task 1: store the square of numbers between 5 to 15 in an array and print it,
# import numpy as np
# lst = [i*i for i in range(5,16)]
# print(np.array(lst))


# Task 2: Generate a list of 25 random numbers. \n",
# "The numbers should be between 100 and 150. \n",
# "Remove duplicates from the list. \n",
# "Find maximum and minimum from the list\n",
# "\n",
# "Generate a new list with only odd numbers from the above random

# import random
# lst = []
# for i in range(25):
#     lst.append(random.randrange(100,151))
# print("list of 25 random numbers:",lst)
# print("maximum number:",max(lst))
# print("minimum number:",min(lst))
# print("after removing all duplicates:",set(lst))
# new_lst = [x for x in lst if x%2 != 0]
# print("new list with odd numbers:",new_lst)

# import numpy as np
# l = []
# lst = "Computer programming is the process of designing and building an executable computer program to accomplish a specific computing result or to perform a specific task. Programming involves tasks such as: analysis, generating algorithms, profiling algorithms' accuracy and resource consumption, and the implementation of algorithms in a chosen programming language ***(commonly referred to as coding)***. The source code of a program is written in one or more languages that are intelligible to programmers, rather than machine code, which is directly executed by the central processing unit. The purpose of programming is to find a sequence of instructions that will automate the performance of a task ***(which can be as complex as an operating system)*** on a computer, often for solving a given problem. Proficient programming thus often requires expertise in several different subjects, including knowledge of the application domain, specialized algorithms, and formal logic."
# l.append(np.array(text))
# print(l)
# print(type(np.array(l)))


# Task 5: For each line, extract the list of words that contains 10 or more letters. Store the result in a array.

# res_list = []
# for i in range(len(text)):
#     temp_list = text[i].split()
#     l = []
#     for j in range(len(temp_list)):
#         if len(temp_list[j]) >= 10:
#             l.append(temp_list[j])
#         else:
#             continue
#     res_list.append(l)
# print(res_list)


# res_lst = []
# for i in range(len(lst)):
#     temp_lst = lst[i].split()
#     nest_lst = []
#     for j in range(len(temp_lst)):
#         if len(temp_lst[j]) >= 10:
#             nest_lst.append(temp_lst[j])
#         else:
#             continue
#     res_lst.append(nest_lst)
# print(res_lst)


# Given data  = {'A': [1,1,2,3,1,2,1,1,1,2,2,2,2,2]}, Print no of occurrences of each element?

# data = [1,1,2,3,1,2,1,1,1,2,2,2,2,2]
# di = dict()
# for i in data:
#     di[i] = data.count(i)
# print(di)


# data  = {'A': [1,1,2,3,1,2,1,1,1,2,2,2,2,2]}
#
# for value in data.values():
#     x = value
#     dic = dict()
#     for i in x:
#         dic[i] = x.count(i)
#     print(dic)


# A PROGRAM IN GENERATOR FUNCTION
# l = [1,1,2,3,1,2,1,1,1,2,2,2,2,2]
# def traverse(li):
#     for i in range(len(li)):
#         yield li[i]
#
#
# l1 = [1,1,2,3,1,2,1,1,1,2,2,2,2,2]
# for j in  traverse(list(l1)):
#     print(j,end="")


# dict1 = ["go","bat","me","eat","goal","boy", "run"]
# arr = ['e','o','b', 'a','m','g', 'l']

# res = []
# for i in dict:
#     c = 0
#     for j in range(len(i)):
#         if i[j] in arr:
#             c +=1
#     if c == len(i):
#         res.append(i)
# print(res)

# res = zip(dict1,arr)
# print(dict(res))


# inp = [(1,2,3)]{1,2}{[(1,2,3)(1,2,3)](1,2)}
# print(inp)


# s = "aaccbbcccdaaaaddde"
# t = list(set(s))
# l = []
# for i in t:
#     c = 0
#     for j in s:
#         if i == j:
#            c +=1
#     if c>=1:
#         print(i+str(c),end="")


# st = input("Enter the sequence")
#
# for i in range(len(st)):
#   st = st[i+1:]
#   f_s = st[0]
#   count = 0
#   for i in range(len(st)):
#     if st[i] == f_s:
#       count += 1
#       if st[i] == st[i+1]:
#         continue
#       else:
#         break
#   c = str(count)
#   print(f_s+c,end="")


# A = [2, 3, 4, 5, 6, 1, 7, 8, 9, 10]
# B = [9, 5, 1, 2]
# c = []
# for i in A:
#     for j in B:
#         if i == j:
#             c.append(i)
# print(c)


# arr = [1, 2, 3, 4, 5, 6, 7]
#
# n = int(input("enter no for rotation:"))
# print(arr[n:] + arr[:n])


# l = [1,2,3,4,5,6,78,9]
# largest = l[0]
# scnd_largest = l[0]
# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
# for i in range(len(l)):
#     if l[i] > scnd_largest and l[i] != largest:
#         scnd_largest = l[i]
# print(scnd_largest)


#
# li = [1,2,3,4,5,6,7,8,9]
# largest = li[0]
# scndlargest = li[0]
# for i in range(len(li)):
#     if li[i] > largest:
#         largest = li[i]
# for i in range(len(li)):
#     if li[i] > scndlargest and li[i] != largest:
#         scndlargest = li[i]
# print(scndlargest)


# print(list(map(lambda a:a+2,[2,4,6,8])))


# a = 5
# b = 10
# print("before swapping the variable a:",a)
# print("before swapping the variable b:",b)
# temp = a
# a = b
# b = temp
#
#
# print("after swapping the variable a:",a)
# print("after swapping the variables b:",b)

# a = a+b
# b = a-b
# a = a-b

# a,b = b,a

# a = a ^ b
# b = a ^ b
# a = a ^ b


# a = a * b
# b = a / b
# a = a / b
# print("after swapping the variable a:",a)
# print("after swapping the variables b:",b)


# 24.	Suppose a child class inherited from two classes which are having same method. Now an object of child class will call
# that declared method. So, from which parent class it is being called?

# class Suneel():
# def __init__(self,name1,name2,wish):
#     self.name1 = name1
#     self.name2 = name2
#     self.wish = wish

#     def hii(self):
#         print("suneel")
#
# #
# #
# #
# class Anil():
#     def hi(self):
#         print("anil ")
#
#
# class Brother(Anil,Suneel):
#     def __init__(self):
#         super().__init__()
#     def bye(self):
#         print("hello")
#         super().hii()
#
#
# a = Brother()
# a.bye()
# a.hi()


# Suppose if a child class C is derived from both A & B and how can we call “set” method from Class A and “get” method from class B?

# class A():
#
#     def set(self):
#         pass
#
#     def get(self):
#         pass
#
#
# class B():
#     def set(self):
#         pass
#
#     def get(self):
#         pass
#
# class C(A,B):
#
#     def put(self):
#         pass
#         A.set(self)
#         B.get(self)

#
# a = C()
# print(a)


# s = "suneelislearner"
# temp = set(s)
# dup = []
# for i in temp:
#     c = 0
#     for j in s:
#         if i == j:
#             c +=1
#
#     if c>1:
#         dup.append(i)
# print((dup))


# from datetime import datetime
# s = '02/05/22'
# date = datetime.strptime(s,'%d/%m/%y')
# print(date)
#
#
# date1 = datetime.now()
# print(date1)
# s = datetime.strftime(date1,'%y/%m/%d')
# print(type(s))


# for i in range(1,11):
#     if i == 0:
#         print(i)
#     else:
#         print(i-1 + i)
#


# s = input("enter string:")
# n = int(input("enter no elements to remove:"))
#
# print(s[n:])

# import random
# lst_of_rndm = []
# for i in range(25):
#     lst_of_rndm.append(random.randrange(1000000000,9999999999))
# winner = random.sample(lst_of_rndm,2)
# print("two lucky winners:",winner)


# test_dict = {'nikhil' : 1, "akash" : 2, 'akshat' : 3, 'manjeet' : 4}

# for key in test_dict.keys():
#     if key == 'nikhil' :
#         print(key,":",test_dict[key])
#     elif  key == 'akshat':
#         print(key, ":", test_dict[key])


# res = {key:test_dict[key] for key in test_dict.keys() & {'nikhil',"akash"}}
# print(res)


# x = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
# l1 = []
# for i in range(len(x)):
#     l = []
#     if i == 0:
#         l.append(x[i])
#     else:
#         l1.append(x[i])
#     print(l1 + l)

# x.sort()
# x.reverse()
# print(x)


# values = [num for num in x if num != 0] + [num for num in x if num == 0]
# print(values)


# import copy
# l = [1,2,3,4,1,5,2,6,8,13,4]
# l1 = copy.copy(l)
# l2 = copy.deepcopy(l)
# print(l)
# print(l1)
# print(l2)


# s1 = "suneel"
# b = s1+s1
# s2 = "es"
# if s2 in b:
#     print("it is subset of s1")
# else:
#     print("it is not a subset ")

# aaccbbcccdaaaaddde
# st = input("Enter the sequence")
#
# for x in range(len(st)):
#   st = st[x+1:]
#   f_s = st[0]
#   count = 0
#   for i in range(len(st)):
#     if st[i] == f_s:
#       count += 1
#       if st[i] == st[i+1]:
#         continue
#       else:
#         break
#   c = str(count)
#   print(f_s+c,end="")


# t = list(set(st))
# for i in range(len(t)):
#   c = 0
#   for j in range(len(st)):
#       if t[i] == st[j]:
#         c +=1
#   if c>=1:
#       print(st[i] + str(c),end="")


# l = [1,2,3,4,5,6,7]
# l1 = []
# for i in l:
#     l1.append(i*2)
# print(l1)


# s = "string"
# for i in range(100):
#     print(s,end="")

# s = "string"
# y = s * 100
# print(y)

#
# from abc import ABC,abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def get(self):
#         print("hello")
#
#
# a = shape()
# a.get()


# s = "suneel"
# print(s[0::2])


# l = [0,1,2,3,4,5,6,7,8,9,10]
# print(l[0:7:2][::-1])


# for fizzbuzz in range(1,101):
#     if fizzbuzz%15 == 0:
#         print("fizzbuzz",end=" ")
#         continue
#     elif fizzbuzz%3 == 0:
#         print("fizz",end=" ")
#         continue
#     elif fizzbuzz%5 == 0:
#         print("buzz",end=" ")
#         continue
#     print(fizzbuzz,end=" ")

# Python program to print Fizz Buzz

# # Loop for 100 times i.e. range
# for fizzbuzz in range(1, 100):
#
#     # Number divisible by 15,(divisible
#     # by both 3 & 5), print 'FizzBuzz'
#     # in place of the number
#     if fizzbuzz % 15 == 0:
#         print("FizzBuzz")
#         continue
#
#     # Number divisible by 3, print 'Fizz'
#     # in place of the number
#     elif fizzbuzz % 3 == 0:
#         print("Fizz")
#         continue
#
#     # Number divisible by 5,
#     # print 'Buzz' in
#     # place of the number
#     elif fizzbuzz % 5 == 0:
#         print("Buzz")
#         continue
#
#     # Print numbers
#     print(fizzbuzz)


# l = [1,2,3,4,5]
# fun = list(map(lambda x:x**2,l))
# print(fun)


# def function(n):
#     if n == 0:
#         return 0
#     else:
#         return function(n-1) + 100
# n1 = 5
# print(function(n1))


# def function(n):
#     s = 0
#     for i in range(1,n+1):
#         s += (i)/(i+1)
#     return s
# n1 = 6
# print(function(round(n1)))

# n = 6
# s = 0.0
# for i in range(1,n+1):
#     s += (i)/(i+1)
# print(round(s,2))


# list1 = [1,2,3,4,5,6,7,8,9,10]
#
# t = list1
# items = [x for x in list1 if x+x == 10 ]
# print(items)
# l = []
# for i in range(len(list1)):
#     for j in range(i+1,len(list1)):
#         if i+j == 10:
#             print(*(i, j))


# def brother(name1):
#     def add(name2):
#
#         a = name1(name2)
#         print("his name is:",a)
#     return add
#
# @brother
# def what_name(name):
#     return (name)
# # print(brother(what_name))
# what_name("suneel")


# def fun(n):
#     f = 1
#     for i in range(1,n+1):
#         f = f * i
#     return f
# x = 5
# print(fun(x))

# n = 9
# for i in range(1,11):
#     print(n, "*", i ,"=", n*i)

#
# n = int(input("enter number:"))
# l = str(n)
# sum = 0
# i = 0
#
# while sum < n:
#     sum += int(l[i]) ** len(l)
#     i +=1
# if sum == n:
#     print("it is a amstrong")
# else:
#     print("it is not a amstrong")
#
#
# n = int(input("enter"))
# l = str(n)
# sum = 0
# for  i in range(len(l)):
#     sum += int(l[i]) ** len(l)
# if sum == n:
#     print("it is am")
# else:
#     print("it is not")


# l = [1,2,3,4,5,6,7,8,9,10]
#
# ls = list(map(lambda x:x*2,(filter(lambda x:(x%2 == 0), l))))
#
# print(ls)


# def function(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n>1:
#         return function(n-1) + function(n-2)
# print(function(5))


# def function(n):
# n = int(input("enter n :"))
# n1, n2= 0, 1
#
# c = 0
# if n <= 0:
#     print(0)
# elif n == 1:
#     print(n1)
# else:
#     while c < n:
#         print(n1)
#         nth = n1 + n2
#         n1 = n2
#         n2 = nth
#         c +=1


# res = function(n)
# print(res)

# Program to display the Fibonacci sequence up to n-th term

# nterms = int(input("How many terms? "))
#
# # first two terms
# n1, n2 = 0, 1
# count = 0
#
# # check if the number of terms is valid
# if nterms <= 0:
#    print("Please enter a positive integer")
# # if there is only one term, return n1
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# # generate fibonacci sequence
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        # update values
#        n1 = n2
#        n2 = nth
#        count += 1


# n  = int(input("enter n :"))
# i = 0
# n1 = 0
# n2 = 1
# while i < n:
#     print(n1)
#     nth = n1 + n2
#     n1 = n2
#     n2 = nth
#     i +=1


# def feb(n):
#     # c= 0
#     n1 = 0
#     n2 = 1
#     for i in range(n):
#         if i <= 0:
#             print(0)
#         else:
#
#             c = n1 + n2
#             n1 = n2
#             n2 = c
#             print(n1)
# nth  = int(input("enter n :"))
# feb(nth)


# def feb(n):
#     a,b = 0,1
#     c = 0
#     while c < n:
#         yield a
#         a,b = b,a+b
#         c +=1
# for i in feb(7):
#     print(i)


# lst = [1,2,[3,4,[5,6,[7,8,9]]]]
# res_lst = []
# def inlist(l):
#     for i in l:
#         if type(i) is list:
#             return inlist(i)
#         else:
#             res_lst.append(i)
#     return res_lst
# print(inlist(lst))


# lst = [1,2,[3,4,[5,6,[7,8,9]]]]
# res_lst1 = []
# def inlist(l):
#
#     for i in (l):
#         if type(i) is list:
#             return inlist(i)
#         else:
#             res_lst1.append(i)
#
#     return res_lst1
# print(inlist(lst))


# import pandas as pd
# df1 = pd.DataFrame({
#                  "A1": ["a", "b", "c", "d"],
#                  "B2": ["e", "f", "g", "h"],
#                  "C3": ["i", "j", "k", "l"],
#                  "A2": ["a", "b", "c", "d"],
#                  "C": ["i", "j", "k", "l"],
#                  "D4": ["m", "n", "o", "p"]
#          })
#
#
#
# def get_duplicate(df):
#     duplicate_clmn = set()
#     for x in range(df.shape[1]):
#         colmn = df.iloc[:,x]
#         for y in range(x+1,df.shape[1]):
#             otrcolmn = df.iloc[:,y]
#             if colmn.equals(otrcolmn):
#                 duplicate_clmn.add(df.columns.values[y])
#     return duplicate_clmn
# duplicates = get_duplicate(df1)
# for col in duplicates:
#     print("duplicates:",col)


# s = " su neel "
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())
# print(s.replace(" ",""))


#
# import pandas as pd
# df1 = pd.DataFrame({
#                  "A1": ["a", "b", "c", "d"],
#                  "B2": ["e", "f", "g", "h"],
#                  "C3": ["i", "j", "k", "l"],
#                  "A2": ["a", "b", "c", "d"],
#                  "C": ["i", "j", "k", "l"],
#                  "D4": ["m", "n", "o", "p"]
#          })

#
# def duplicate(df):
#     dup_columns = set()
#     for x in range(df.shape[1]):
#         col = df.iloc[:,x]
#         for y in range(x+1,df.shape[1]):
#             othr_colmn = df.iloc[:,y]
#             if col.equals(othr_colmn):
#                 dup_columns.add(df.columns.values[y])
#     return dup_columns
# duplicates = duplicate(df1)
# for col in duplicates:
#     print("duplicate columns:", col)


# def convert(di,tup):
#     for a,b in tup:
#         di.setdefault(a,[]).append(b)
#     return di
# dic = {}
# tup1 = [("suneel",2),("a",5),("b",8),("c",7)]
# print(convert(dic,tup1))


# for col in df1.columns:
#     if "A1" in col:
#         del df1[col]
# print(df1)


# print(df1.drop(["A1"],axis=True))

# print(df1.drop(df1.columns[[1]],axis=True))

# l = [1,2,3,4,5,6,7,8,9]
# for i in range(len(l)):
#     print(l[i])


# i = 0
# while i < len(l):
#     print(l[i])
#     i +=1


# for fizzbuzz in range(1,101):
#     if fizzbuzz%3 == 0:
#         print("fizz",end=" ")
#     elif fizzbuzz%5 == 0:
#         print("buzz",end=" ")
#     else:
#         print(fizzbuzz,end=" ")


# l = [1,2,3,4,5,6,7,8,9]
# largest = l[0]
# scnd_largest = l[0]
# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
# for j in range(len(l)):
#     if l[j] > scnd_largest and l[j] !=largest:
#         scnd_largest = l[j]
# print("the second largest number:",scnd_largest)

#

# # l = [x for x in f]
# l = []
# for i in f:
#     # l.append(i)
#     y = i.split(".")
#     l.append(y)
#     print(y)
# # print(y)
# for j in y:
#     n = j.split(' ')
#     # print(n)
#     c = 0
#     for k in n:
#         if len(k)>=10:
#             l.append(k)
#             print(l)


# for i in f:
#     if i.startswith("(") and i.endswith(")"):
#         print("jhh",i)
# # print(l)
# import re
#
# x=re.findall(r'\(.*?\)',f)
# print(str(x))


#
#
#         # x = str(j).split(" ")


# Dict = ["go","bat","me","eat","goal","boy", "run"]
# arr = ['e','o','b', 'a','m','g', 'l']
#
# l = []
# for i in Dict:
#     c = 0
#     for j in range(len(i)):
#         if i[j] in arr:
#             c +=1
#     if c == len(i):
#         l.append(i)
# print(l)


# f = open(r"C:\Users\ulasa\OneDrive\Documents\file name.txt","r")
# print(f.read())
#
# l = []
# for i in f:
#     y = i.split(".")
#
#     print(y)

# d = {'A': [1,1,2,3,1,2,1,1,1,2,2,2,2,2]}
# for key,value in d.items():
#     y = value
#     t = list(set(y))
#     l = []
#
#     for j in t:
#         c = 0
#         for k in y:
#             if j == k:
#                 c +=1
#         if c>=1:
#             l.append(c)
#             print(j,c)

# d = {'A': [1,1,2,3,1,2,1,1,1,2,2,2,2,2]}
# for key,value in d.items():
#     y = value
#     d = dict()
#     for i in y:
#         x = y.count(i)
#         d[i] = x
# print(d)


# def brother(name1):
#     def add(name2):
#         print("he is my brother:",name1(name2))
#     return add
#
#
#
# @brother
# def bro(name):
#     return name
# bro("suneel")

# l = [1,2,3,4,6,6]
# def myfunction(l):
#     for i in l:
#         yield i
#
#
# l1 = [1,2,3,4,6,6]
# print(list(myfunction(l1)))


# a1 = "aaccbbcccdaaaaddde"
#
# s = ""
# a = 1
# for i in range(1,len(a1)):
#     if a1[i-1] == a1[i]:
#         a +=1
#     else:
#         s = s+a1[i-1]
#         if a>1:
#             s += str(a)
#         a = 1
# s = s+a1[-1]
# if a>1:
#     s +=str(a)
# print(s)


# A = [ 2, 3, 4, 5, 6, 1, 7, 8, 9, 10]
# B = [9, 5, 1, 2]

# s = "suneel"
# s1 = "nel"
# a = s + s
# print("it is subset:",s1 in s)

# print(B in  A)
# l = [A for B in A ]
# l = []
# for i in A:
#     for j in B:
#         if i == j:
#             l.append(i)
# print(l)


# list1 = [1,2,3,4,5,6,7,8,9,10]
# for i in range(len(list1)):
# l = [x for x in list1 if x + x == 10 ]
# print(l)

# for i in range(len(list1)):
#     for j in range(i+1,len(list1)):
#         if i + j == 10:
#             print((i,j),end="")


# l = [x**2 for x in range(5,16) ]
# print(l)
#
# import random
# l = []
# for i in range(25):
#     l.append(random.randrange(1,26))
# print(l)
#
# print(len(l))


# text = "Computer programming is the process of designing and building an executable computer program to accomplish a specific computing result or to perform a specific task. Programming involves tasks such as: analysis, generating algorithms, profiling algorithms' accuracy and resource consumption, and the implementation of algorithms in a chosen programming language (commonly referred to as coding). The source code of a program is written in one or more languages that are intelligible to programmers, rather than machine code, which is directly executed by the central processing unit. The purpose of programming is to find a sequence of instructions that will automate the performance of a task (which can be as complex as an operating system) on a computer, often for solving a given problem. Proficient programming thus often requires expertise in several different subjects, including knowledge of the application domain, specialized algorithms, and formal logic."
# l = []
# for i in text.split("."):
#      l.append(i)
#      y = i.split(" ")
# print(l)
# for j in l:
#      z = j.split(" ")
#      print("jj",z)
#      for k in range(len(z)):
#           print(z.count(k))


# for i in range(1,11):
#     # if i == 0:
#     #     print(0)
#     # elif i == 1:
#     #     print(i)
#     # else:
#         print((i - 1) +i)

# l1 = [5, 10, 15, 20, 25, 30, 30]
# l = [1,2,3,4,5,6,7,8,9,10]
# for i in range(len(l)):
#     if i == 0:
#         print(l[i])
#     else:
#         print(l[i-1] + l[i])


# n = int(input("enter n:"))
# n1 = 0
# n2 = 1
# for i in range(n):
#
#     # if i == 0:
#         print(n1)
#
#         c = n1 + n2
#         n1 = n2
#         n2 = c
# print(n1)


# import random
# l = []
# for i in range(1,101):
#     l.append(random.randrange(100000000,9999999999))
# winnners = random.sample(l,2)
# print("two lucky winners:",winnners)


# d = { "sb":47,"s":[5,5,47,8],"s":[55]}
# print(d)


# def fac(n):
#     return 1 if (n == 0 or n == 1) else n * fac(n - 1)
# def strong(n):
#     s,total = str(n),0
#     for i in range(len(s)):
#         total += fac(int(s[i]))
#     print("Given number is strong number") if total == n else print("Given number is not a strong number")
# strong(145)


# import pyautogui
import functools

# l = "suneel"
# l1 = []
# for i in range(len(l)):
#     l1.append(l[i])
# print(l1)

# from functools import reduce
# l2 = ['s', 'u', 'n', 'e', 'e', 'l']
# item = (reduce(lambda y,x:y+x,l2))
# y=[str(x) for x in item]
# print(y)

# l2 = ['s', 'u', 'n', 'e', 'e', 'l']
# s = ""
# # t = l2
# for i in range(len(l2)):
#     y = str(l2[i])
#     print(str(y),end="")
# for j in range(len(t)):
#
#     s += l2[i] + t[j]
# print(s)


# Square of all the elements in a list using lambda (inputfrom user)

# l = list((input("enter:")))
# item = (map(lambda x: x**2,l))
# print(item)

# import pandas as pd
# d = {"rollno":[1,2,3,4,5],"name":["s","b","m","k","a"],"marks":[10,11,12,13,14]}
# df = pd.DataFrame(d)
# print(df)


# n = 153
# s = str(n)
# sum = 0
# for i in s:
#     sum += int(i)**len(s)
# if sum == n:
#     print('it is a amstrong')
# else:
#     print('it not a amstrong')


# n = 153
# s = str(n)
# sum = 0
# i = 0
# while sum < n:
#     sum += int(s[i]) ** len(s)
#     i +=1
# if sum == n:
#     print('it is a amstrong')
# else:
#     print('it not a amstrong')


# def fac(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fac(n - 1)
# def sum(n):
#     s = str(n)
#     total = 0
#     for i in range(len(s)):
#         total += (fac(int(s[i])))
#     if total == n:
#         print("it is strong")
#     else:
#         print("it not")
# sum(145)


# import pandas as pd
# df1 = pd.DataFrame({
#                  "A1": ["a", "b", "c", "d"],
#                  "B2": ["e", "f", "g", "h"],
#                  "C3": ["i", "j", "k", "l"],
#                  "A2": ["a", "b", "c", "d"],
#                  "C" : ["i", "j", "k", "l"],
#                  "D4": ["m", "n", "o", "p"]
#          })
#
#
# def duplicate(df):
#     duplicate_col = set()
#     for x in range(df.shape[1]):
#         col = df.iloc[:,x]
#         for y in range(x+1,df.shape[1]):
#             other_col = df.iloc[:,y]
#             if col.equals(other_col):
#                 duplicate_col.add(df.columns.values[y])
#     return duplicate_col
# print(duplicate(df1))


# d = {"a":5, "b":6, "c":7, "d": 8, "e":9}
# i = input("enter")
# for i,j in d.items():
#     print(i,",",j)
# print(d["a"])
# print(d[input("enter")])

# x = int(input("enter:"))
# if x%7 == 0 or x%10 == 7:
#     print("it is")
# else:
#     print("not")


# import pandas as pd
# df1 = pd.DataFrame({
#                  "A1": ["a", "b", "c", "d"],
#                  "B2": ["e", "f", "g", "h"],
#                  "C3": ["i", "j", "k", "l"],
#                  "A2": ["a", "b", "c", "d"],
#                  "C" : ["i", "j", "k", "l"],
#                  "D4": ["m", "n", "o", "p"]
#          })
#
# def duplicates(df):
#     duplicate_col = set()
#     for x in range(df.shape[1]):
#         column = df.iloc[:,x]
#         for y in range(x+1,df.shape[1]):
#             other_col = df.iloc[:,y]
#             if column.equals(other_col):
#                 duplicate_col.add(df.columns[y])
#     return duplicate_col
# print(duplicates(df1))

# lst = list(map(int,input("enter numbers:").split(" ")))
# square = list(map(lambda x:x**2,lst))
# print(square)

# for col in df1.columns:
#     if "A1"and "C" in col:
#         del df1[col]
# print(df1)


# def duplicates(df):
#     duplicate_col = set()
#     for x in range(df.shape[1]):
#         col = df.iloc[:,x]
#         for y in range(x+1,df.shape[1]):
#             othr_col = df.iloc[:,y]
#             if col.equals(othr_col):
#                 duplicate_col.add(df.columns.values[y])
#     return duplicate_col
# print(duplicates(df1))


# def convert(di,tup):
#     for a,b in tup:
#         di.setdefault(a,[]).append(b)
#     return di
# dit = {}
# tup1 = [("s",2),("u",3),("n",4),("e",5)]
# print(convert(dit,tup1))


#
# s = "aabcddeebfgfh"
# t =
# x = 0
# x +=5
# print(x)


import datetime
from datetime import timedelta


# begin_date = datetime.datetime.now()
# print(begin_date)
# ending_date = begin_date + timedelta(days= 45)
# print(ending_date)

# s = "28/05/22"
# date = datetime.datetime.strptime(s,"%d/%m/%y")
# print(date)
# print(type(date))

# date = datetime.datetime.now()
# print(date)
# date_str = datetime.datetime.strftime(date, "%y/%m/%d %H:%M:%S")
# print(date_str)
# print(type(date_str))


# lst = [1,2,3,4,5,6,7,8,9]
# largest = lst[0]
# scnd_largest = lst[0]
# for i in range(len(lst)):
#     if lst[i] > largest:
#         largest = lst[i]
# for j in range(len(lst)):
#     if lst[j] > scnd_largest and largest != lst[j]:
#         scnd_largest = lst[j]
# print(scnd_largest)


# def isperfectsquare(x):
#     s = x**0.5
#     return s**2 == x
# def isfibonacci(n):
#     return isperfectsquare(5*n**2+4) or isperfectsquare(5*n**2-4)
# n1 = int(input("enter number:"))
# if isfibonacci(n1) == True:
#     print(n1," is a fibonacci number")
# else:
#     print(n1," is not a fibonacci number")
#
# n = 5
# # n = int,input("enter:")
# if (5*n**2-4 == n) or (5*n**2+4 == n):
#     print("it is a fibonacci number")
# else:
#     print("it is not a fibonacci")


# def fac(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fac(n-1)
# def strong(n1):
#     s = str(n1)
#     sum = 0
#     for i in range(len(s)):
#         sum += fac(int(s[i]))
#         print(s[i])
#     if sum == n1:
#         print("it is a strong number")
#     else:
#         print("it is not a strong number")
# strong(145)

# def myfunction(**kwargs):
#     print("args:",kwargs["verb"])
# myfunction(subject = "i",verb = "am",word = "learner")


# colours = ((1,"red"),(2,"blue"),(3,"black"),)
# for i in range(len(colours)):
#     if colours[i][1] == "black":
#         print(colours[i-1][0])


# l = [yhj,ghvh,gkvk,]
# di = {"s":1,"u":2,"n":3,"e":4}
# for i,j in di.items():
#     if j == 2:
#         print(i)

# import pandas as pd
# di = {"rollno":[1,2,3,4,5],"name":["s","u","n","e","e"],"marks":[10,11,12,13,14]}
# df = pd.DataFrame(di,index=[1,2,3,4,9])
# print(df)
# print(df.['name']=='u')


# s = ("s","u","n",",","e","e","l")
# print((s[:]))

# s = "usuneel"
# print(s[-1:-5:-1])
# print(len(s))

# n = int(input("enter number:"))
# n1 = 0
# n2 = 1
# i = 0
# while i<n:
#     print(n1)
#     c = n1+n2
#     n1 = n2
#     n2 = c
#     i +=1


# colours = ((1,"red"),(2,"blue"),(3,"black"),)
# for i in range(len(colours)):
#     if colours[i][1] == "black":
#         print(colours[i-1][0])


# l = [1,2,3,4,5]
# l1 = [1,2,3,4,5]
# items = [i//j for i,j in zip(l,l1)]
# print(items)


# def SearchingChallenge(x):
#
#   # code goes here
#   for i in range(len(x)):
#     for j in range(len(x)):
#       if x[0] != x[j]:
#         return x[i]
#
#


#
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]
# l = []
# for i in range(1,101):
#   if i%7 == 0:
#     l.append(i)
# print(l)

# print([x for x in range(0,101,7)])
# print(items)


# s = input("enter:")
# v =  "aeiou"
# s.islower()
#
# c = 0
# for i in (s):
#     if i in  v:
#         c +=1
# print(c)
# for j in (v):
#
#     if s[i] == v[i]:
#         c +=1
#         print(c)


# purposeful
# serpant

# s1 = input("entet s1:")
# s2 = input("enter s2:")
# s1=s1.lower()
# s2=s2.lower()
#
# l = []
# for i in range(len(s1)):
#     for j in range(len(s2)):
#         if s1[i] == s2[j]:
#             l.append(s1[i])
# print(set(l))


# x = ("apple","banana")
# y = ("apple","banana")
# z = x
#
# print(x is y)
# print(x is z)
# print(x == y)


# x = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# print(x[1:3][0:2])


# keep this function call here
# print(SearchingChallenge(input("enter:")))
#
# SearchingChallenge(str) take the str parameter being passed, which will contain only alphabetic characters and spaces,
# and return the first non-repeating character. For example: if str is "agettkgaeee" then your program should return k.
# The string will always contain at least one character and there will always be at least one non-repeating character.
# Once your function is working, take the final output string and concatenate it with your ChallengeToken,
# and then replace every fourth character with an underscore.
#
# Your ChallengeToken: j6t3wz5oa0
# Have the function ArrayChallenge(arr) take the array of numbers stored in arr and
# determine the largest sum that can be formed by any contiguous subarray in the array.
# For example, if arr is [-2, 5, -1, 7, -3] then your program should return 11 because the
# sum is formed by the subarray [5, -1, 7]. Adding any element before or after this subarray would make the sum smaller.
# Examples
# Input: [1, -2, 0, 3]
# Output: 3
# Input: [3, -1, -1, 4, 3, -1]
# Output: 8
# Python version
# --------------
# 3.8.3 [GCC 8.3.0]
#
# Packages installed
# ------------------
# boto3
# numpy
# pandas
# pyspark
# pytest
# requests
# scikit-learn
# scipy
# tensorflow
#
# output logs will appear here
# def ArrayChallenge(arr):
#
#   # code goes here
#   return arr
#
# # keep this function call here
# print(ArrayChallenge(input()))


# s = "abcdfa"
#
# while s != "":
#   slen_0 = len(s)
#   ch = s[0]
#   s = s.replace(ch,"")
#   slen_1 = len(s)
#   if slen_1 == slen_0 -1:
#     print(ch)
#     break
#   else:
#     pass


# b = "j6t3wz5oa0876"
#
# a = "abcde"
# l = []
# for i in a:
#     c = 0
#     for j in a:
#         if i == j:
#             c +=1
#     if c == 1:
#         l.append(i)
# y = l[0]+b
# items = [x for x in y ]
# for i in range(len(y)):
#     if (i+1)% 4 == 0:
#         y = y.replace(y[i],'_')
# print(y)
# op = [y.replace(ch,'_') for ch in y[::4]]
# print(op)
# op = list(map(lambda x: ))
#
# def ArrayChallenge(l):
#
#     for i in range(len(l)):
#         s = l[i]
#         for j in range(len(l)):
#             if j<len(l)-1:
#                 new_s = s + l[j+1]
#                 if s < new_s:
#                     s = new_s
#                 else:
#                     pass
#             else:
#                 pass
#
# print(ArrayChallenge([-2, 5, -1, 7, -3]))
#
#
# def maxSubArraySum(a, size):
#     max_so_far = a[0]
#     curr_max = a[0]
#
#     for i in range(1, size):
#         curr_max = max(a[i], curr_max + a[i])
#         max_so_far = max(max_so_far, curr_max)
#
#     return max_so_far
#
# a = [-2, 5, -1, 7, -3]
# print( maxSubArraySum(a, len(a)))


# print(input("enter string:").split(",")[::-1]*100)
# n = (input("enter:"))
# a = n[::-1]
# print(f"{n[0]}{a[:-1]}")


# def encrypt(text, s):
#     result = ""
#     for i in range(len(text)):
#         char = text[i]
#         if (char.isupper()):
#             result += chr((ord(char) + s - 65) % 26 + 65)
#         else:
#             result += chr((ord(char) + s - 97) % 26 + 97)
#         return result
# text = "CEASER CIPHER DEMO"
# s = 4
# print( "Plain Text : " + text)
# print ("Shift pattern : " + str(s))
#
# print("Cipher: " + encrypt(text, s))


# lst = [-5, -23, 5, 0, 23, -6, 23, 67]
# newlst = []
# for i in range(len(lst)):
#     minmum = lst[0]
#     for j in lst:
#         if j < minmum:
#             minmum = j
#     newlst.append(minmum)
#     lst.remove(minmum)
# print(newlst)


# n = int(input("enter number:"))
# s = str(n)
# a = s[::-1]
# if n < 0:
#     print(int(s[0] + a[:-1]))
# else:
#     print(int(s[::-1]))


#
# n = int(input("enter:"))
# s = str(n)
# l = len(s)
# min_l = l - 4
# s_len = s[min_l:]
# print("#" * min_l + s_len)


#
# def order_list(l):
#     lst = []
#     for i in range(len(l)):
#         mnm = l[0]
#         for j in l:
#             if j < mnm:
#                 mnm = j
#         lst.append(mnm),l.remove(mnm)
#
#     return lst
# lst1 = list(map(int,input("enter:").split(",")))
# print(order_list(lst1))


# def strxor(a, b):     # xor two strings of different lengths
#     if len(a) > len(b):
#         return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
#     else:
#         return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])
# print(strxor("abcde","fghi"))

# print(ord('z'))
# print(126-97)


# s = input("enter:")
# c = ""
# for i in s:
#     if i.isupper():
#         c += chr((ord(i) + 4 - 65) %26 + 65)
#
#     else:
#         c+=chr(((ord(i) + 4-97)%26) + 97)
# print(c)


# def anil(name1):
#     def add(name2):
#         return ("he is my brother " + name1(name2))
#     return add
#
# @anil
# def brother(name):
#     return name
# print(brother("suneel"))

#


# a = 5
# b = 10


# print("before swapping a=",a,"b=",b)
# a = a + b
# b = a-b
# a = a-b

# x = a
# a = b
# b = x

# a,b = b,a
#
# a = a * b
# b = a // b
# a = a // b

# a = a ^ b
# b = a ^ b
# a = a ^ b
# print("after swapping a=",a,"b=",b)


# s = "asdfhgfskjiopyukoio"
# t = set(s)
# for i in t:
#     c = 0
#     for j in s:
#         if i == j:
#             c +=1
#     if c >= 1:
#         print(i+str(c),end="")


# s = "asdfhgfskjiopyukoio"
# d = dict()
# for i in s:
#     y = s.count(i)
#     d[i] = y
# print(d)

# l = [1,2,3,4,5,6,7,8,9]
# n = int(input("enter the no of rotations:"))
# print("before rotations:",l)
# rotations = l[n:] + l[:n]
# print("after no of rotations:",rotations)


# l = [5,6,7,4,8,2,9]
# for i in range(len(l)):
#     if i ==0:
#         print(l[i])
#     else:
#         print(l[i -1] + l[i])


# s = "suneelyadav"
# n = int,input("enter to remove:")
#
# print(s[n:])

# import random
# random_lst = []
# for i in range(100):
#     random_lst.append(random.randrange(1000000000,9999999999))
# lucky_winners = random.sample(random_lst,2)
# print("the lucky tow winners:",lucky_winners)


# def formate_string(a):
#     res = ""
#
#     for i,digit in enumerate(reversed(str(a))):
#
#         if i != 0 and i%3 == 0:
#             res += ","
#         res += digit
#     return res[::-1]
# print(formate_string(10000000))


# item = s + s
#
# def double_string(s):
#     for i in range(len(s)-1 ):
#         if s[i] == s[i + 1]:
#             return True
#     return False
#
# print(double_string(s = input("enter:")))

# s = "suneel"
# items = any([a == b for a,b in zip(s,s[1:])])
# print(items)

#
# def add_dots(s):
#     c = ""
#     for i in s:
#
#         if i in s:
#             c += i +"."
#
#     return c[:-1]
# def remove_dots(s):
#     c = ""
#     for i in s:
#         if i!= ".":
#             c +=i
#     return c
#
# print(remove_dots(add_dots("sunel")))


# def count_(s):
#     l = []
#     for i in s.split("-"):
#         l.append(i)
#         for j in l:
#             if j == "":
#                 l.remove(j)
#     print(len(l))
# s1 = input("enter:")
# (count_(s1))


# def anagram(s,s1):
#     if sorted(s) == sorted(s1):
#         return True
#     else:
#         return False
# print(anagram("abcd","dabe"))


# def flatten(l):
#     l1 = []
#     for i in l:
#         for j in i:
#             l1.append(j)
#     return l1
# print(flatten([[1,2],[3,4]]))

#
# l = [5,8,9,0,-1,-8,-30,10]
# l1 = []
# for i in range(len(l)):
#     mnm = l[0]
#     for j in l:
#         if j < mnm:
#             mnm = j
#     l1.append(mnm)
#     l.remove(mnm)
# print(l1)


# def order_list(l):
#     lst = []
#     for i in range(len(l)):
#         mnm = l[0]
#         for j in l:
#             if j < mnm:
#                 mnm = j
#         lst.append(mnm),l.remove(mnm)
#
#     print(lst)
# lst1 = list(map(int,input("enter:").split(",")))
# (order_list(lst1))

#
# l = [5,8,9,0,-1,-8,-30,10]
# lst = []
# for i in range(len(l)):
#     mnm = l[0]
#     for j in l:
#         if j < mnm:
#             mnm = j
#     lst.append(mnm)
#     l.remove(mnm)
#
# print(lst)


# def f(a):
#     return a in a[::-1]
#
#
#
# print(f("aba"))
# print("a".split())


#
# def square(n):
#     s = n ** 0.5
#     return s **2 == n
# def fibonacci(n1):
#     return square(5*n1**2+4) or square(5*n1**2-4)
# n2 = int(input("enter number:"))
# if fibonacci(n2) == True:
#     print("the given number ",n2,"is fiboncci")
# else:
#     print("the given number",n2, "not fiboncci")
#
#
# def isperfectsquare(x):
#     s = x**0.5
#     return s**2 == x
# def isfibonacci(n):
#     return isperfectsquare(5*n**2+4) or isperfectsquare(5*n**2-4)
# n1 = int(input("enter number:"))
# if isfibonacci(n1) == True:
#     print(n1," is a fibonacci number")
# else:
#     print(n1," is not a fibonacci number")


#
# def fac(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fac(n - 1)
#
# def strong(n1):
#     s = str(n1)
#     sum = 0
#     for i in range(len(s)):
#         sum += (fac(int(s[i])))
#     if sum == n1:
#         print("it is a strong number")
#     else:
#         print("it is not strong number")
# strong(145)

# l = [1,2,3,4,5,6,7,8,9]
# largest = l[0]
# scnd_largest = l[0]
# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
# for j in range(len(l)):
#     if l[j] > scnd_largest and l[j] != largest:
#         scnd_largest = l[j]
# print(scnd_largest)


# import random
# def func():
#
#     a = random.randrange(1,101)
#     return (a)
# print(func())


# def sort_by_frequency(arr):
#     res = dict()
#     for i in arr:
#         c = 0
#         for j in arr:
#             if i == j:
#                 c+= 1
#         res[i]=arr
#     return res
#
# s = (sort_by_frequency([0,1,8,1,7,1,9,1,2,2,6,2,6,0,1,2,3,5,1]))
#
# l = []
# for i,j in s.items():
#     l.append(str(i)*j)
#
# h = sorted(l,key=len,reverse=True)
# print(h)
# o = []
# for i in h:
#     o.extend(list(i))
# print(o)
# out_list = [int(i) for i in o]
# print(out_list)


#
# class Student:
#     count = 0
#
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#         Student.count +=1
#
#     def show(self):
#         print(self.name + " got "+ self.marks)
#     @classmethod
#     def get(cls):
#          return cls.count
#
# s = Student("suneel", "40")
# # s1 = Student("anil","50")
# s.show()
# print(Student.get())


# hours = int(input("enter :"))
# seconds = 60
# min = 60
# print(hours*seconds*min)

# a = [1,2,3,4]
# b = [5,6,7,8]
# l = []
# for i in a,b:
#     for j in i:
#         l.append(j)
#     # for j in b:
#     #     l.append(j)
# print(l)

#
# s = "sunel"
# if len(s)%2==0:
#     print(s[len(s)//2])

# def get(s):
#     for i in range(len(s)):
#         return s[len(s)//2-1]
# print(get("suniil"))

# def difference(l):
#
#     large = l[0]
#     small = l[0]
#     for i in range(len(l)):
#         if l[i] > large:
#             large = l[i]
#     for j in range(len(l)):
#         if l[j] < small:
#             small = l[j]
#     return(large-small)
# print(difference([2,5,4,1,7,3]))


# def inverse_chr(s):
#     if s.isupper():
#         return ((ord(s)-65)%26+97)
#     else:
#         return ((ord(s)-97)%26+65)
# print(inverse_chr("c"))


# import operator
#
# def calculator(n1,opr,n2):
#     l = [n1,opr,n2]
#     opr1 = {"+": operator.add}
#     return opr1[opr](n1,n2)
#
#
# print(calculator(4,"+",5))

# def cricket(wins, draws, losses):
#         return wins * 2 + draws * 1 + losses * 0
#
#
# print(cricket(5, 3, 4))

#
# def curzon(n):
#     first_num = (2**n + 1)
#     scnd_num = (2*n+1)
#     if first_num % scnd_num == 0:
#         print("the given number is curzon")
#     else:
#         print("the given number is not curzon")
# curzon(5)


# l1 = [1,4,7,8,9]
# l2 = [1,4,7,8,9]
# print(l1 is l2)
#
# @classmethod
# @staticmethod
# @property


# s = "sunl"
# for i in range(len(s.split())):
#     print(s[len(s)//2-1])

# def sorting(l):
#     dic = dict()
#     l1 = []
#     for i in l:
#         y = len(i)
#         z = sorted(y)
#         l1.append(z)
#         print(l1)
#         for j in range(len(i)):
#             dic[j] = l.count(j)
#     print(dic)
# sorting(['aa','bbbb','c','ddd'])

# def sorting(l):
#     l1 = []
#     d = dict()
#     for i in range(len(l)):
#         for j in range(len(l[i])):
#             d[j] = i.count(j)
#     print(d)
# sorting(['aa','bbbb','c','ddd'])

# def sorting(l):
#     l.sort(key = len,reverse=True)
#     return l
# print(sorting(['aa','bbbb','c','ddd']))


# def my(n):
#     return abs(n - 50)
#
# l1 = [100, 53, 83, 54]
# l1.sort(key=my)
# print(l1)




