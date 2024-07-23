# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def div(a,b):
#     return a/b
# v1=int(input("enter the number"))
# v2=int(input("enter the number"))
# print("---------------------------")
# print("select(1) for addition ")
# print("select(2) for subraction ")
# print("select(3) for divison ")
# print("------------------------")
# ch =int(input("enter your choice:: "))
# if ch==1:
#     print(f"{v1} + {v2} addition is::",add(v1,v2))
# if ch==2:
#     print(f"{v1} + {v2} subraction is::", sub(v1,v2))
# if ch==3:
#     print(f"{v1} + {v2} divison is::", div(v1,v2))
#
# argument and no return value
# def multiply(x,y):
#     print("value ofx=",x)
#     print("value ofy=",y)
#     c=x*y
#     print(c)
# multiply(y=2,x=4)
# function with noarugument,in return value

# def factorial_number():
#     factorial=1
#     num=int(input("enter a number to get its factorical:"))
#
#     for i in range(1,num+1):
#         factorial=factorial*i
#         print("the factorial is",factorial)
# factorial_number()

# no arugument,with return value
#
# my_list=[23,44,66,74,23]
#
# def add_list():
#     sum=0
#     for list_item in my_list:
#      sum=sum+list_item
#     return sum
# result=add_list()
# print("the sum is",result)
#
#



# def is_palindrome(num):
#     num = str(num)
#     rev = num[::-1]
#     if num == rev:
#         return True
#     else:
#         return False
# x1 = 373
# result = is_palindrome(x1)
# if result:
#     print(f"{x1} is a palindrome.")
# else:
#     print(f"{x1} is not a palindrome.")



#
# def is_palidrome(num):
#     num=str(num)
#     rev= num[::-1]
#     if num==rev:
#     print(f"the given number {n} is palidrome")
# def multiply(x,y):
#     print("value ofx=",x)
#     print("value ofy=",y)
#
#
#
#
# #palindrome with no arguement and no return function
# num = int(input("enter any number:"))
# rev = 0
# temp = num
# while num!=0:  #while num>0
#     digit = num%10
#     rev = rev*10+digit
#     num//= 10
# print("the reverse of the number is::", rev)
# if rev == temp:
#     print("is palindrome")
# else:
#     print("is not palindrome")
#
#
# # palindrome without arguement with return function
# def find_palindrome():
#     num = input("Enter a number: ")
#     if num.isdigit():
#         num = int(num)
#         def is_palindrome(n):
#             return str(n) == str(n)[::-1]
#         original_num = num
#         while True:
#             if is_palindrome(num):
#                 print(f"The palindrome of {original_num} is: {num}")
#                 return num
#             else:
#                 num += 1
#     else:
#         print("Invalid input. Please enter a valid number.")
# find_palindrome()







































