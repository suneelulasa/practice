# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#
# between 2000 and 3200 (both included).
#
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#

# l = []
# for i in range(2000,3201):
#     if i%7==0 and i%5!=0:
#         l.append(str(i))
# print(",".join(l))


# Write a program which can compute the factorial of a given numbers.
#
# The results should be printed in a comma-separated sequence on a single line.
#
# Suppose the following input is supplied to the program:
# input:-8
# output:-40320

# def fact(x):
#     if x == 0:
#         return 1
#     else:
#         y = x * fact(x - 1)
#     return y
#
#
# z = int(input("enter number"))
# print(fact(z))


# With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
# such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# input:-8
# output:-{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


# n = int(input("enter number :"))
# di = dict()
# for i in range(1,n+1):
#     di[i] = i*i
# print(di)


# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# input:-34,67,55,33,12,98
# output:-
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')


# n = input("enter sequence :")
# x = n.split(",")
# print(list(x))
# print(tuple(x))


# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.


# class Show:
#     def __init__(self):
#         self.name = ""
#
#     def get_string(self):
#         self.name = input("enter a string")
#
#     def to_upcase(self):
#         print(self.name.upper())
#
#
# a = Show()
# a.get_string()
# a.to_upcase()


# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# input:-100,150,180
# output:-18,22,24

# c = 50
# h = 30
# l = []
# items = [i for i in (input("enter values :").split(","))]
# # print(items)
# for d in items:
#     l.append(str(int(round((2*c*int(d))/h)**0.5)))
# print(",".join(l))


# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# input:-3,5
# output:-[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]


# items = [int(x) for x in input("enter :").split(",")]
# rownum = items[0]
# colnum = items[1]
# multilist = [[2 for col in range(colnum)] for row in range(rownum)]
# for col in range(colnum):
#     for row in range(rownum):
#         multilist[row][col] = row * col
# print(multilist)


# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated
# sequence after sorting them alphabetically.
# input: jhg,ghg,lkj,asd
# output:asd,ghg,jhg,lkj


# l = []
# s = input("enter a string :").split(",")
# for i in s:
#     l.append((i))
#     # l.sort()
# print(",".join(sorted(l)))


# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:


# l = []
# while True:
#     s = input("enter sequence :")
#     if s:
#         l.append(s.upper())
#     else:
#         break
# print(l)
# #
# l = []
# while True:
#     s = input("enter sequence :")
#     if s:
#         l.append(s.upper())
#     else:
#         break
# for i in l:
#     print(i)


# Write a program that accepts a sequence of whitespace separated words as input and
# prints the words after removing all duplicate words and sorting them alphanumerically.
# input:-hand kamal kumar hand jacky loky kamal
# output:-hand jacky kamal kumar loky


# s = input("enter sequence :")
# w = [i for i in s.split(" ")]
# print(w)
# print(" ".join(sorted(list(set(w)))))


# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether
# they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.


# n = input("enter number")
# l = []
# x = [j for j in n.split(",")]
# for i in x:
#     p = int(i,2)
#     if p%5==0:
#         l.append(i)
# print(" ".join(l))


# Write a program, which will find all such numbers between 1000 and 3000
# (both included) such that each digit of the number is an even number.

# l = []
# for i in range(1000,3001):
#     s = str(i)
#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
#         l.append(s)
# print(" ".join(l))


# Write a program that accepts a sentence and calculate the number of letters and digits.


# s = input("enter string")
# alphabates = 0
# number = 0
# for i in s:
#     if i.isalpha():
#         alphabates += 1
#     elif i.isdigit():
#         number += 1
# print(alphabates,number)


# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.


# s = input("enter sequence :")
# upper = 0
# lower = 0
# for i in s:
#     if i.isupper():
#         upper += 1
#     elif i.islower():
#         lower += 1
# print("uppercase",upper,"lowercase",lower)


# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# input:-9
# output:-11106

# n = input("enter a value :")
# n1 = n*1
# n2 = n*2
# n3 = n*3
# n4 = n*4
# total = int(n1)+int(n2)+int(n3)+int(n4)
# print(total)
#
# n = input("value :")
# c = 0
# for i in range(1,5):
#     a = n*i
#     c = c+int(a)
# print(c)


# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# input:-1,2,3,4,5,6,7,8,9
# output:-1,9,25,49,81


# lst = input("enter value :")
# x = [str(int(i)**2)for i in lst.split(",") if int(i)%2!=0]
# print(",".join(x))


# Write a program that computes the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as following:
# D 100
# W 200


# transaction = 0
# while True:
#     s = input("give transaction :")
#     if s:
#         v = s.split(" ")
#         operation = v[0]
#         amount = int(v[1])
#         if operation == "D":
#             transaction += amount
#         elif operation == "W":
#             transaction -= amount
#     else:
#         break
# print(transaction)


# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
# Passwords that match the criteria are to be printed, each separated by a comma.
# input:-ABd1234@1,a F1#,2w3E*,2We3345


# import re
# l = []
# items = [x for x in input("enter here :").split(",")]
# for p in items:
#     if len(p)<6 or len(p)>12:
#         continue
#     else:
#         pass
#     if not re.search("[\w]+",p):
#         continue
#     elif not re.search("[$#@]+",p):
#         continue
#     elif re.search("[\s]+",p):
#         continue
#     else:
#         pass
#     l.append(p)
# print(",".join(l))

#
# import re
#
# l = []
# values = [x for x in input("enter here :").split(",")]
# for p in values:
#     if len(p)>=6 and len(p)<=12:
#         print("it is in suficiant length")
#     else:
#         continue
#     if re.search("[\w]+",p):
#         print("it has all characters")
#     elif re.search("[$#@]",p):
#         print("you entered the simbol also")
#     elif re.search("[\s]",p):
#         continue
#     else:
#         break
#     values.append(p)
# print("it is in  right formate :",l)


# You are required to write a program to sort the (name, age, height) tuples by ascending order
# where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# input:-
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85

# from operator import itemgetter
#
# l = []
# while True:
#     s = input("enter here :")
#     if s:
#         l.append(tuple(s.split(",")))
#     else:
#         break
# print(sorted(l, key=itemgetter(2)))


# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

# def Iterate(n):
#     i = 0
#     while i < n:
#         j = i
#         i += 1
#         if j % 7 == 0:
#             yield j
#
#
# n1 = int(input("enter number"))
# for i in Iterate(n1):
#     print(i)
#


# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT
# with a given steps. The trace of robot movement is shown as the following:

# The numbers after the direction are steps. Please write a program to compute the distance from current position
# after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# input:-
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
#
#
# p = [0,0]
# while True:
#     s = input("give the direction :")
#     if s:
#         values = s.split(" ")
#         directions = values[0]
#         steps = int(values[1])
#         if directions == "up":
#             p[0] += steps
#             print(p,'here 1')
#         elif directions == "down":
#             p[0] -= steps
#             print(p)
#         elif directions == "left":
#             p[1] -= steps
#             print(p)
#         elif directions == "right":
#             p[1] += steps
#             print(p)
#         else:
#             pass
#     else:
#         break
# print(int(round(((p[0])**2+(p[1])**2)**0.5)))


# Write a method which can calculate square value of number

# def Square(n):
#     return n ** 2
#
#
# n1 = int(input("enter"))
# re = Square(n1)
# print(re)
#

# PleasewriteaprogramtoprintsomePythonbuilt - in functionsdocuments, such as abs(), int(), raw_input()


# print(input.__doc__)

# def square(n):
#     c = n**2
#     return c
#
#
# re = square(5)
# print(re.__doc__)


# class person:
#     name = "person"
#
#     def __init__(self,name=None):
#         self.name = name
#
#
# person1 = person("anil")
# print(person.name, person1.name)
# person2 = person()
# person2.name = "sudheer"
# print("%s name is %s" % (person.name, person2.name))


# class Person:
#     # Define the class parameter "name"
#
#     name = "Person"
#
#     def __init__(self, name=None):
#         # self.name is the instance parameter
#
#         self.name = name
#
#
# jeffrey = Person("Jeffrey")
#
# print("%s name is %s" % (Person.name, jeffrey.name))
#
# nico = Person()
#
# nico.name = "Nico"
#
# print("%s name is %s" % (Person.name, nico.name))
#


# Define a function which can compute the sum of two numbers.

# def add(x,y):
#     c = x+y
#     return c
#
#
# re = add(5,6)
# print(re)


# Define a function that can convert a integer into a string and print it in console.

# def convert(number):
#     return str(number)
# re = convert(5)
# print(type(re))
# print(re)


# Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.


# def recive(x,y):
#     c = int(x)+int(y)
#     return c
# x1 = input("enter here :")
# y1 = input("enter here also :")
# re = recive(x1,y1)
# print(re)
# print(type(x1))
# print(type(y1))


# Define a function that can accept two strings as input and print the string with maximum length in console.
# If two strings have the same length, then the function should print al l strings line by line.

# def accept(s1,s2):
#     if len(s1)>len(s2):
#         print(s1)
#     elif len(s2)>len(s1):
#         print(s2)
#     else:
#         print(s1, '\n', s2)
# s = input("enter first string :")
# S = input("enter second string :")
# accept(s,S)


# Define a function that can accept an integer number as input and print the "It is an even number"
# if the number is even, otherwise print "It is an odd number".


# def check(n):
#     if n%2 == 0:
#         print("it is an even number")
#     else:
#         print("it is an odd number")
# n1 = int(input("enter a value :"))
# check(n1)


# Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.


# def myfunction():
#     di = dict()
#     for i in range(1,4):
#         di[i] = i**2
#     print(di)
# myfunction()


# Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.


# def printdictionary():
#     di = dict()
#     for i in range(1,21):
#         di[i] = i**2
#     print(di)
# printdictionary()


# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and
# the values are square of keys. The function should just print the values only.


# def printdict():
#     di = dict()
#     for i in range(1,21):
#         di[i] = i**2
#     for values in di.values():
#         print(values)
# printdict()


# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and
# the values are square of keys. The function should just print the keys only.

#
# def printdict():
#     di = dict()
#     for i in range(1,21):
#         di[i] = i**2
#     for key in di.keys():
#         print(key)
# printdict()


# Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).


# def printlist():
#     l = []
#     for i in range(1,21):
#         l.append(i**2)
#     print(l)
# printlist()


# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print the first 5 elements in the list.


# def listgenrtr():
#     l = []
#     for i in range(1,21):
#         l.append(i**2)
#     print(l[0:5])
#
#
# listgenrtr()


# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print the last 5 elements in the list.


# def generatelst():
#     l = []
#     for i in range(1,21):
#         l.append(i**2)
#     print(l[-5:])
#
#
# generatelst()


# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print all values except the first 5 elements in the list.


# def printlist():
#     l = []
#     for i in range(1,21):
#         l.append(i**2)
#     print(l[5:])
#
#
# printlist()


# Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).


# def myfunction():
#     l = []
#     for i in range(1,21):
#         l.append(i**2)
#     print(tuple(l))
#
#
# myfunction()


# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.


# tuple_1 = (1,2,3,4,5,6,7,8,9,10)
# print(tuple_1[:5])
# print((tuple_1[5:]))


# Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).


# tuple_1 = (1,2,3,4,5,6,7,8,9,10)
# l = []
# for i in (tuple_1):
#     if i%2 == 0:
#         l.append(i)
# print(tuple(l))


# Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".


# s = input("enter the string :")
# if s == "yes" or s == "Yes" or s == "YES":
#     print("yes")
# else:
#     print("no")


# Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].


# number = [1,2,3,4,5,6,7,8,9,10]
#
# even_numbers = filter(lambda x: x % 2 == 0, number)
# print(even_numbers)
#
#
# # Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
#
#
# lst = [1,2,3,4,5,6,7,8,9,10]
# square = list(map(lambda x: x**2,lst))
# print(square)
#
#
# tup= (5, 7, 22, 97, 54, 62, 77, 23, 73, 61)
# newtuple = tuple(map(lambda x: x+3 , tup))
# print(newtuple)

# Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].


# lst = [1,2,3,4,5,6,7,8,9,10]
# even_numbers = map(lambda x: x**2, (filter(lambda x: x%2 == 0, lst)))
# print(even_numbers)


# Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).


# lst = filter(lambda x: x%2 == 0, range(1,21))
# print(lst)


# Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).


# lst = map(lambda x: x**2,range(1,21))
# print(lst)
#


# Define a class named American which has a static method called printNationality.


# class American(object):
#
#     @staticmethod
#     def printNationality():
#         print("america")
#
#
# an_american = American()
# an_american.printNationality()
# American.printNationality()


# Define a class named American and its subclass NewYorker.


# class American:
#     pass
#
#
# class Newyork(American):
#     pass
#
#
# anAmerican = American()
# anNewyork = Newyork()
# print(anAmerican)
# print(anNewyork)


# Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.


# class Class:
#
#     def __init__(self,radius):
#         self.radius = radius
#
#     def area(self):
#         print((self.radius**2)*3.14)
#
#
# a = Class(2)
# a.area()


# import re
# l = []
# items = [x for x in input("enter here :").split(",")]
# for p in items:
#     if len(p)<6 or len(p)>12:
#         continue
#     else:
#         pass
#     if not re.search("[\w]+",p):
#         continue
#     elif not re.search("[$#@]+",p):
#         continue
#     elif re.search("[\s]+",p):
#         continue
#     else:
#         pass
#     l.append(p)
# print(",".join(l))
# ABd1234@1,a F1#,2w3E*,2We3345

#
# import re
#
# try:
#     l = []
#     items = [x for x in input("enter here :").split(",")]
#     print(items)
#     for p in items:
#         if len(p) < 6 or len(p) > 12:
#             continue
#         elif not re.search("[\w]+", p):
#             continue
#         elif not re.search("[#$@]+", p):
#             continue
#         elif re.search("[/s]+", p):
#             continue
#         else:
#            pass
#         l.append(p)
#     print(l)
# except ValueError:
#     print("At least 1 letter between [a-z],"
#           " At least 1 number between [0-9]"
#           "At least 1 letter between [A-Z]"
#           " At least 1 character from [$#@]"
#           "Minimum length of transaction password: 6"
#           "Maximum length of transaction password: 12")
# else:
#     print("It is in right formate")
# finally:
#     print("Thanks for visit the site")

# ABd1234@1,a F1#,2w3E*,2We3345

# import re
#
# value = []
#
# items=[x for x in input("enter").split(',')]
#
# for p in items:
#
#     if len(p)<6 or len(p)>12:
#
#         continue
#
#     else:
#
#         pass
#
#     if not re.search("[a-z]",p):
#
#         continue
#
#     elif not re.search("[0-9]",p):
#
#         continue
#
#     elif not re.search("[A-Z]",p):
#
#         continue
#
#     elif not re.search("[$#@]",p):
#
#         continue
#
#     elif re.search("\s",p):
#
#         continue
#
#     else:
#
#         pass
#
#     value.append(p)
#
# print(",".join(value))


# def check(year):
#     return ((year%4 == 0) and (year%100 != 0) or (year%400 == 0))
# year1 = 2100
# if(check(year1)):
#     print("it is a leap year")
# else:
#     print("it is not a leap year")


# year = int(input("enter year :"))
# if ((year%4 == 0) and (year%100 != 0)) or (year%400 == 0):
#     print("it is leap year")
# else:
#     print("it is not a leap year")


# it is password validation program in exception handling

# import re
# try:
#     p = input("enter :")
#     if not len(p)>=6 and len(p)<=12:
#         raise Exception("length of characters not sufficient ")
#     elif not re.search("[a-z]",p):
#         raise Exception("there is no lower case letter ")
#     elif not re.search("[A-Z]",p):
#         raise Exception("there is no upper case letter ")
#     elif not re.search("[@#$]",p):
#         raise Exception("there is no special character ")
#     elif  re.search("\s",p):
#         raise Exception("space not allowed ")
#     else:
#         pass
# except Exception as error:
#     print('Caught this error: ' + repr(error))
# else:
#     print("it is in good format")
# finally:
#     print("thanks for visit the site")


# Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.


# class Rectangle:
#
#     def __init__(self, length, width):
#         self.length = length
#         self.widht = width
#
#     def area(self):
#         print(self.length * self.widht)
#
#
# a = Rectangle(2,10)
# a.area()


# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.


# class Shape:
#
#     def __init__(self,length):
#         pass
#
#     def area(self):
#         return 0
#
# class Square:
#
#     def __init__(self,length):
#         self.length = length
#         # super().__init__()
#
#     def area(self):
#         return self.length * self.length
#
#
# a = Square(3)
# print(a.area())


# class Shape(object):
#
#     def __init__(self):
#
#         pass
#
#
#
#     def area(self):
#
#         return 0
#
#
#
# class Square(Shape):
#
#     def __init__(self, l):
#
#         Shape.__init__(self)
#
#
#         self.length = l
#         super().__init__()
#
#
#
#     def area(self):
#
#         return self.length*self.length
#
#
#
# aSquare= Square(3)
#
# print(aSquare.area())


# Please raise a RuntimeError exception.

# a = int(input("enter a value :"))
# b = int(input("enter b value :"))
# try:
#     c = a/b
#     print(c)
# except ZeroDivisionError as error:
#     print("this is the" + repr(error))
#
# else:
#     print("there is no error")
# finally:
#     print("it is a good program")


# Define a custom exception class which takes a string message as attribute.


# class error(Exception):
#     def show(self,msg):
#         self.msg = msg
#
#
# attri = error("something wrong")
# print(attri)


# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the
# user name of a given email address. Both user names and company names are composed of letters only.


# import re
# email = input("enter the email :")
# res = re.match("(\w+)@((\w+\.)+(com))",email)
# print(res.group(2))


# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to
# print the company name of a given email address. Both user names and company names are composed of letters only.


# import re
# email = input("enter email :")
# res = re.match("(\w+)@(\w+\.+com)",email)
# print(res.group(2))


# Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.


# words = input("enter words :")
# l = []
# items = [x for x in words.split(" ")]
# for word in items:
#     if word.isdigit():
#         l.append(word)
# print(l)
#


# BY USING REGULAR EXPRESSIONS
# import re
# words = input("enter words :")
# digt = re.findall("\d+",words)
# print(digt)


# Print a unicode string "hello world".


# unicd = u"suneel"
# print(type(unicd))


# Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.


# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

# n = int(input("enter the number :"))
# s = 0.0
# for i in range(1,n+1):
#     s += (i)/(i+1)
# print(round(s,2))


# Write a program to compute:
# f(n)=f(n-1)+100 when n>0
# and f(0)=1


# def function(n):
#     if n == 0:
#         return 0
#     else:
#         return function(n-1) + 100
#
#
# n1 = int(input("enter n :"))
# res = function(n1)
# print(res)


# The Fibonacci Sequence is computed based on the following formula:
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1


# def function(n):
#     if n == 0:
#         return 0
#
#     elif n == 1:
#         return 1
#     else:
#         return function(n-1) + function(n-2)
#
#
# n1 = int(input("enter n :"))
# res = function(n1)
# print(res)

# 0,1,2,3,5,8,13


# Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.


# def function(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return function(n-1) + function(n-2)
#
#
# n1 = int(input("enter n :"))
# values = [str(function(n1)) for n1 in range(0,n1+1)]
# print(",".join(values))


# Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.


# def even(n):
#     i = 0
#     while i <= n:
#         if i % 2 == 0:
#             yield i
#         i += 1
#
#
# n1 = int(input("enter n :"))
# l = []
# for j in even(n1):
#     l.append(str(j))
# print(",".join(l))


# Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n
# in comma separated form while n is input by console.


# def even(n):
#     i = 0
#     while i<=n:
#         if i%5 == 0 and i%7 == 0:
#             yield i
#         i += 1
#
#
# n1 = int(input("enter n value :"))
# l = []
# for j in even(n1):
#     l.append(str(j))
# print(",".join(l))


# Please write assert statements to verify that every number in the list [2,4,6,8] is even.


# l = [2, 4, 6, 8, 12]
# for i in l:
#     assert i%2 == 0
# print(l)


# x = input("enter:")
#
# print(eval(x))


# Please write a binary search function which searches an item in a sorted list. The function should return
# the index of element to be searched in the list.


# import math
#
# def bin_search(li, element):
#
#     bottom = 0
#
#     top = len(li)-1
#
#     index = -1
#
#     while top>=bottom and index==-1:
#
#         mid = int(math.floor((top+bottom)/2.0))
#
#         if li[mid]==element:
#
#             index = mid
#
#         elif li[mid]>element:
#
#             top = mid-1
#
#         else:
#
#             bottom = mid+1
#
#
#
#     return index
#
#
#
# li=[2,5,7,9,11,17,222]
#
# print(bin_search(li,11))
#
# print(bin_search(li,12))


# Please generate a random float where the value is between 10 and 100 using Python math module.


# import random
#
# x = random.random()*100
# print(x)


# Please generate a random float where the value is between 5 and 95 using Python math module.

# import random
#
# x = random.random()*100 -5
# print(x)


# Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.


# import random
#
# x = int(input("enter x :"))
# y = random.choice([i for i in range(1,x+1) if i%2 == 0])
# print(y)


# Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive using random module
# and list comprehension.


# import random
# n = int(input("enter n :"))
# x = random.choice([i for i in range(1,n+1) if i%5 == 0 and i%7 == 0])
# print(x)


# Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.


# import random
#
# x = random.sample(range(100),5)
# print(x)


# Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.


# import random
# x = random.sample([i for i in range(100,200) if i%2 == 0],5)
# print(x)


# Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.

# import random
# x = random.sample([i for i in range(1,1001) if i%5 == 0 and i%7 == 0],5)
# print(x)


# Please write a program to randomly print a integer number between 7 and 15 inclusive.


# import random
# x = random.randrange(7,15)
# print(x)


# Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".


# import zlib
#
# s = b'suneel'
# t = zlib.compress(s)
# print((t))
# print(zlib.decompress(t))

# BY USING THE ZLIB WE KNOW THE BYTES OF THE STRING


# Please write a program to print the running time of execution of "1+1" for 100 times.


# from timeit import Timer
#
# x = Timer("for i in range(100):2+5")
# print(x.timeit())


# Please write a program to print the running time of execution of "1+1" for 100 times.


# from random import shuffle
#
# x = [22, 5, 6, 8, 5, 23]
# shuffle(x)
#
# print(x)
#


# Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"]
# and the object is in ["Hockey","Football"].


# person = ["I", "You"]
# like = ["Play", "Love"]
# game = ["Hockey","Football"]
#
# for i in range(len(person)):
#     for j in range(len(like)):
#         for k in range(len(game)):
#             print(person[i] + like[j] + game[k]  )


# Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].


# y = [5,6,77,45,22,12,24]
# items = [x for x in y if x%2!=0]
# print(items)


# By using list comprehension, please write a program to print the list after removing delete numbers
# which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

# li = [12,24,35,70,88,120,155]
# items = [x for x in li if x%5 != 0 and x%7 != 0]
# print(items)


# By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers
# in [12,24,35,70,88,120,155].


# li = [12,24,35,70,88,120,155]
#
# items = [x for i,x in enumerate(li) if i%2 != 0]
# print(items)


# By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.


# arry = [[[5 for x in range(8)]for y in range(2)]for z in range(3)]
# print(arry)


# By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in
# [12,24,35,70,88,120,155].


# li = [12,24,35,70,88,120,155]
# items = [x for (i,x) in enumerate(li) if i not in (0,4,5)]
# print(items)
#

# By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

# li = [12,24,35,24,88,120,155]
#
# items = [i for i in li if i != 24 ]
# print(items)
#
#
# for i in li:
#     if i == 24:
#         li.remove(i)
# print(li)


# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list
# whose elements are intersection of the above given lists.


# l1 = [1,3,6,78,35,155]
# l2 = [12,24,35,24,88,120,155]
#
# l = []
#
# for i in range(len(l1)):
#     c = 0
#     for j in range(len(l2)):
#         if l1[i] == l2[j]:
#             c +=l1[i]
#             l.append(c)
# print(l)
#
#
# set1=([1,3,6,78,35,155])
# s1 = set(set1)
#
# set2=([12,24,35,24,88,120,155])
# s2 = set(set2)
#
# s1 &= s2
#
# li=list(s1)
#
# print (li)


# With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all
# duplicate values with original order reserved.


# li = [12,24,35,24,88,120,155,88,120,155]
# s = set(li)
# print(sorted(s))


# def removel(li):
#     l = []
#     for i in li:
#         l.append(i)
#     return l
#
# li1 = [12,24,35,24,88,120,155,88,120,155]
# print(sorted(set(removel(li1))))


# Define a class Person and its two child classes: Male and Female. All classes have a method "getGender"
# which can print "Male" for Male class and "Female" for Female class.


# class Person:
#     def getGender(self):
#         pass
#
#
# class Male(Person):
#     def getGender(self):
#         print("male")
#
#
# class Female(Person):
#     def getGender(self):
#         print("female")
#
#
# a = Male()
# b = Female()
# a.getGender()
# b.getGender()


# Please write a program which count and print the numbers of each character in a string input by console.


# s = input("enter s :")
#
# t = list(set(s))
#
# for i in (t):
#     c = 0
#     for j in s:
#         if i == j:
#             c +=1
#     if c>1:
#
#         print(i,str(c))

# IT IS IN DICTIONARY FORMATE

# s = input("enter s:")
# di = dict()
# for i in s:
#     v = s.count(i)
#     di[i] = v
# print(di)


# Please write a program which accepts a string from console and print it in reverse order.


# s = input("enter string :")
# v = ""
# for i in s:
#     v = i+v
# print("".join(v))


# s = input("enter string :")
# print(s[::-1])


# Please write a program which accepts a string from console and print the characters that have even indexes.

# s = input("enter s :")
# print(s[::2])


# create a dictionary with list and tuple:


# li = [("suneel",5), ("anil",6), ("suman",2), ("sudheer",9)]
#
# y = dict(li)
# print(y)


# def trance(tup,di):
#     for i,j in tup:
#         di.setdefault(i,[] ).append(j)
#     return di
#
#
# tup1 = [("suneel",5), ("anil",6), ("suman",2), ("sudheer",9)]
# di1 = {}
# y = trance(tup1,di1)
# print(y)


# import random
# c = random.random()
# print(c)


# DATETIME  module

# from datetime import date
# from datetime import timedelta
# begining_date = date.today()
# enddate = begining_date + timedelta(days= 45)
# print("begindate:",begining_date)
# print("enddate:",enddate)


# FINDING THE SECOND LARGEST NUMBER IN THE LIST:-

# def find(list1):
#     scndlargest = list1[0]
#     largest = list1[0]
#     for i in range(len(list1)):
#         if list1[i] > largest:
#             largest = list1[i]
#         elif list1[i] > scndlargest and list1[i] != largest:
#             scndlargest = list1[i]
#     return scndlargest
#
#
# print(find([10, 20, 80, 1, 65, 30, 87, 90]))



# li = [1,2,3,4,5,6,7,8,9]
# largest = li[0]
# scndlargest = li[0]
# for i in range(len(li)):
#     if li[i] > largest:
#         largest = li[i]
#     elif li[i] > scndlargest and li[i] != largest:
#         scndlargest = li[i]
# print(scndlargest)
# li.sort()
# print(li[-2])




# PROGRAM FOR FINDING THE STRONG NUMBER:-



# PROGRAM FOR AMSTRONG NUMBER :-
# IN FOR LOOP:-
# n = input("enter number:")
# s = 0
# for i in n:
#     s += int(i)**len(n)
# if s == n:
#     print("it is amstrong number")
# else:
#     print("it is not a amstrong")
#

# 5 * R * R + 4

# PROGRAM FOR KNOW THE NUMBER IS FIBONACCI OR NOT :-

# n = int(input("enter a value:"))
# if (5*n**2+4) == n or (5*n**2-4) == n:
#     print("the given number ",n,"is fibonacci")
# else:
#     print("the given number ",n," is not fibonacci")



# A PROGRAM FOR PLAYING CRICKET:-

# import random
# print("here comes for the toss")
# toss = input("choose head or tail:").lower()
# random_toss = random.randint(1,2)
# random_opt = random.randint(1,2)
# u_opt = 0
# c_opt = 0
#
# if random_toss == 1 and toss == "head":
#     print("you won the toss")
#     u_opt = (input("choose bat or ball :"))
# elif random_toss == 2 and toss == "tail":
#     print("you won the toss :")
#     u_opt = input("choose bat or ball :")
# else:
#     print("you loss the toss")
#
#     if random_opt == 1:
#         c_opt = "bat"
#         print("computer choose :",c_opt)
#     elif random_opt == 2:
#         c_opt = "ball"
#         print("computer choose",c_opt)
#
# print("FIRST INNINGS START")
#
# runs_1 = 0
# wickets_1 = 0
# balls_1 = 0
# while  wickets_1 !=2 and balls_1 !=12:
#     u_choice = int(input("choose any number from 1 to 6:"))
#     c_choice = random.randint(1,6)
#
#     if u_choice < 1 or u_choice > 12:
#         print("please choose any number in 1 to 6")
#     else:
#         print("your choice is :",u_choice,"computer choice is :",c_choice)
#
#         if u_choice == c_choice:
#             wickets_1 +=1
#         else:
#             if u_opt == "bat" or c_opt == "ball":
#                 bat_first = "you"
#                 ball_first = "computer"
#                 runs_1 += u_choice
#             elif u_opt == "ball" or c_opt == "bat":
#                 bat_first = "computer"
#                 ball_first = "you"
#                 runs_1 += c_choice
#         print("score:",runs_1,"/",wickets_1)
#         balls_1 += 1
#
#         if balls_1 == 6:
#             print("end of 1st over ")
#         elif balls_1 == 12:
#             print("end of 2nd over 2")
#         print("balls remaining :",12 -balls_1 )
#
# print("end of innings")
# print("final score:")
# print("runs=",runs_1)
# print("wickets=",wickets_1)
#
# print(ball_first,"needs",runs_1 + 1,"runs to win")
#
# print("second innings start")
#
# runs_2 = 0
# wickets_2 = 0
# balls_2 = 0
#
# while wickets_2 != 2 and balls_2 != 12 and runs_2 <= runs_1:
#     u_choice = int(input("choose any number in 1 to 6:"))
#     c_choice = random.randint(1,6)
#
#     if u_choice <1 or u_choice >12:
#         print("please choose any number between 1 to 6:")
#     else:
#         print("your choice=",u_choice,"computre choice=",c_choice)
#
#         if u_choice == c_choice:
#             wickets_2 +=1
#         else:
#
#             if bat_first == "computer":
#                 runs_2 += u_choice
#                 bat_second = "you"
#             elif  bat_first == "you":
#                 runs_2 += c_choice
#                 bat_second = "computer"
#         print("scores:",runs_2,"/",wickets_2)
#         balls_2 +=1
#
#         if balls_2 == 6:
#             print("end of 1st over")
#         elif balls_2 == 12:
#             print("end of 2nd over")
#
#         if runs_2 <= runs_1 and balls_2 <= 11 and wickets_2 != 2:
#             print("to win ", runs_2+1,"runs needed from ", balls_2,"balls")
#
# print("end of innings")
#
# print("final score:")
# print("runs=",runs_2)
# print("wickets=",wickets_2)
#
# print("--------------results------------")
# if runs_1 > runs_2:
#     if bat_first == "you":
#         print("congratulations you won the match by",runs_1 - runs_2,"runs")
#     else:
#         print("better luck next time, the computer won the match by",runs_1-runs_2)
# elif runs_2 > runs_1:
#     if bat_second == "you":
#         print("congratulations you won the match by",2 - wickets_2,"wickets")
#     else:
#         print("better luck next time, the computer won the match by" ,2 - wickets_2,"wickets")
# else:
#     print("the match is tie, no one wins ")




# PROGRAM FOR AMSTRONG:-
# IN FOR LOOP:-

# n = int(input("enter n:"))
# s = str(n)
# sum = 0
# for i in s:
#     sum +=int(i)**len(s)
# if sum == n:
#     print("it is an amstron number")
# else:
#     print("it is not an amstrong number")


# IN WHILE LOOP


# n = int(input("enter n:"))
# s = str(n)
# sum = 0
# i = 0
# while sum < n:
#     sum += int(s[i])**len(s)
#     i +=1
# if sum == n:
#     print("it is amstrong")
# else:
#     print("it is not an amstrong")
#


# PROGRAM FOR SQUARE EACH ELEMENT IN THE LIST BY USING THE MAP AND LAMBDA:-


# l = [1, 2, 3, 4, 5]
# square = list(map(lambda x: x**2,l))
# print(square)



# HOW TO KNOW HOW MANY TIMES THE ITEM REPEATE IN THE SET :-

# s = {1,22,4,5,9,8,1,2,5,7,6,1}
# l = list(s)
#
# counting = l.count(int(input("search here:")))
# print(counting)


#
# s = [1,22,4,5,9,8,1,2,5,7,6,1]
# t = list(set(s))
# for i in range(len(t)):
#     c = 0
#     for j in range(len(s)):
#         if t[i] ==s[j]:
#             c +=1
#     if c>1:
#         print(c)




# PROGRAM FOR MISSING NUMBER IN A LIST:-



# def missing(lst):
#     return sum(range(lst[0],lst[-1]+1)) - sum(lst)
#
#
# l = [1,2,3,4,5,7,8]
# print(missing(l))



# def ma(**kwargs):
#     for key,value in kwargs.items():
#         print("args:","%s == %s" % (key,value))
#
# ma(first="i",middle= "am",last="learner")


# def ma(**kwargs):
#     print("who is he",kwargs["last"])
#
# ma(first="suneel",middle= "is",last="learner")


# def ma():
#     return
# ma()



# li1 = [1,2,3,4,5]
# # l = str(li1)
# # li2 = [1,2,3,5]
#
# items = [x for (i,x) in enumerate(li1) if i not in (3,0) ]
# print(items)


# Square of all the elements in a list using lambda (inputfrom user)

# n = input("enter here :").split(",")
# l = int(n)
# square = list(map(lambda x: x**2, l))
# print(square)


# n1 = input("enter number").split(",")
# n = [n1]
# items = list(map(lambda x: int(x)**2,n))
# print(items)


# convert - 'ketha' -> ['k','e','t','h','a'] and
# convert ['k','e','t','h','a'] -> 'ketha'


# s = "ketha"
# l = []
# for i in range(len(s)):
#     l.append(s[i])
# print(l)


# import functools
# l1 = ['k','e','t','h','a']
# l = []
# y = functools.reduce(lambda a,b: a+b, l1)
# output = [str(x) for x in y ]
# print(output)



#  In how many ways u can achieve list2 from list1
# Input - li1 = [1,2,3,4,5]
# Output - li2 = [1,2,3,5]



# li1 = [1,2,3,4,5]

# output = [x for x in li1 if x != 4]
# print(output)

# del li1[3]
# print(li1)

# li1.pop(3)
# print(li1)

# li1.remove(4)
# print(li1)

# l = []
# for i in li1:
#     if i != 4:
#         l.append(i)
# print(l)


# x = [1,2,3,4,5]
# l = len(x)
# li = []
# i = 0
# while i < l:
#     if x[i] != 4:
#         li.append(x[i])
#     i += 1
# print(li,end=" ")



# List rotation problem

# li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# print("original list:",li)
#
# rotation_by_3 = li[3:] + li[:3]
# print("left rotation :",rotation_by_3)
# back_to_rotation = rotation_by_3[-3:] + rotation_by_3[:-3]
# print("right rotation :",back_to_rotation)

# from datetime import datetime
# date_time_obj = '04/03/22 02:15:11'
# date = datetime.strptime( date_time_obj, '%d/%m/%y %H:%M:%S')
# print(date)
#
# from datetime import datetime
#
# date_time_str = '18/09/19 01:55:19'
#
# date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')
# print(date_time_obj)



