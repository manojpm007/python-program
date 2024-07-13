# looping (control statement)
# for x in range(1,11):
#     print(x)
#
# for x in range(10,0,-1):
#     print(x)
#
# find sum of first 10 numbers
# sum=0
# for x in range(1,11):
#     sum+=x
# print("----------------------")
# print(" the sum is::",sum)
# x=0
# for i in range(1,11):
#      x += i
#      print(x)




# # print odd number and even number b/w 1 to 20 finf thier sum
# sum=0
# for x in range(1,21):
#   if x%2==0:
#    print(x)
#    sum += x
# print(" the sum of even num is::",sum)
# print("-----------------------------")
# for x in range(1,21):
#     if x % 2!=0:
#       sum +=x
# print(" the sum odd num  is::",sum)


# print all leap  year between 2000& 2024

# print("leap year between 2000 to 2024")
# for x in range(2000,2024):
#     if x%4==0:
#      print(x)


# python program that prints each items and its corresponding type from the followig
# datalist=[1452,11.23,True,'Be practical',(0,1),[5,12],{"class":'V',"section":'A'}]
# for i in datalist:
#      print(f"the item is {i}",type(i))


# print only even number of the defined list and find
# lst=[23,48,24,67,87,4,23,78]
# sum=0
# for i in lst:
#     if i%2==0:
#         print(i)
#         sum += i
#
# print(sum)


# squrae and cube
# lst=[2,3,4,5,6]
# for i in lst:
#         print(f" the square and cube {i} is ",i**2 ,'and', i**3 )

# separate and postive  and negative
#x=[2,3,4,5,6]
# print(f"the postive number in {x} is::")
# for i in x:
#         if i>=0:
#                 print(i)
# print(f" the negative number in {i} is ::")
# for i in x:
#         if i<0:
#                 print(i)

#print demonstrate a calculator
# a=int(input("enter the a value:: "))
# b=int(input("enter the b value:: "))
# print("""select the number of operator
# 1:'+'
# 2.'-'
# 3.'*'
# 4.'%'
# """)
# operator=int(input())
# if operator==1:
#     print("addition")
#     print(a+b)
#
# elif operator==2:
#     print("subraction")
#     print(a-b)
#
# elif operator==3:
#     print("multipaction")
#     print(a*b)
#
# elif operator==4:
#     print("divison")
#     print(a/b)
#
# else:
#     print("invalid values ")







#
# # print multipcation for table
# x=int(input("enter the number to be multipaction"))
# table=[1,2,3,4,5,6,7,8,9]
# for i in table:
#     print("f{x}*{i}=",x*i)
#
#
# # factorinal
# # num=int("enter any number")
# # fact=1
# # for x in range(1,num+1):
# #     fact *=x
# #     print(" the factorinal of {num}"is ,fact ")


# palidrome
# num =int(input(" enter any number:: "))
# rev=0
# while num!=0:
#     digit=num%10
#     rev = rev*10+digit
#     num//=10
# print("the reverser of the number is:: ",rev)

# num =int(input(" enter any number:: "))
# rev=0
# temp= num
# while num!=0:
#     digit=num%10
#     rev = rev*10+digit
#     num//=10
# print("the reverser of the number is:: ",rev)
# if rev==temp:
#     print(" is palindrome")
# else:
#     print(" is not palidrome")


# astromd
# num=int(input("enter any  3 digit number:: "))
# sum=0
# temp=num
#
# while temp!=0:
#     d=temp%10
#     sum +=d*d*d
#     temp//=10
#
# if sum==num:
#     print(" it is an Amstrong number")
# else:
#     print(" it is not  Amstrong number")

# num=int(input("enter any  4 digit number:: "))
# sum=0
# temp=num
#
# while temp!=0:
#     d=temp%10
#     sum +=d*d*d*d
#     temp//=10
#
# if sum==num:
#     print(" it is an Amstrong number")
# else:
#     print(" it is not  Amstrong number")

# continue and break
# for x in range(1,21):
#     if x==14:
#         continue
#     print(x)
#
# for x in range(1,21):
#   if x==14:
#       break
#   print(x)



 #nesting of loop

# for r in range(6,1,-1):
#      for c in range(1,r+1):
#          print(c,end=" ")
#      print()
# for r in range(1,6):
#      for c in range(1,r+1):
#          print("*",end=" ")
#      print()
# for r in range(6,1,-1):
#      for c in range(1,r+1):
#          print("*",end=" ")
#      print()


# for r in range(6,1,-1):
#     for c in range(1,r+1):
#         print("x",end=" ")
#     print()

# for x in range (6,1,-1):
#     for y in range (6,x-1,-1):
#         print(y-1,end=" ")
#     print()


# for x in range(3):
#     for y in range(1,11):
#         print(y,end=" ")
#     print()


# by taking user input
# rows=int(input("enter the # of rows:: "))
# cols=int(input("enter the # of cols:: "))
# symbols=input("enter the symbol:: ")
# for x in range(rows):
#     for y in range(cols):
#         print(symbols,end =" ")
#     print()


# loop with list items
# fruits=['mango','apple','grapes','peach']
# for f in fruits:
#     for i in f:
#         print(i,end="*")
#     print()
#
# fruits=['mango','apple','grapes','peach']
# for f in fruits:
#     for i in f:
#         print(f,end="*")
#     print()




# color=['red','green','pink']
# items=['apple','veggies','watch']
# for x in color:
#     for y in items:
#         print(x,y)
#         print('')



# # while loop
# i=5
# while(i>0):
#     j=5
#     while(j>i):
#         print("x",end=" ")
#         j=j-1
#     i=i-1
#     print()

#append  2 lists
#
# list1=[10,20,30]
# list2=[40,50,60]
# result=[]
# for i in list1:
#     for j in list2:
#         result.append(i+j)
#     print(result)


# multiping 2 lists
# list1 = [2,4,6,8]
# list2 = [2,4,6,8]
#
# for i in list1:
#     for j in list2:
#         if i==j:
#             continue
#         print(i,"*",j,"=",i*j)
#
# a=1
# while a<=50:
#     sum=0
#     for i in range(1,a):
#         if i%2==0:
#             sum +=i
#     a=a+1
# print("the sum of even numbers is::",sum)

#
# fruits =['apple','mango','grapes','kiwi']
# for f in fruits:
#     count=0
#     while count<6:
#         print(f,end =" ")
#         count=count + 1
#     print()

# for x in range(-6,1):
#     for y in range (-x):
#         print(y,end=" ")
#     print()

#
#
# print("""select your choice
# 0.paper
# 1.rock
# 2.stone""")
# choice=int(input("enter any choice"))
# if choice==1:
#     print("paper")
# elif choice==2:
#     print("rock")
# elif choice==3:
#     print("stone")
# choice=("choice:")
# lst=["paper","rock","stone"]
# for i in lst:
#     if choice==lst[1]:
#         print('draw')
#     elif choice==lst[2]:
#         print('your lost')
#
#
# else:
#         print("invalid choice")










#
#
# print("""select your choice
# 1.rock
# 2.paper
# 3.scissor """)
# choice =int(input("enter any choice:: "))
# if choice==1:
#  lst=["rock","paper","scissor"]
# for i in lst:
#  if choice==lst[1]:
#      print("drawn")
#  elif choice==lst[2]:
#      print(" your lost")
#  print()







# #
#
# choice=input("enter your choice::")
# player1=['rock','paper','scissor']
# player2=['rock','paper','scissor']
# for i in player1:
#     for j in player2:
#          if i==j:
#              print("")
#          else :
#              print("the player1 is winner")
#              continue
#     print()


print("welcome to rock,paper,scissor game")
print('''
1.rock
2.paper
3.scissor
''')
x = input("enter the option::")
if x == 'rock':
    print("the game is over and player draw the game ")

else:
    print("the game is over and player win game")








































































