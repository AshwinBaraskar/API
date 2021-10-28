
"""Iterables: It is something that can be loop over"""

'''Iterable is an object, which one can iterate over. It generates an Iterator when passed to iter() method. 

Iterator is an object, which is used to iterate over an iterable object using __next__() method. Iterators
 have __next__() method, which returns the next item of the object.'''



# nums = [1, 2, 3]
# for num in nums:
#     print(num)

'''
1] __iter__ method that is called on initialization of an iterator. This should return an object that 
    has a next or __next__ (in Python 3) method.

2]  next ( __next__ in Python 3) The iterator next method should return the next value for 
    the iterable. When an iterator is used with a ‘for in’ loop, the for loop implicitly calls next() 
    on the iterator object. This method should raise a StopIteration to signal the end of the iteration.
'''
# nums = [1, 2, 3]
# print(dir(nums))  # it shows __iter__


# nums = [1, 2, 3]
#
# i_nums = nums.__iter__()
# # or we can write above in following way...still get the same output
# i_nums = iter(nums)
# print(i_nums)
# print(dir(i_nums))

#
# nums = [1, 2, 3]
# i_num = iter(nums)
# i_num = nums.__iter__()     # another way of representation
#
# print(next(i_num))
# print(next(i_num))
# print(next(i_num))
# # print(next(i_num))  # error
# for i in i_num:
#     print(i)

'''another characteristics of iterator is that they only go forward'''
# nums = [1, 2, 3]
# i_num = iter(nums)
# while True:
#     try:
#         item = next(i_num)
#         print(item)
#     except StopIteration:
#         break

'''Example: 1'''
'''with class'''
# class MyRange:
#     def __init__(self, start, end):
#         self.value = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.value >= self.end:
#             raise StopIteration        ##############
#         current = self.value
#         self.value += 1
#         return current
#
#
# nums = MyRange(6, 10)
#
# for num in nums:
#     print(num)

# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))  # Error

'''generator iterator'''
# def my_range(start, end):
#     current = start
#     while current < end:
#         yield current
#         current += 1
#
# nums = my_range(1, 10)
#
# for num in nums:
#     print(num)


'''to iterate infinite obj'''
# def my_range(start):
#     current = start
#     while True:
#         yield current
#         current += 1
#
# nums = my_range(90)
#
# for num in nums:
#     if num<100:
#         print(num)
#     else:
#         break


'''Example: 2'''
# class Test:
#     def __init__(self, limit):
#         self.limit = limit
#
#         # Called when iteration is initialized
#     def __iter__(self):
#         self.x = 10            # mentioning the start value
#         return self
#
#     # To move to next element. In Python 3,
#     # we should replace next with __next__
#     def __next__(self):                 # dunder method and always use __next__()
#         # Store current value of x
#         x = self.x
#         # Stop iteration if limit is reached
#         if x > self.limit:
#             raise StopIteration
#             # Else increment and return old value
#         self.x = x + 1
#         return x
# #
#     # Prints numbers from 10 to 15
# for i in Test(15):
#     print(i)
#
# # Prints nothing
# for i in Test(5):
#     print(i)

'''Example: 3'''
# Iterating over dictionary
# print("\nDictionary Iteration")
# d = dict()
# d['xyz'] = 123
# d['abc'] = 345
# print(d)
# for i in d:
#     print("%s  %d" % (i, d[i]))
#
# for i in d:
#     print((i, d[i]))


'''Example: 4'''
# class InfIter:
#     def __init__(self, limit):
#         self.limit = limit
#     """Infinite iterator to return all
#         odd numbers"""
#
#     def __iter__(self):
#         self.num = 1
#         return self
#
#     def __next__(self):       # Ans> 1 3 5
#         num = self.num
#         self.num += 2
#         return num
#
#     # def __next__(self):       # Ans> 3 5 7
#     #     self.num += 2
#     #     return self.num
#
# z = iter(InfIter(10))
# # print(next(z))
# # print(next(z))
# # print(next(z))
#
# for i in InfIter(1):
#     print(i)


'''###############'''


# values = []
# for item in range(10):
#     if item%2==0:
#         values.append(item)
# print(values)
#
# values = [item for item in range(10) if item % 2 == 0]  # short hand expression
# print(values)

########################
import sys
from itertools import count
import time
#
#
#
# def get_no_pages(size,nooflines):
#     pages = int(nooflines/size)  # 4
#     if nooflines%size>0:
#         pages+=1
#     return pages
#
# class LineIterator:
#     def __init__(self,screensize,article):
#         self.article = article
#
#         #4
#         LineIterator.noofpages = get_no_pages(screensize,len(article))
#
#         #10
#         self.nooflines = screensize   # always screensize lines
#
#         #0
#         self.start = 0
#
#         #10
#         self.stop = screensize
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.noofpages>0:
#             portion = self.article[self.start:self.stop:]
#             self.start = self.stop
#             self.stop += self.nooflines
#             LineIterator.noofpages-=1
#             return portion
#         else:
#             raise StopIteration('All lines are read')
#
#
# def read_data_from_file():
#     with open('C:\\Users\\Yogesh\\Desktop\\sample_f.txt') as file:
#         all_lines = file.readlines()
#     return all_lines

# article = read_data_from_file()
#
# lineitr = LineIterator(5,article)
# cnt = 1
# for item in iter(lineitr):
#     for lin in item:
#         print(lin.strip())
#     time.sleep(1)
#     print('PageNo : {}-------------------------------------------------'.format(cnt))
#     cnt+=1
# sys.exit(0)
#
# read_data_from_file()


# class Student:
#     allAtributes = []
#
#     def __init__(self, sid, snm, sage, sadr, marks, email):
#         self.studId = sid
#         self.studName = snm
#         self.studAge = sage
#         self.studAddress = sadr
#         self.studmarks = marks
#         self.studEmail = email
#         Student.allAtributes = list(self.__dict__.keys())          ###########
#
#     def __str__(self):
#         return f'''
#             Stud ID : {self.studId}
#             Stud Name: {self.studName}
#             Stud Age : {self.studAge}
#             Stud Address : {self.studAddress}
#             Stud Marks : {self.studmarks}
#             Stud Email : {self.studEmail}
#     --------------------------------------------------------------
#         '''
#
#     def __repr__(self):
#         return str(self)
#
#     def __iter__(self):
#         self.start = 0
#         self.stop = 2
#         self.end = len(Student.allAtributes)  # 4
#         return self
#
#     def __next__(self):
#         if self.stop <= self.end:
#             returnval = Student.allAtributes[self.start:self.stop:]              ############
#             self.start = self.stop
#             self.stop += 2                                                          ########
#             returnval = [(item, self.__dict__.get(item)) for item in returnval]
#             # print(returnval)
#             return returnval
#         else:
#             raise StopIteration("Single Student Attributes finished")
#             # return 10
#         # business logic -- what you want to deliver to one next and so on
#         # return 10
#
#
# import random
# import copy
#
# cnt = count(start=101)
#
# s1 = Student(101, "ABCD", 20, 'Pune', 88, 'abc@gmail.com')
# stud_list = []
# for item in range(100):
#     s1 = copy.deepcopy(s1)
#     s1.studId = next(cnt)
#     namechars = [chr(random.randint(65, 90)) for item in range(5, 10)]
#     s1.studName = "".join(namechars).title()
#     s1.studAge = random.randint(20, 30)
#     stud_list.append(s1)
# # print(stud_list)
#
# import time
#
# for stud in stud_list:  # iter next - - list
#     studiter = iter(stud)
#     # print(studiter)
#     for st in studiter:  # iter next -- student -- iterable
#         print(st)
#         time.sleep(1)
#     print('--------------------------------------------')


# class OwnIterator:
#     value = None  # 3
#
#     def __init__(self, val):
#         OwnIterator.value = val  # at the time of creating instance we are initialize class level  3
#         self.tablevalue = val * 10  # 30
#         self.table = 0  # 3
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         print('inside next')
#
#         # 30          #3
#         if self.tablevalue > self.table:
#             self.table = self.table + OwnIterator.value
#             return self.table  # 3
#         raise StopIteration('Completed..')  # exeuction will is going end here..
#
#
# obj = OwnIterator(4)
# table3 = iter(obj)
# #
# # import time
# #
# # for val in table3:
# #     print('val --', val)
# #     time.sleep(1)
# #
# # print('Program execution completed..!')
#
# obj1 = OwnIterator(4)
# print('Obj1 --', obj1, '--', type(obj1))
# val1 = iter(obj1)
# print('Value1', val1, '--', type(val1))
# a = next(val1)
# print('given a call to next', a, '--', type(a))

'''separate int and strings'''
# list = [1 , 2 , 3, "name", "Ashwin", 4, 5]
# l1=[]
# l2=[]
# for i in list:
#     if type(i) == int:
#         # print("Integer: ", i)
#         l1.append(i)
#
#     else:
#         l2.append(i)
#         # print("String: ",i)
#
# print("Integer: ",l1)
# print("string: ",l2)