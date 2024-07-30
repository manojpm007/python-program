# squares = [x**2 for x in range(11)]
# print(squares)


# city1=["paris","london","berlin","tokyo","sydney"]
# city2=[]
# for x in city1:
#     city2.append(x)
# print(city2) normal method

# with list comprehession
# city1=["paris","london","berlin","tokyo","sydney"]
# city2=[]
# city2=[x for x in city1]
# print(city2)



# numbers=[1,2,3,4,5,6,7,8,9,10]
# even_no=[]
# even_no=[i  for i in numbers if i%2==0]
# print(even_no)
# print("--------------------------")

# normal
# list1=['q','a','t','d','o','f','e']
# list2=['a','e','i','o','u']
#
# result=[]
#
# for i in list1:
#     for j in list2:
#         if i==j:
#             result.append(i)
#
# print(result)


# with comprehension
# list1=['q','a','t','d','o','f','e']
# list2=['a','e','i','o','u']
# result=[i for i in list1 for j in list2 if i==j]
# print(result)
# print("-----------------------------")


# words=["filtering","words","based","on","length"]
# five_lttr=[word for word in words if len(word)==5]
# print(five_lttr)


# my_friut=['apple','banana','orange','mango']
# my_friut2=[i[0] for i in my_friut]
# print(my_friut2)

#
#
# mixed_list=['apple','banana',12,15,7,2,3,'organe','mango']
#
# #  if type is equal to int the append square of the number
# # otherwise append first character of string
#
# mixed_list2=[i** 2 if type(i) == int else i[0] for i in mixed_list ]
# print(mixed_list2)

# using list comprehension with fucntions
# def power(x):
#     return x**2
# p_num=[]
#
# for x in range(1,10):
#     p_num.append(power(x))
# print(p_num)
#
#
# # with compression
# def power(x):
#     return x**2
# p_num =[power (x) for x in range(1,10)]
# print(p_num)

# nested list comprehension


# nstd=[[1,2],[3,4],[5,6]]
# elements=[elements for pair in nstd for elements in pair]
# print(elements)

# #
# list1=[1,2,3]
# list2=["a","b","c"]
# pairs=[(x,y) for x in list1 for y in list2]
# print(pairs)



#  question
# 1.generate a set of common elements from two lists
#
# list1=[1,2,3,4,5]
# list2=[3,4,5,6,7]
# result = [i for i in list1 for j in list2 if i == j]
# print(result)


# # 2.wap to generate pairs of distinct elemts and thier charcter postion sum from two lists
# list1=["abc","def","ghi"]
# list2=["jkl","mno","pqr"]
# pairs=[(x,y) for x in list1 for y in list2]
# print(pairs)







































































































