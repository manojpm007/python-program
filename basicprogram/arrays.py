import array as arr
# numbers = arr.array('i',[10,20,30,40,50])
# print(numbers)
# print("------------------------------")
# for x in numbers:
#     print(x)
#
# a=arr.array('d',[1.1,2.1,3.1])
# print(a[1])
#
# a=arr.array('d',[1.1,2.1,3.1])
# print(len(a))
#
#
# a=arr.array('d',[1.1,2.1,3.1])
# a.append(3.4)
# print(a)
# a.extend([4.5,6.3,6.8])
# print(a)
#
# ### to add  a d specfic element at a particular index postion in array,
# ## the insert(i,x) function ca be used
# a=arr.array('d',[1.1,2.1,3.1])
# a.insert(1,3.8)
# print(a)
#
#
# a=arr.array('d',[1.1,2.1,3.1,2.6,7.8])
# b=arr.array('d',[3.7,8.6])
# c=arr.array('d')
# c=a+b
# print("array c=",c)


# # find the sum of all array elements
# sum=0
# numbers= arr.array('i',[10,20,30,40,50])
# for x in numbers:
#     sum +=x
# print(sum)

# reverse
# a=arr.array('i',[10,20,30,40,50])
# print(a[::-1])

# display even numbers
# sum=0
# numbers= arr.array('i',[1,2,3,4,5,6,7,8,9])
# for x in numbers:
#     if x%2==0:
#         print(x)
#     sum +=x
# print(sum)

# silicing
# a=arr.array('i',[1,2,3,4,5,6,7,8,9,10])
# print(a[0])
# print(a[-7])
# print(a[:2])

# max and min
# a=arr.array('i',[1,2,3,4,5,6,7,8,9,10])
# print(max(a))
# print(min(a))

# delete
# a=arr.array('i',[1,2,3,4,5,6,7,8,9,10])
# del(a[2])
# print(a)

# square and cube
# a=arr.array('i',[1,2,3,4,5,6,7,8,9,10])
# for x in a:
#     print(f" the square of array {x}is::",x**2)
#     print(f" the cube of array {x}is::", x**3)
#     print("---------------------------------")



# for min and max
# num_array=arr.array('i',[3,5,7,8,-1,4,10,12])
# if len(num_array)==0:
#     print("the array is empty")
# else:
#     max_num=num_array[0]
#     min_num=num_array[0]
# for num in num_array:
#     if num > max_num:
#         max_num = num
#     if num <min_num:
#         min_num=num
#     print(f"the maxinum number is {max_num}")
#     print(f"the mininum  number is {min_num}")

# multi dimentional arrays
# T = [[11,12,5,2],[15,6,10,5],[10,8,12,5],[12,15,8,6]]
# print(T)
# print("------------------------------")
# for r in T:
#     for c in r:
#         print(c,end=" ")
#     print()
#using nested concepts
# T = [[11,12,5,2],[15,6,10,5],[10,8,12,5],[12,15,8,6]]
# print(T)
# T.insert(2, [0,5,11])
# for r in T:
#     for c in r:
#         print(c,end=" ")
#     print()

#matrix  using  join() function
# m=[[1,2,3],[7,1,5],[0,9,3]]
# for i in m:
#     print("".join(str(i)))
#


import array as arr
from numpy import ones,zeros,reshape,eye,arange

#
# a=ones((3,4),int)
# print(a)
# b=zeros((3,4),int)
# print(b)
# print("----------------")
# c=eye(3)
# print(c)
# print("--------------------------------")
#
# arange
# a=[1,2,3,4,5,6]
# b=reshape(a,(2,3))
# print(b)
# print("=========")
# b =reshape(a,(3,2))
# print(b)

# a=arange(12)
# print(a)
# b=reshape(a,(2,3,2))
# print(b)
# print("-------------------------")
# b=reshape(a,(3,2,2))
# print(b)

t = arange(9)
print(t)
a=reshape(t,(3,3))
print(a)
print("-------------------------")
b=reshape(t,(3,3))
print(b)
print("-------------------------")
sum=a+b
print(sum)




 















































