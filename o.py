#
# # replace
# # st="python is awesome and python is easy"
# # st=st.replace("python","java")
# # print(st)
# #
# # st = "python is awesome and python is easy"
# # st=st.replace("python","umesh")
# # print(st)
#
# # st = "python is awesome and python is easy"
# # # st=st.replace("python","madhu")
# # # print(st)
# # st=st.replace("python","c++")
# # print(st)
# # # +
# # st = "python is awesome and python is easy"
# # # st=st.replace(" ","+")
# # # print(st)
# # # st=st.replace(" ","+")
# # # print(st)
# # st=st.replace(" "," and ")
# # print(st)
# # find
# # st = "python is awesome and python is easy"
# # # # print(st.find("y"))
# # # # print(st.find("o"))
# # # print(st.find("s"))
# # print(st.find("h"))
#
#  #capitalize 1st letter
#
# # st = "python is awesome and python is easy"
# # print(st.capitalize())
# #
# #count
#
# # st = "python is awesome and python is easy"
# # # print(st.count("python"))
# # # print(st.count("is"))
# # print(st.count("awesome"))
#
# # split and join
# # st = "python is awesome and python is easy"
# # print(st.split())
# # print("".join(st))
# #english
# # st="i didn\"t go"
# # print(st)
#
# # st = "python is awesome and python is easy"
# # print(st[::-1])
#
# #operators
#
# # a=5//2   # if we don't want to decimal value
# # print(a)
# # a=3  # out put want 6 or 9
# # print(a*2)
# # print(a**2)
#
# # assignment operators
# #20
# # a=10
# # a+=10
# # print(a)
# #0
# # a=10
# # a-=10
# # print(a)
# #20
# # a=10
# # a*=2
# # print(a)
# #comparision ==,!=,<,>,
# # a=10
# # b=20
# # if a==b:
# #     print(True)
# # else:
# #     print(False)
#
#
# # a=10
# # b=20
# # c=30
# #
# # if a>b and b<c:
# #     print(True)
# # else:
# #     print(False)
#
#
# # a=10
# # if a==10:
# #     print(a)
# # if a is 10:
# #     print(True)
# # else:
# #     print(False)
#
# # st="python"
# # for i in st:
# #     print("python"not in st)
#
# # st="good things take time"
# # print(st.split())
# # u=st.split()
# # # print(u)
# # for i in u:
# #     print(i.capitalize())
#
#         # even or odd ##if we divide any number with 2 if we will get 0 its even number if not odd number
#
# # number = int(input("enter a number:"))
# #
# # if number %2==0:
# #     print("is even number:".format(number))
# # else:
# #     print("is odd number:".format(number))
#
#
#       #prime or not
#
# # number = int(input("enter a number:"))
# # for i in range(2,number):
# #     if number%i==0:
# #         print("its not a prime ")
# #         break
# #     else:
# #         print("its prime ")
#
#
#
#
#
#
# #we have to enter alphabhabet then we have to store that in variable,then we have to check that alohabet is ovwel or not
# # we have to check both upper and lower case
#
#              #Ovwls and Consonents
#
# # a = input("enter the Alphabet:")
# # if a in ('a','e','i','o','u'):
# #     print(a,"is a vowel")
# # else:
# #     print(a,"is a consonent")
#
#
# # sqaure root
#
# # n=int(input("enter a no:"))
# # import math
# # print(math.sqrt(n))
#
#        #swap
# # a=10
# # b=20
# # temp=10  #10
# # a=b #20
# # b=temp #10
# # print("value of a {}".format(a))
# # print("value of b {}".format(b))
#
#
#
#
# n=int(input("enter a number:"))
#
# if n>1:
#     print("Its a positive ")
# else:
#     print("Its a Negative")
#
#
# l=["umesh",1,3,65,6,33,"python","java",2.1,3.5]
# # print(l)
# # print(l[4:9])
# # print(l[-1])
# # print(l[1:])
#
# l[4]:78
# print(l)



# s1={1,2,3,"ReleaseOwl",2.6,True,False}
# s1_to_list=list(s1)
# print(s1)
#
# index=s1_to_list.index(2.6)
# print(index)
#
# s1_to_list[index]=5.2
# print(set(s1_to_list))


# s1={1,2,3,"ReleaseOwl",2.6,True,False}

# for i in s:
#     print(i)
# if True in s:
#     print(True)
# else:
#     print(False)

# s.add("Correct")
# print(s)
# s2={1,2,3,4,5,6}
# s1.update(s2)
# print(s1)
# s1={1,2,3,"ReleaseOwl",2.6,True,False}
# s1.discard("ReleaseOwl")
# print(s1)


# def st(name):
#     print("my organisation name:" +str(name))
# name="ReleaseOwl"
# st(name)
                # dict

# def dic_values(d):
#     for i in d:
#         print(i)
#
# d={"name":"umesh",'Age':22,"phone":6302094028,"address":'hyd'}
# dic_values(d)
#
#                # SET
#
# def set_values(st):
#     for i in st:
#         print(i)
#
# st={1,2,3,"ReleaseOwl",True,False,2.6}
# set_values(st)


                 # tuple
# def tup_vales(t):
#     for i in t:
#         print(i)
#
# t=(1,2,3,"ReleaseOwl",True,False,2.6)
# tup_vales(t)
#
# import calendar
# year=2023
# month=2
# x=calendar.month(year,month)
# print(x)



# for i in range(1,101):
#     print(i)

# for i in range(1,100,2):
#     print(i)

# for i in range(2,100,2):
#     print(i)

# for i in range(2,101):
#     if i>1:
#         for k in range(2,i):
#             if i%k==0:
#                 break
#         else:
#             print(i)

# st="python is awesome and python is easy"
# a=st[1:4]
# print(a)

# st="python is awesome and python is easy"
# st=st.replace(" ","/")
# print(st)

# st="python is awesome and python is easy"
# st=st.replace("python","Umesh")
# print(st)

# st="python is awesome and python is easy"
# st=st.capitalize()
# print(st)

# st="python is awesome and python is easy"
# z=st.title()
# print(z)


# st="python is awesome and python is easy"
# st=st.find("h")
# print(st)


# st="python is awesome and python is easy"
# st=st.count("is")
# print(st)

# st="python is awesome and python is easy"
# st=st.split()
# print(st)
# print(" ".join(st))

# st="python is awesome and python is easy"
# st=st.title()
# print(st)


# st="i did\'t go"
# print(st)

# age=25
# marks=356
# st="i am 25 years old i got 356 marks"
# st="i am {} years old i got {} marks".format(age,marks)
# print(st)


# st="Releaseowl"
# print(st[::-1])
# print(st[::+1])



#
# st=input("enter a string:")
# reverse=st[::-1]
# if st==reverse:
#     print("its a palidroms")
# else:
#     print("its not a palidroms")


# n=int(input("enter a number:"))
# for i in range(1,n):
#     print(n,"*",i,"=",n*i)


# for i in range(1,101):
#     print(i)
#
# for i in range(1,100,2):
#     print(i)
#
# for i in range(2,100,2):
#     print(i)

# for i in range(2,101):
#     if i>1:
#         for k in range(2,i):
#             if i%k==0:
#                 break
#         else:
#             print(i)


# st="python is awesome and python is easy "
# a=st[1:4]
# print(a)

# st="python is awesome and python is easy "
# st=st.replace(" " ,'+')
# print(st)

# st="python is awesome and python is easy "
# st=st.replace("python","java")
# print(st)


# st="python is awesome and python is easy "
# st=st.find("o")
# print(st)


# st="python is awesome and python is easy "
# st=st.capitalize()
# print(st)

# st="python is awesome and python is easy "
# z=st.title()
# print(z)


# st="python is awesome and python is easy "
# st=st.split()
# print(st)
# print(" ".join(st))


# st="python is awesome and python is easy "
# z=st.title()
# print(z)



# st="i didn\'t go"
# print(st)

# age=30
# marks=666
# st="i am 30 years old , i got 666 marks"
# st="i am {} years old , i got {} marks".format(age,marks)
# print(st)


#
# st="Umesh"
# print(st[::-1])
# print(st[::+1])


# a=3
# print(a**2)


# st=input("enter a string:")
# reverse=st[::-1]
# if reverse==st:
#     print("its a palidroms")
# else:
#     print("its not a polidroms")



# n=int(input("enter a number:"))
# for i in range(1,n):
#     print(n,"*",i,"=",n*i)




# numbers=int(input("enter a number :"))
# if numbers%2==0:
#     print("its even number ".format(numbers))
# else:
#     print("its a odd number".format(numbers))


# number= int(input("enter a number:"))
# for i in range(2,number):
#     if number%i==0:
#         print("its not a prime number")
#         break
#     else:
#         print("its a prime number")


# A=input("enter a alphabet:")
# if A in ("a","e","i","o","u"):
#     print("its a vowel")
# else:
#     print("its consonent")

# n=int(input("enter a number:"))
# import math
# print(math.sqrt(n))

# year=int(input("enter the year:"))
# if year %4==0:
#     print("its a leap year")
# else:
#     print("its not a leap year")












#
# def prime():
#     for i in range(2, 101):
#         if i > 1:
#             for k in range(2, i):
#                 if i % k == 0:
#                     break
#             else:
#                 print(i)
# prime()


#
# def primornot(number):
#     number = int(input("enter a number:"))
#     for i in range(2, number):
#         if number % i == 0:
#             print("its not a prime ")
#             break
#         else:
#             print("its a prime ")
# number=int(input("enter a number:"))
# primornot(number)



# def pveornve(number):
#     n = int(input("enter a number:"))
#     if n > 1:
#         print("its a +ve")
#     else:
#         print("its a -ve")
# number=int(input("enter a number:"))
# pveornve(number)

# def leapornot(year):
#     year = int(input("enter a year:"))
#     if year % 4 == 0:
#         print("its a leap year")
#     else:
#         print("its not leap year")
# year=int(input("enter a year:"))
# leapornot(year)


# def eqt(number):
#     n = int(input("enter a number:"))
#     for i in range(1, n):
#         print(" " * (n - i) + i * " *")
# number=int(input("enter a number:"))
# eqt(number)


# number=6
# total=1
# while number >0:
#     total= total * number
#     number-=1
# print(total)



# def factorial(number):
#     number = 7
#     total = 1
#     while number > 0:
#         total = total * number
#         number -= 1
#     print(total)
# factorial(number)


# st=input("enter a string:")
# reverse=st[::-1]
# if st==reverse:
#     print('its a palidroms')
# else:
#     print("its not a palidroms")



# def paliornot(string):
#     st = input("enter a string:")
#     reverse = st[::-1]
#     if st == reverse:
#         print('its a palidroms')
#     else:
#         print("its not a palidroms")
# string=input("enter a string:")
# paliornot(string)


# a=input("enter the alphabet:")
# if a in ('a','e','i','o','u'):
#     print("its a vowel")
# else:
#     print("its a consonent")



# def vorc(zoom):
#     a = input("enter the alphabet:")
#     if a in ('a', 'e', 'i', 'o', 'u'):
#         print("its a vowel")
#     else:
#         print("its a consonent")
# zoom=input('enter the alphabet:')
# vorc(zoom)


# import calendar
# print(calendar.calendar(2023,2))


# for i in range(1,100):
    # print(i)

#
# for i in range(1,100,2):
#     print(i)


# for i in range(2,100,2):
#     print(i)



# for i in range(2,101):
#     if i>1:
#         for k in range(2,i):
#             if i%k==0:
#                 break
#         else:
#             print(i)


#
# st="python is awesome and python is easy"
# a=st[1:6]
# print(a)


# st="python is awesome and python is easy"
# st=st.replace(" "," + ")
# print(st)

# st="python is awesome and python is easy"
# st=st.find("h")
# print(st)

# st="python is awesome and python is easy"
# st=st.replace("python ","java")
# print(st)


# st="python is awesome and python is easy"
# st=st.capitalize()
# print(st)

# st="python is awesome and python is easy"
# st=st.count("is")
# print(st)



# st="python is awesome and python is easy"
# st=st.split()
# print(st)
# print(" ".join(st))

#
# st="python is awesome and python is easy"
# z=st.title()
# print(z)
# z=st.upper()
# print(z)
# z=st.lower()
# print(z)


# st="i didn\"t go"
# print(st)


# age=25
# marks =100
# st=" i am 35 years old, i got 100 marks"
# st="i am {} years old,i got {} marks".format(age,marks)
# print(st)

# st="ReleaseOwl"
# # st=st[::-1]
# # print(st)
# st=st[::+1]
# print(st)

# st=input("enter a string:")
# reverse=st[::-1]
# if st==reverse:
#     print("its a palidroms")
# else:
#     print("its not a palidroms")

# n=int(input("enter a number:"))
# for i in range(1,n):
#     print(n,"*",i,"=",n*i)

# number=int(input("enter a number :"))
# if number %2==0:
#     print("its a even no")
# else:
#     print("its a odd no")

# number = int(input("enter a number:"))
# for i in range(2,number):
#     if number %i==0:
#         print("its not prime no")
#         break
#     else:
#         print("its a prime no")



# a=input("enter a alphabet:")
# if a in ("a","e","i","o","u"):
#     print("its a vowel")
# else:
#     print("its a consonent")



#
# number=6
# total=1
# while number >0:
#     total = total * number
#     number -=1
# print(total)

# import math
# print(math.sqrt(360))


# year = int(input("enter a year :"))
# if year %4==0:
#     print("its a leap year ")
# else:
#     print("its not a leap year")

# n=int(input("enter a number :"))
# if n>1:
#     print("its a positive")
# else:
#     print("its a negative")


# n=int(input("enter a number:"))
# for i in range(1,n):
#     print(" "*(n-i)+i*" *")


# n=int(input("enter a number :"))
# if n%2==0:
#     print("its +ve")
# else:
#     print("its -ve")


# n=int(input("enter a number :"))
# for i in range(2,n):
#     if n%i==0:
#         print("its not prime")
#         break
#     else:
#         print("its prime")
#
# def primeornot():
#     for i in range(2,n):
#         if n%i==0:
#             print("its not a prime")
#             break
#         else:
#             print("its prime no")
# n=int(input("enter a number :"))
# primeornot()

# class primeornot:
#     def __init__(self,n):
#         self.n=n
#     def prornot(self):
#         for i in range(2,n):
#             if n%i==0:
#                 print("its not a prime")
#                 break
#             else:
#                 print("its a prime no")
# n=int(input("enter a number :"))
# obj=primeornot(n)
# obj.prornot()



# n=int(input("enter a number :"))
# import math
# print(math.sqrt(25))



# n=int(input("enter a number:"))
# total=1
# while n>0:
#     total=total*n
#     n-=1
# print(total)


# def factorial():
#     n = int(input("enter a number :"))
#     total = 1
#     while n>0:
#         total=total*n
#         n-=1
#     print(total)
# factorial()

# st=input("enter a string :")
# reverse=st[::-1]
# if st==reverse:
#     print("its a palidroms")
# else:
#     print("its not palidroms")


# l=[10,20,30,"ReleaseOwl",2.5,True,False,50]
# print(type(l))
# print(len(l))
# print(l[1:4])
# print(l[:8])
# print(l[0:])
# for i in l:
#     print(i)

# l=[1,2,12,3,4,5,6,77,78]
# for i in l:
#     print(i**2)

# l=[10,20,30,"ReleaseOwl",2.5,True,False,50]
# # l[2]="java"
# # print(l)
#
# l[0:5]=(55,2.2,'umesh',56)
# print(l)
#
# l=[10,20,30,"ReleaseOwl",2.5,True,False,50]
# # l.insert(5,"pawan kalyan")
# # print(l)
# l.append(500)
# print(l)


# import turtle
# t = turtle.Turtle()
# t.pensize(2)
# t.color('green')
# t.left(90)
# t.backward(100)
# t.speed(20)
# t.shape('turtle')
#
# def tree(i):
#     if i<10:
#         return
#     else:
#         t.forward(i)
#         t.color('red')
#         t.circle(2)
#         t.color("brown")
#         t.left(30)
#         tree(3*i/4)
#         t.right(60)
#         tree(3*i/4)
#         t.left(30)
#         t.backward(i)
#
# tree(100)
# turtle.done()


# Enter a string and then find the length of the string without using len.


# st="he is going to out side"
# var1=0
# for i in st:
#     var1=var1+1
# print(var1)

# for i in range(1,101,1):
#     print("hello world", end=" ")

# st=input("enter a string :")
# n=int(input("enter a number :"))
# print(st*n)

#
# n=int(input("enter a number :"))
# for i in range(1,n+1):
#     print(i)

# st="sds234of343gg4"
# alpha=0
# number=0
# numbers=["0","1","2","3","4","5","6","7","8","9"]
# for i in st:
#     if i in numbers:
#         number=number+1
#     else:
#         alpha=alpha+1
# print(number)
# print(alpha)


# for i in range(1,100,1):
#     print("hello world",end=" ")

# def hundred():
#     for i in range(1,101,1):
#         print("hello world",end=" ")
# hundred()

# class hundred:
#     def __init__(self):
#         pass
#     def handerd(self):
#         for i in range(1,101,1):
#             print("hello world",end=" ")
# obj=hundred()
# obj.handerd()



# n=int(input("enter a number :"))
# for i in range(1,n+1):
#     print(i,end=" ")


# def natural():
#     for i in range(1,n+1):
#         print(i,end=" ")
# n=int(input("enter a number :"))
# natural()


# class natural():
#     def __init__(self,n):
#         self.n= n
#     def nturl(self,):
#         for i in range(1,n+1):
#             print(i,end=" ")
# n=int(input(" enter a number :"))
# obj=natural(n)
# obj.nturl()





#1. Enter a string then count how many char's and how many int's
# eg: input : sds234of343gg4 output : chars : 7 and numbers : 7

# st="sds234of343gg4"
# int_count=0
# char_count=0
# for i in st:
#     if i.isdigit():
#         int_count += 1
#     else:
#         char_count += 1
# print(int_count)
# print(char_count)

# def countchandint():
#     st="sds234of343gg4"
#     int_count=0
#     char_count=0
#     for i in st:
#         if i.isdigit():
#             int_count +=1
#         else:
#             char_count +=1
#     print(int_count)
#     print(char_count)
# countchandint()


# class intorchar():
#     def __init__(self):
#         pass
#     def inorchars(self,st):
#         int_count=0
#         char_count=0
#         for i in st:
#             if i.isdigit():
#                 int_count+=1
#             else:
#                 char_count+=1
#         print(int_count)
#         print(char_count)
# st="sds234of343gg4"
# obj=intorchar()
# obj.inorchars(st)

#2. Enter a string and then find the length of the string without using len.


# st="he is going to out side"
# count=0
# for i in st:
#     count+=1
# print(count)


# def length():
#     st="he is going to out side"
#     count=0
#     for i in st:
#         count+=1
#     print(count)
# length()



# class Length():
#     def __init__(self,st):
#         self.st = st
#     def leng(self):
#         count=0
#         for i in st:
#            count+=1
#         print(count)
# st="he is going to out side"
# obj=Length(st)
# obj.leng()


#3. Enter a string and convert that string as big string as having length equal to 100
# (it should not less or greater than 100, should equals to 100) by increasing
# string by taking the reference of the user entered string(initial string which we have taken)
#eg: input : hello world, output : hello world hello world hello world hello world.......hello world
# = output string length should be equal to 100


# st=input("enter a string :")
# n=int(input("enter a number :"))
# print(st*n)



# def hundred():
#     st=input("enter a string :")
#     n=int(input("enter a number"))
#     print(st*n)
# hundred()


# class hundred():
#     def __init__(self,st,n):
#         self.st=st
#         self.n=n
#     def handred(self):
#         print(st * n)
# st=input("enter a string :")
# n=int(input("enter a number :"))
# obj=hundred(st,n)
# obj.handred()


#  4. pring infinite natural numbers
#
# number = 1
# while number >0:
#     number +=1
#     print(number)


# def infinatenatural():
#     number=1
#     while number>0:
#         number+=1
#         print(number)
# infinatenatural()

# class infintenactral():
#     def __init__(self):
#         pass
#     def infinatenatural(self,number):
#         while number > 0:
#             number += 1
#             print(number)
# number=1
# obj=infintenactral()
# obj.infinatenatural(number)


# 5. print prime numbers by taking only one for loop

# for i in range(2,101):
#     if i>1:
#         for k in range(2,i):
#             if i%k==0:
#                 break
#         else:
#             print(i)











#6. enter a string and print the longest substring without repeating characters,
# eg : input : python is an excellent programming language, output : python


# st="python is an excellent programming language"
# st=st.split()
# print(st)
# final_st=''
# for i in st:
#     temp_set=set()                     # should take empty set
#     for k in i:                         # i vales transfer to k
#         temp_set.add(k)                  # adding k's values to empty set
#     # print(temp_set)                      # we can see dont repetating duplicate values list
#
#     if len(temp_set)==len(i):               # # should compare j(python)==i length
#         print(i)
#         if len(i)>len(final_st):
#             final_st=i                     # in final st we are adding i
# print(final_st)

# class cls_double():
#     def __init__(self, st):
#         self.st = st
#         self.vowels = ["a", "e", "i", "o", "u"]
#
#     def len_2(self):
#         final_st = self.st * 2
#         return final_st[0:len(final_st) // 2] + final_st[len(final_st) // 2:].upper()
#
#     def len_even(self):
#         return self.st[0:len(self.st) // 2] + self.st[len(self.st) // 2:].upper()
#
#     def len_odd_ovwel(self, final_st):
#         return final_st[0].upper() + final_st[1:len(final_st) // 2] + final_st[len(final_st) // 2:].upper()
#
#     def len_odd_con(self, final_st):
#         return final_st[0].lower() + final_st[1:len(final_st) // 2] + final_st[len(final_st) // 2:].upper()
#
#     def run(self):
#         if len(self.st) == 2:
#             print(self.len_2())
#
#         elif len(self.st) % 2 == 0 and len(self.st) < 10:
#             print(self.len_even())
#         elif len(self.st) >= 10:
#             if len(self.st) % 2 == 0:
#                 final_st = self.len_even()
#                 print(final_st[0:4] + final_st[4:9].upper() + final_st[9:])
#
#             elif len(self.st) % 2 == 1:
#                 if self.st[0] in self.vowels:
#                     final_st = "v" + self.st
#                     print(self.len_odd_ovwel(final_st))
#                 else:
#                     final_st = "c" + self.st
#                     print(self.len_odd_con(final_st))
#
#         elif len(self.st) % 2 == 1:
#             if self.st[0] in self.vowels:
#                 final_st = "v" + self.st
#                 print(self.len_odd_ovwel(final_st))
#             else:
#                 final_st = "c" + self.st
#                 print(self.len_odd_con(final_st))
#
#
# st = "programmings"
# obj_cls_double = cls_double(st)
# obj_cls_double.run()


# dict={"company":"ReleaseOwl",
#       "uin no":787994646,
#       "company ceo":"niranjan",
#       "year":2013,
#       "manager":"madhu",
#       "location":"hyderabad",
#       "branches":445,
#       "company product":"SAP"}
# a=dict["manager"]
# print(a)
# dict["year"]=2018
# print(dict)
# dict.update({"locaton":"bengluru"})
# print(dict)
# dict.pop("branches")
# print(dict)
# dict.popitem()
# print(dict)
# print(type(dict))
# print(len(dict))
# for i in dict:
#      print(i)
# print(dict["location"])
# print(dict["company product"])
# print(dict.get("year"))
#
# print(dict.keys())
# print(dict.values())


# for x in "banana":
#   print(x,end="")

# st="python is awesome and python is easy"
# print("awesome" in st)
#
# st = "The best things in life are free!"
# if "free" in st:
#   print("Yes, 'free' is present.")

# st1="python is awesome "
# st2="python is easy"
# print(st1+" "+st2)



# class strings():
#     def __init__(self,str):
#         self.str=str
#     def s1(self):
#         double=str*2
#         return double[0:len(double)//2] + double[len(double)//2:].upper()
#
#     def even(self):
#         return str[0:len(str)//2] + str[len(str)//2:].upper()
#
#     def allpro(self):
#         if len(str)==2:
#             print(self.s1())
#
# str="hi"
# obj=strings(str)
# obj.s1()




           # REPLACE
# st="python is awesome and python is easy"
# st=st.replace("python","CPQ")
# print(st)
          #concadination

# st="cpq is good "
# st2="cpq is better"
# print(st+st2)

# st="cpq is good and cpq is better"
# print(len(st))
# print(type(st))
#
#        withoutspace
# st="cpq is good and cpq is better"
#
# st=st.replace(" ","")
# print(st)

# fi nd the index number
# st="cpq is good and cpq is better"
# st=st.find("i")
# print(st)
           # Capitalize
# st="cpq is good and cpq is better"
# st=st.capitalize()
# print(st)

# st=st.upper()
# print(st)
# st=st.lower()
# print(st)

# st="cpq is good and cpq is better"
# st=st.count("is")
# print(st)

# st="cpq is good and cpq is better"
# st=st.split()
# print(st)
# st=" ".join(st)
# print(st)


# st="cpq is good and cpq is better"
# st=st.title()
# print(st)
# st="cpq is good and cpq is better"
# u=st.split()
# # print(u)
# for i in u:
#     print(i.capitalize(),end=" ")

# age=25
# year=2000
# st=" i am 25 years old"
# st="i am {} years old,date of year {}".format(age,year)
# print(st)


# st="cpq is good"
# st2="cpq is great"
#
# print(st+ ",","it is easy to learn","and","easy to understand "," and " +st2)

# st="i didn\"t go"
# print(st)

# st="hyderabad"
# print(st[::-1])


# st="cpq is good and cpq is better"
# st=st.startswith("cpq")
# print(st)

# st="cpq is good and cpq is better"
# st=st.endswith("better")
# print(st)

# st= "45464116546"
# print(st.isdigit())
#
# st="cpq is good and cpq is better"
# st=st.replace("cpq","sap")
# print(st)
#
# st="cpq is good and cpq is very good"
# st=st.count("cpq")
# print(st)
# print(len(st))
# st=st.count('c',0,8)
# print(st)
# st=st.count("k")
# print(st)


# st="cpq is good and cpq is better 100"
# st=st.replace(" ","")
# print(st)
# st=st.isalpha()
# print(st)


# st="454651184854432"
# st=st.isdecimal()
# print(st)

# st="4544546545"
# st=st.isnumeric()
# print(st)





   # replace

# st="cpq is good and cpq is better"
# st=st.replace("cpq","sap")
# print(st)

   # concadination

# st1="cpq is good"
# st2="cpq is better"
#
# print(st1 + " and " + st2)

#add
# st="cpq is good and cpq is better"
# st=st.replace(" ","=")
# print(st)

#find
# st="cpq is good and cpq is better"
# st=st.find("e")
# print(st)

 # capitalize
# st="cpq is good and cpq is better"
# st=st.capitalize()
# print(st)
# st="cpq is good and cpq is better"
# st=st.upper()
# print(st)
# st=st.lower()
# print(st)
#              # starring letter upper
# st="cpq is good and cpq is better"
# st=st.title()
# print(st)

#split
# st="cpq is good and cpq is better"
# st=st.split()
# print(st)
 # join
# print(" ".join(st))

# count
# st="cpoooq is good and cpq is better good"
# st=st.count("cpq")
# print(st)
# st=st.count("")
# print(st)
# print(len(st))
# st=st.count("o",5,15)
# print(st)
       # english
# st="i didn\"t go"
# print(st)

# formate

# name="umesh"
# age=99
# st=" my name is {},age is {}".format("umesh",99)
# print(st)

# reverse

# st="bharathbro"
# print(st[::-1])
# print(st[::+1])

# start with

# st="cpq is good and cpq is better"
# st=st.startswith("cpq")
# print(st)

#ends with

# st="cpq is good and cpq is better"
# st=st.endswith("better")
# print(st)

# is alpha

# st=("husigdguguiqy")
# st=st.isalpha()
# print(st)

# is decimal

# st=("848798798778")
# st=st.isdecimal()
# print(st)

# is digit

# st="45668877"
# st=st.isdecimal()
# print(st)



# l=[10,20,30,40,50,"python","umesh",2.4,5.6,7.8,True,False]
# print(type(l))
# print(len(l))

# print(l[0])
# print(l[4])
#
# print(l[0:7])
# print(l[:12])
# print(l[0:])


# l=[10,20,30,40,50,"python","umesh",2.4,5.6,7.8,True,False]
# for i in l:
#     print(i)

# l=[10,20,30,40,50]
# for i in l:
#     print(i*2)

# l=[10,20,30,40,50,"python","umesh",2.4,5.6,7.8,True,False]
# l[5]="java"
# print(l)

# l[1:6]=56,45,57,78,"html"
# print(l)
# l[6:10]='naresh',"umesh","java","cc"
# print(l)


# l=[10,20,30,40,50,"python","umesh",2.4,5.6,7.8,True,False]
# l.insert(0,"7899")
# print(l)
# for i in range(2,101):
#     count=0
#     for k in range(1,i+1):
#         if i %k ==0:
#             count+=1
#     if count==2:
#         print(i)
         # by using only one one for lopp
# for i in range(1,101,2):
#     count=0
#     if i==1:
#         print(2)
#         continue
#     if i%3==0:
#         count+=1
#         pass
#     if i%5==0:
#         count+=1
#         pass # upto 9 no it will divisable by these no &check by 1 aslo other than 1 or itself primre number
#     if i%7==0:
#         count+=1
#         pass
#     if i%9==0:
#         count+=1
#         pass
#     if count==0 or (len(str(i))==1  and count==1):
#         print(i)

    # count is 0   # l3ngth is 1      count 1 length of 2

#
# start_year=2000
# end_year=2024
# for year in range(start_year,end_year):
#     if year%4==0 and year%100!=0:
#         print(year)


# class pvornv():
#     def __init__(self,n):
#         self.n=n
#     def pveornve(self):
#         if n>1:
#             print("its +ve")
#         else:
#             print("its a -ve")
# n=int(input("enter a number :"))
# obj=pvornv(n)
# obj.pveornve()


# class leapyear():
#     def __init__(self,n):
#         self.n=n
#     def lyr(self):
#         if n%4==0 and n%100!=0 or n%400==0:
#             print("its leap a year")
#         else:
#             print("its not leap year")
# n=int(input("enter a any year:"))
# obj=leapyear(n)
# obj.lyr()



# def prime(p):
#     count=0
#     for i in range(1,p+1):
#         if p%i==0:
#             count+=1
#     if count==2:
#         print(p)
#
# fi = filter(prime,range(2,101))
# (list(fi))

# def prime(p):
#     count=0
#     j=1
#     while j<p+1:
#         if p%j==0:
#             count+=1
#         j+=1
#     if count==2:
#         print(p)
# n=int(input("enter a number:"))
# fi=(filter(prime,range(2,n)))
# list(fi)

# l=[10,20,30,40,50,60]
# for i in l:
#     print(i)

# #iter
# l=[10,20,30,40,50,60]
# us=iter(l)
# print(next(us))
# print(next(us))
# print(next(us))



#arthametic fuctions
#
# x =int(input("enter a number"))
# y=int(input("enter a number"))
# print(x+y)
# print(x*y)
# print(x%y)
# print(x-y)



            #   +,-,*,% or /

# print("select options :")
# print("1. Adding ")
# print("2. Subtraction")
# print("3. Multi")
# print("4. Division")
#
# operation=input()
# if operation=="1":
#     num1 = int(input("enter the first number:"))
#     num2 = int(input("enter the second number:"))
#     print("sum is " + str(int(num1 + num2)))
# elif operation=="2":
#     num1 = int(input("enter the first number:"))
#     num2 = int(input("enter the second number:"))
#     print("diff is " + str(int(num1 - num2)))
# elif operation=="3":
#     num1 = int(input("enter the first number:"))
#     num2 = int(input("enter the second number:"))
#     print("mul is " + str(int(num1 * num2)))
# elif operation=="4":
#     num1 = int(input("enter the first number:"))
#     num2 = int(input("enter the second number:"))
#     print("div is " + str(int(num1 / num2)))
# else:
#     print("please choose correct option:")


#
#
# st=" python is awesome and it is easy to choice to pick"
# st=st.split()
# print(st)
# count1=0
# count2=0
# for i in st:
#     if len(i)%2==0:
#         count1+=1
#     else:
#         count2+=1
# print("number of even",count1)
# print("number of odd ",count2)



# n=int(input("enter a number:"))
# number=1
# while number<=n:
#     print("* "*number)
#     number+=1



# n=int(input("enter a number:"))
# number=1
# while number<=n:
#     for i in range(1,number):
#         print(i, end=" ")
#     print("\n")
#     number+=1


# n=int(input("enter a number:"))
# number=1
# val=2
# count=-1
# while number<=n:
#     pow=val**count
#     for i in range(1,number):
#         print(i**pow, end=" ")
#     print("\n")
#     number+=1
#     count+=1




# def sum(n1,n2):
#     return n1+n2
# n1=10
# n2=20
# print(sum(n1,n2))

# class addition:
#     def sum(self,a,b):
#         self.a=a
#         self.a=b
#     def add(self,a,b):
#         return a+b
# a = 10
# b = 20
# obj=addition()
# print(obj.add(a,b))

# class Multiply:
#     def __init__(self, a, b):
#             self.a = a
#             self.b = b
#     def multiply(self):
#         return self.a * self.b
# m = Multiply(10, 20)
# print(m.multiply())

# n=int(input("enter a no"))
# for i in range(1,n):
#     print(n,"*",i,"=",n*i)
# print ("\u2764\ufe0f")

# class mul:
#     def __init__(self):
#         self.mult="mult"
#
#     def multi


# print('\U0001F917')
# print('\U0001F618')
#














import mail
mail.sum(30,50)





# class computer:
#     def __init__(self,colour,ram,len):
#         self.colour = colour
#         self.ram = ram
#         self.len = len
#     def beh1(self):
#         return "colour of computer is " + str(self.colour)
#     def beh2(self):
#         return "ram of computer is " + str(self.ram)
#     def beh3(self):
#         return "len of the computer is " + str(self.len)
# obj1=computer("red","4gb ram","12 inches ")
# print(obj1.beh1())
# print(obj1.beh2())
# print(obj1.beh3())



def computer():
    print("this is hp lap top")



























