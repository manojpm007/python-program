n1 = 89
n2 = 67
"""
res = n1+n2
print(res)
print(n1+n2)
print("The sum is::",res)
print("The sum is::",n1 + n2)
print("The sum is::",n1,"and",n2,"is",res)
#f string
print(f"The sum of {n1} and {n2} is::",res)"""
"""
name='manoj pm'
reg_no='1EW20IS047'
dept='ise'
ph_no='9380194693'
email='manojpm3010@gmail.com'
loc='bengaluru'
gen="M"
clg="east west institue of technology "
per="83.34"
print(name,'\n',reg_no,'\n',dept,'\n',ph_no,'\n',email,'\n',loc,'\n',gen,'\n',clg,'\n',per)"""

"""
pyz = '''
Hello, welcome to
"Be practical",Bangalore
Learning "Python Full Stack"
'''
print(pyz)"""

# arthimetic operater
"""
x = int(input("enter any number:: "))
y = int(input("enter any number:: "))

res = x+y
print("addition")
print("the result is:: ",x+y)
print("the result is:: ",res)
print(f"the difference of{x} and {y} is:: ",res)
print("-----------------------------------")

res = x-y
print("subraction")
print("the result is:: ",x-y)
print("the result is:: ",res)
print(f"the difference of{x} and {y} is:: ",res)
print("-----------------------------------")

res = x*y
print("multipaction")
print("the result is:: ",x*y)
print("the result is:: ",res)
print(f"the difference of{x} and {y} is:: ",res)
print("-----------------------------------")
21

print("floor divison ")
print("the result is:: ",x**y)
print("the result is:: ",res)
print(f"the difference of{x} and {y} is:: ",res)"""
print("-----------------------------------")
""""
x=int(input("enter any number: "))
y=int(input("enter any number: "))

res = x^2+y^2
print("square")
print("this result is:: ",res)

res=x^3+y^3
print("cube")
print("this result is:: ",res)

r=int(input("enter the radius,"))
print("the area of circle of radius {r} is {3.151*}")"""


# assignment operator

"""
x=int(input("enter any number:: "))
y=int(input("enter any number:: "))

x += y
print("the result is::",x)


x -= y
print("the result is::",x)

x *= y
print("the result is::",x)"""


#relational operater
"""
x = int(input("enter  number:: "))
y = int(input("enter  number:: "))

print(x>y)
print(x<y)
print(x==y)
print(x!=y)"""

"""
#logical operater

x = True
y = True
print(x and y)"""

#bit wise
"""
x=5
y=6
print(x and y)
print(x or y)
print(~x)
"""

# membership operators
"""
name="Dawa penjor"
print('Dawa'in name)

print('sonam' is name)

print('sonam'not in  name)"""

# identiy operators
"""
x=[1,2,3]
y=x
result=x is y
print(result)

a='hello'
b='word'
result=a is not b
print(result)"""

# id
"""
x=5
y=x
print(id(x))
print(id(y))"""
"""
x=4
y=5 
x+y
print(id(x))
print(id(y))
"""

# python code to demostrate type converion int,float

# implict
"""
a=5.5
b=5
res=a+b
print(res)"""

# explict
"""
s="10010"
print(type(s))
# printing string conversation to int base 2
c=int(s,2)
print("after converting to integer base 2: ")
print(c)
print(type(c)"""
# printing string coversation to float
"""
e="8"
e=float(8)
print("after converting to float:")
print(e)
print(type(e))"""


# list
"""
my_list=['p','r','o','b','l','e','m']
subject=['maths','science','social',['kannada','english','hindi'],'sankrit']

print(subject[3] [2])

# first item
print(my_list[0])

#third item
print(my_list[2])

#fifth item
print(my_list[4])
"""
#negative indexing
"""
my_list=['p','r','o','b','e']

#last item
print(my_list[-1])

#fifth last item
print(my_list[-5])

#list slicing of python
my_list=['p','r','o','b','e']
# elements from index 2to index 4(it will read(n-1)logic)
print(my_list[2:5])

# negative slicing 
print(my_list[:5])
print(my_list[:-5])"""

# add /changes list elements

# correcting mistakes values ina list
"""
even=[2,4,6,8]
print(even)
#change the 1st item
even[0]=1
print(even)

#change 1nd to 3rd items
even[1:4]=[3,5,7]
print(even)

# append and extend

# appending and extending lists inpython


"""
#
"""

#deleting list item
my_list=['p','r','o','b','l','e','m']
#delete multiple items
del my_list[1:5]
print(my_list)

del my_list[2]
print(my_list)"""

#delete the entire list
"""del my_list
print(my_list)

#remove() and pop()
my_list=['p','r','o','b',['l','u','p'],'e','m']
my_list.remove('m')
print(my_list)

print(my_list.pop(4))
print(my_list)

my_list.clear()
print(my_list)"""
"""
#sort python list
#ascending
mylist=[21,5,8,52,21,87,52]
mylist.sort()
print(mylist)

# descnding
mylist=[21,5,8,52,21,87,52]
mylist.sort(reverse=True)
print(mylist)"""


# tuples
"""
tpl=(2,4,5,7,8,[10,17,23],45,23)
tpl[5][1]=21
print(tpl)

tpl=(2,4,5,7,8,[10,17,23],45,23)
print(tpl[-5])
print(tpl[:5])
print(tpl[:-5])"""

# zip tuple
"""
first_names=('Anil','Sarah','Metha','Arjun')
last_names=('Das','Pm','Raj','Gowda')
ages=(49,55,65,78)
res=zip(first_names,last_names,ages)
print(res)
print("------------------------------------")
cmr=tuple(res)
print(cmr)

first_names,last_names,ages=cmr[3]
print(f"{first_names} {last_names} is {ages} year old")"""

#adding tuples together
"""
Tuple_a=(1,2)
Tuple_b=('x','y')
Tuple_c=Tuple_a+Tuple_b
print(Tuple_c) """

#sorted
"""
a=(3,5,8,2,9)
print(type(a))
b=sorted(a)
print(b)
print(type(b))

a=(1,3,4,5,6)
print(type(a))
b=sorted(a)
print(b)
print(type(b))

# Appending and Extending lists in Python
even = [1, 3, 5]
even.append( [7,8,9] )
print(even)
even.extend([9, 11, 13])
print(even)"""

# set
"""
set1=set([1,1,1,2,2,3]) #from list
set2=set(('a','a','b','b','c'))#from tuple
set3=set('anaconda')# from a string

#second way:using curly branches

set4={1,1,'anaconda','anaconda',8.6,(1,2,3),None}
print('set1:::',set1)
print('set2:::',set2)
print('set3:::',set3)
print('set4:::',set4)"""

#inital
#discard
"""
myset={1,2,3,4}
myset.discard(1)
print(myset)
myset.discard(5)
print(myset)


#remove
myset.remove(4)
print(myset)
myset.remove(5)
print(myset)"""

# pop
"""
myset={1,2,3,4}
print(myset.pop())
print(myset)

#removing all the items
myset.clear()
print(myset)

myset={5,10,15}
print('set:',myset)
print('size:',len(myset))
print('min:',min(myset))
print('max:',max(myset))
print('sum:',sum(myset))
print('\n')

# all set with all() and any() all act as and operator and any operator
print(all({1,2,'a',2.4}))
print(all({1,False}))
print(any({1,False}))
print(any({False,False}))

# a set with sort() function
myset={4,2,5,1,3}
print(sorted(myset))
myset={'c','b','e','a','d'}
print(sorted(myset))



# dictonary

# three type of identiy

#type

MLB_team={
    'colorando':'Rockies',
    'Bostron':'Redsox',
    'minnesota':'twins',
    'milwaukee':'brewers',
    'seattle':'mariens'
}
print(MLB_team)

#type2
MLB_team=dict([
    ('colorado','rockies'),
    ('manoj','chethan'),
    ('prajwal','manoj'),
    ('chethan','gowda'),
])
print(MLB_team)

#type 3
MLB_team=dict(
    manoj='pm',
    boston='red sox',
    minnestoa='twins',
    chethan='gowda',
    age=23
)
print(MLB_team)"""

# adding in diffrent catergires
"""
Employee = {'name':'john','age':29,'experience':4.5,'salary':25000,'company':'cisco'}
Employee['name'] = 'Jack'
Employee['age'] = 27
Employee['experience'] = 4.0
Employee['salary'] = 50000
Employee['company'] = 'accenture'


print(Employee)
print("printing employee1 data:")
print("name:%s"%Employee["name"])
print("age:%d"%Employee["age"])
print("experience:%f"%Employee["experience"])
print("salary:%d"%Employee["salary"])
print("company:%s"%Employee["company"])
print("---------------------------------------------------")
print("printing employee2 data:")
print("Name:%s"%Employee["Name"])
print("Age:%d"%Employee["Age"])
print("Experience:%f"%Employee["Experience"])
print("Salary:%d"%Employee["Salary"])
print("Company:%s"%Employee["Company"])"""


# dictinary.get()
"""

my_dict={'a':10,'b':20,'c':30}
print(my_dict.get('b'))

# d.items()
d={'a':10,'b':20,'c':30}
print(d.items())
print(list(d.items())[1][0])
print(list(d.items())[1][1])

# d.keys()
d={'a':10,'b':20,'c':30}
print(list(d.keys()))
print(d.keys())
# d.values()
d={'a':10,'b':20,'c':30}
print(list(d.values()))"""




# test
"""
it is easy to learn
it can run with "" or ''

#2
mutable data type:is it can add or it can delete
immutable data type :it cannot add or delete

#3

x=int(input("enter any number::"))
y=int(input("enter any number::"))

res=x+y
print(res)

#4
# sample data:3,5,7,23

tpl=[3,5,7,2,3]
tpl[2]=[1]
print(tpl)

a=(3,5,7,23)
print(type(a))
b=sorted(a)
print(b)


#5
tuple1 =(11,22)
tuple2 =(99,88)
tuple3=tuple1+tuple2
print(tuple3)

# 1list program
my_list=(2,3,4,(1,2,3),5,6)
print(my_list[0])
print(my_list[-1])
print(my_list[:3])

# 2 index in alist

my_list=[2,3,6,7,8,9]
my_list[1:2]
print(my_list)

# 3

my_list=[2,8,4,5,9,7]
my_list.sort()
print(my_list)

my_list=[2,8,4,5,9,7]
my_list.sort(reverse=True)
print(my_list)

# 4
my_list=[2,8,4,5,9,7]
print(min(my_list))
print(max(my_list))

# TUPLES
tpl=(2,3,4,[1,2,3],5,6,7)
tpl[3][1]=21
print(tpl)

#2
tpl=("sunday","monday","tuesday","wendesday","thursday","friday","saturday")
print(tpl[3])
print(tpl[1])

# sets
#1,2
set1=set([1,1,1,2,2,3])
set2=set(('2','4','5','6'))
print(set1)
print(set2)

#3
myset={1,2,3,4}
myset.remove(2)
print(myset)

#4
print(all({1,2,2,1}))
print(all({1,False}))

#dict
MLB_type={
    'volvo':'x6',
    'maruti':'suzuki',
    'audi':'q7'
}
print(MLB_type)
"""

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
if (x%2)==0:
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
"""
x=int(input("enter any number:: "))
if:    print(f"{x} is lesser than {y}")
x<=18:
    print(f"the person age is {x} is valid for vote ")
else:
    print(f"the person age is {x} is not valid for vote  ")
   
 """
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
# if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
#     print(f" the given  aplhabets{char} is vowel ")
# else:
#     print(f"the given a"
#           f"aplhabets{char} is constant")

# 








