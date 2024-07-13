# considation
"""
x=int(input("enter any number::"))
y=int(input("enter any number::"))

if x >= y:
    print(f"{x}is bigger than {y}")

elif x<=y:
    print(f"{x} is lesser than {y}")
elif x<=y:
    print(f"{x} is not equal to  {y}")

else:
    print(f"{x}in equal to {y}")

"""
"""
x=int(input("enter any number:: "))
if x%2==0:
    print(f"{x} is even")
else:
    print(f"{x} is odd")"""

# 0 leap year or not
"""
x=int(input("enter any number:: "))
if (x%4)==0:
    print(f"{x}is leap year")
else:
    print(f"{x} is not leap year")"""

# age is valid to vote or not
#
# x=int(input("enter any number:: "))
#
# if x>=18:
#
#     print(f"the person age is {x} is valid for vote ")
# else:
#     print(f"the person age is {x} is not valid for vote  ")


# divisble by 3 or 5

# x=int(input("enter any number:: "))
# if x%3==0:
#     print(f"the number {x} divisble by 3")
# elif x%5 == 0:
#     print(f"the number {x} divisble by 5")
#
# else:
#     print(f"the number {x} is not divisble by  3 or 5")

# check biggest 3 number
#
# x=int(input("enter x value::"))
# y=int(input("enter y value::"))
# z=int(input("enter z value::"))
# if x>y and x>z:
#     print(f"{x} is bigger than {y} and {z}")
# elif y>z and y>x:
#     print(f"{y} is bigger than {z} and {x}")
# elif z>x and z>y:
#     print(f"{z} is bigger than {x} and {y}")
#
# enter vowel or constant
# char=input("enter the alphabets::")

#     print(f" the given  aplhabets{char} is vowel ")
# else:
#     print(f"the given a{char} is constant")

# taking 5 subject add and result to
# english=int(input("enter the marks::"))
# kannada=int(input("enter the marks::"))
# hindi=int(input("enter the marks::"))
# maths=int(input("enter the marks::"))
# social=int(input("enter the marks::"))
# total=english+kannada+hindi+maths+social
# print(f"total marks is {total}")
# avg=total/5
# print(f"avg marks is {avg} ")

# if avg>=95:
#     print("distication")
# elif 65<=avg<=95:
#     print("first class")
# elif 45<=avg<=65:
#     print("second class")
# elif 30<=avg<=45:
#     print("third class")
# else:
#     print("fail")

# bank account deatils valid or not,if valid display account deatils

# id=89
# acc_num = "sbi 89"
#
# x =int(input("enter id :"))
# y =input("enter acc_num :")
#
# if x ==id and y ==acc_num:
#      print("""
#      bank name:"kotak bank"
#      acc holder name:manoj pm
#      type of acc:saving
#      balance:2000""")
# else:
#      print(f"entered  x'{id}' or  y'{acc_num}' is wrong ")
# # rental of cars
print("wlc for car rentals:")
print("enter the name::")
name=input("")
print("enter your  age::")
age=int(input(""))
if age<18:
    print("perosn age invalid ")
else:
    print("DL_no")
Dl_no=(input(""))
print("select type of vehicle")
print("""two wheeler
four wheeler
""")
vehicle_type=int(input())
if vehicle_type==1:
    print("""
    activa
    suzuki
    xpulse
    mt 15 """)
    model=int(input())
    if model==1:
        print("activa")
        print("rent per hours is 56")
        hour=int(input())
        print("vehicle cost")
        cost=(56*hour)
        print(cost)
        total=cost*0.12+cost

    elif model==2:
        print("suzuki")
        print("rent per hours is 56")
        hour = int(input())
        print("vehicle cost")
        cost = (56 * hour)
        print(cost)
        total = cost * 0.12 + cost
    elif model==3:
        print("xpulse")
        print("rent per hours is 56")
        hour = int(input())
        print("vehicle cost")
        cost = (56 * hour)
        print(cost)
        total = cost * 0.12 + cost
    elif model==4:
       print("mt 15")
       print("rent per hours is 56")
       hour = int(input())
       print("vehicle cost")
       cost = (56 * hour)
       print(cost)
       total = cost * 0.12 + cost

else:
      print(" type of vehicle is invalid ")

if vehicle_type==2:
    print("""
    nexon
    punch
    taigo
    kia """)
    model=int(input())
    if model==1:
        print("nexon")
        print("rent per hours is 100")
        hour=int(input())
        print("vehicle cost")
        cost=(100*hour)
        print(cost)
        total=cost*0.12+cost

    elif model==2:
        print("punch")
        print("rent per hours is 100")
        hour = int(input())
        print("vehicle cost")
        cost = (56 * hour)
        print(cost)
        total = cost * 0.12 + cost
    elif model==3:
        print("tiago")
        print("rent per hours is 100")
        hour = int(input())
        print("vehicle cost")
        cost = (100 * hour)
        print(cost)
        total = cost * 0.12 + cost
    elif model==4:
       print("kia")
       print("rent per hours is 100")
       hour = int(input())
       print("vehicle cost")
       cost = (100 * hour)
       print(cost)
       total = cost * 0.12 + cost

else:
      print(" type of vehicle is invalid ")


















































































