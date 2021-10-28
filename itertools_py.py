'''itertools() -->'''

'''cycle():-->repeat predefine steps for infinite times
if we want to use fixed data repete cycle
                  e.g ludo, playwin(lottery), worker    '''
from itertools import cycle
import time

# values = [1,2,3,4,5]
# c = cycle(values)   # infinite iterator
# #
# for item in c:
#     print(item)
#     time.sleep(1)
#

# print("----------------------------------------------------------------------")

# def precheck():
#     pass
#
# def packing():
#     pass
#
# def pricetag():
#     pass
#
# product_manf_line = [precheck,packing,pricetag] # pipeline--> pipeline-->
# cyc = cycle(product_manf_line)
# products = []
# for product in products:
#     for item in range(cyc): #stop --> precheck
# item(product) #--> precheck --> packing-->pricetag
# --precheck --packing-->pricetag
# precheck --> break
# print("----------------------------------------------------------------------")

from itertools import cycle
import time

cy = cycle("ABCDE")

# for item in cy:
#     print(item)
#     time.sleep(1)


# for item in cy:
#     print(item)
#     if item =='D':
#         break
#     time.sleep(1)
#
#
# def precheck(p):
#     print('inside precheck',p)
#     return True
#
# def price_tag(p):
#     if p=="p4":
#         return False
#     print('inside pricetag',p)
#     return True
# #
# def final_check(p):
#     print('final check',p)
#     return True
# #
# values = [precheck,price_tag,final_check]
# products = ["p1","p2","p3","p4","p5","p6"]
# cy = cycle(values)
# #
# for prod in products:
#     for index,item in enumerate(cy):
#         value = item(prod)
#         if not value:
#             print(prod,"Failed",item)
#             break
#         if index==3:
#             break
#         time.sleep(1)

# print("----------------------------------------------------------------------")
'''count() -->count 0 to infinite value from given steps'''
from itertools import count

# cnt = count(1, step=.5)  # infinite
#
#
# for item in cnt:
#     print(item)
#     time.sleep(1)

# cnt = count(10, step=-1)  # infinite
#
#
# for item in cnt:
#     print(item)
#     time.sleep(1)

'''repeat() -->repeat same element infinite time'''
# from itertools import repeat
#
# r = repeat("A")  # infinite
# for item in r:
#     print(item)
#     time.sleep(1)

# print("----------------------------------------------------------------------")
'''chain()'''
from itertools import chain

# val1 = [10,20,30,40,50,60]
# val2 = ["A","B","C","D","E","X"] #
# val3 = ("A1","B2","C3","D4")
# ch = chain(val1,val2,val3) #logically merge -?? --> iteration purpose--> finite
# print(list(ch))
#
# for item in ch:
#     print(item)
#     time.sleep(1)

# print("----------------------------------------------------------------------")
'''Compress(): This iterator selectively picks the values to print from the passed container according to the boolean
 list value passed as other arguments. The arguments corresponding to boolean true are printed else all are skipped.

compress()--> 0/False don't give value, 1/True give value
    -->used for image processing and compression
    '''
import itertools
import operator

# example = itertools.compress('ABCDE5', [1, 0, 1, 0, 0, 1])
#
# for each in example:
#     print(each)


from itertools import compress
#
# import random
# value = [random.randint(1, 100) for item in range(20)]
# value1 = [random.randint(0,1) for item in range(20)]
# print(value)
# print(value1)
#
# val=compress(data=value, selectors=value1)
# print(list(val))

import random

# value = [95, 20, 12]
# value1 = [0 , True, 1]
# print(value)
# print(value1)
#
# val=compress(data=value, selectors=value1)
# print(list(val))

# print("----------------------------------------------------------------------")
'''dropwhile()-->
 finds the first false and then start collecting '''
import random
from itertools import dropwhile


# def is_positive(n):  # this is for +ve numbers
#     return n > 0
#
#
# value_list = [5, 6, -8, -4, 11, 2, 1, -4]
# result = list(itertools.dropwhile(is_positive, value_list))
# print(result)

# values = [random.randint(5,55) for item in range(10)]
# print(values)
#
# dw = dropwhile(lambda x: x%5==0, values )
# print(list(dw))


# val = [5, 10, 15]
# values = [random.randint(5,55) for item in range(10)]
# val.extend(values)
#
# print(val)
# dw = dropwhile(lambda x: x%5==0, val)
# print(list(dw))


'''takewhile():-'''

'''filterfalse()-->
whenever predicate return false start collecting
This iterator prints only values that return false for the passed function.
----->only false value collecting'''
# from itertools import filterfalse
#
# values = [random.randint(5, 55) for item in range(10)]
# print(values)
# dw = filterfalse(lambda x: x % 5 == 0, values)
# print(list(dw))

# print("----------------------------------------------------------------------")

'''starmap() 
Syntax : starmap(function, iterable)
'''
from itertools import starmap

# def fun(x, y):
#     return x * y
#
#
# values = [(1, 2), (2, 3), (3, 3), (2, 3), (4, 5)]
# ans = starmap(fun, values)   # extended version of map
# print(list(ans))


# def val(x, y, *args):
#     ans = x + y
#     for item in args:
#         ans = ans + item
#     return ans
#
#
# values = [(1, 2, 4), (2, 3, 6), (3, 3), (2, 3), (4, 5)]
# ans = starmap(val, values)
# print(list(ans))


'''example that differentiates map() and starmap().'''

# li = [2, 3, 4, 5, 6, 7]
#
# # adds 2 to each element in list
# ans = list(map(lambda x: x + 2, li))
# print(ans)

# print("----------------------------------------------------------------------")

'''zip()  --> as long as values finds it creates pairs'''
# val1 = [item for item in range(1, 11)]
# val2 = [item for item in range(101, 111)]
# print(val1)
# print(val2)
# ans = dict(zip(val1, val2))
# print(ans)

# print("----------------------------------------------------------------------")

'''zip_longest()  --> as long as values finds it creates pairs'''
# from itertools import zip_longest
# val1 = [item for item in range(1, 21)]
# val2 = [item for item in range(101, 111)]
# ans = dict(zip_longest(val1, val2))
# print(ans)

# from itertools import zip_longest
# val1 = [item for item in range(1, 11)]
# val2 = [item for item in range(101, 150)]
# ans = dict(zip_longest(val1, val2))
# print(ans)
#
# from itertools import zip_longest
# val1 = [10, 20, 30]
# val2 = ["A", "B", "C", "D", "E"]
# ans = zip_longest(val1, val2, fillvalue="NA")
# print(list(ans))

# print("----------------------------------------------------------------------")
'''product()
forward+backword+self'''
from itertools import product

# prodval = product('ABCD')   # repeat 1=4^1 and 2=4^2 and 3=4^3
# print(list(prodval))
#
# prodval = product('ABCD',repeat=2)   # repeat 1=4^1 and 2=4^2 and 3=4^3
# print(list(prodval))

# prodval = product('ABCD',repeat=3)   # repeat 1=4^1 and 2=4^2 and 3=4^3
# print(list(prodval))

'''permutation()
no pair with self
This method takes a list/string as an input and return an object list of tuples that contain all permutation in a list form.'''
# print("-----------------------------------------------------------------------------")
# from itertools import permutations
# p = permutations("ABCD", r=2)
# print(list(p))

# print("-----------------------------------------------------------------------------")
'''combination() -->
no self, only forward pairs'''
# from itertools import combinations
#
# p = combinations("ABCD", r=2)
# print(list(p))

# print("-----------------------------------------------------------------------------")
'''combinations_with_replacement()  --->
no self, only forward pairs'''
# from itertools import combinations_with_replacement
# p = combinations_with_replacement("ABCD", r=2)
# print(list(p))
