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
