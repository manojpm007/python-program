# x=lambda a,b:a*b
# print(x(5,6))
#
#
# name_list=['grace hopper','ada lovelace','emmy noether','marie curie']
# sorted_by_surname=sorted(name_list,key=lambda x:x.split()[1])
# print(sorted_by_surname)


# def add(a,b):
#     return (lambda x:a+b)
# f=add(3,4) (0)
# print(f)
#
# res=lambda x:(x%2 and 'odd'or 'even')
# print(res(15))


# str=lambda string:string in "welcome to the world of lambda function in python"
# print(str('python'))


# map
# lst=['kousalya','bhavitha','bhuvan','namitha']
# lst_upper_case=list(map(str.upper,lst))
# print(lst_upper_case)

# circle_areas=[3.56773,5.57688,4.00914,5.62424,9.01344,3.20013]
# # round()
# res=list(map(round,circle_areas,range(1,7)))
# print(res)


#
# strngs=['a','b','c','d','e']
# numbrs=[1,2,3,4,5]
# res=list(zip(strngs,numbrs))
# print(res)
#

# strngs=['a','b','c','d','e']
# numbrs=[1,2,3,4,5]
# res=list(map(lambda x,y:(x,y),strngs,numbrs))
# print(res)

#
#
# marks=[45,66,70,34,68,74,23,90,86]
# def sort_marks(marks):
#     return marks>70
# res=list(filter(sort_marks,marks))
# print(res)


# wrds=['hgflkjh','madam','mom','radar','mnbv']
# palidrome=list(filter(lambda word:word==word[::-1],wrds))
# print(palidrome)


# # double of each  number using map
# numbers=[1,2,3,4,5]
# doubled_numbers=list(map(lambda x: x*2,numbers))
# print(doubled_numbers)


## reduce function
# from functools import reduce
# number=[3,4,5,6,7,8]
# print(number)


# def custom_sum(first,second):
#     return first + second
# result=reduce (custom_sum,number)
# print(result)
#
# numbers=[1,2,3,4,5]
# total=reduce(lambda x,y:x+y,numbers)
# print(total)
#
#
# numbers=[1,2,3,4,5]
# max_numbers=reduce(lambda x,y:x if x>y else y,numbers)
# print(max_numbers)













