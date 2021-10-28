'''Lambda
ref = lambda 'define variable': 'operation'
ref = filter(lambda 'define variable': 'operation', "Iterator")
'''

# def addition(x, y):
#     return x + y
# result = addition(10, 20)
# print(result)
#
# ref = lambda x, y: x + y
# print(ref(10, 30))

"----------------------------------------------------------------------------------------"

# def addition(x, y):
#     return x + y
# x = addition
# y = addition(10, 20)
# print("Function ref--memory location: ", x)  # Function ref--memory location:  <function addition at 0x000001FF24D17CA0>
# print("Actual return value: ", y)    # Actual return value:  30
#
#
# ref = lambda x, y: x+y
# x = ref
# y = ref(10, 10)
# print(x)
# print(y)

"------------------------------------------------------------------------------------"
import random

# values = [random.randint(1, 30) for item in range(10)]
# print(values)
#
#
# def find_even1(x):
#     if x % 2 == 0:
#         print("even number")
#     else:
#         print("odd number")
#
# funref1 = lambda x : x%2 ==0   # above code in one line
# print(funref1(5))
# print(funref1(50))

'''filter()
The filter() method filters the given sequence with the help of a function that tests each 
element in the sequence to be true or not.
'''
# import random

# values = [random.randint(1, 30) for item in range(10)]
# print(values)
# def find_even2(values):
#     evenlist = []
#     for item in values:
#         if item % 2 == 0:
#             evenlist.append(item)
#     return evenlist
# ref2 = find_even2(values)
# print(ref2)
# #
# funref2 = list(filter(lambda x: x % 2 == 0, values))  # above code in one line
# print(funref2)



# ages = [5, 12, 17, 18, 24, 32]
# def myFunc(x):
#   if x < 18:
#     return False
#   else:
#     return True
#
# adults = filter(myFunc, ages)
#
# print(list(adults))



"-------------------------------------------------------------------------------------"
'''filter()  -->we use condition satisfy'''
import random

DESIGNATION = ['MANAGER', 'CLERK', 'SOFTWARE ENGINEER', 'SR. SOFTWARE ENGINEER']


class Emp:
    def __init__(self, empid, empnm, empsal, empag, empdes):
        self.empId = empid
        self.empName = empnm
        self.empAge = empag
        self.empSalary = empsal
        self.empDesig = empdes

    def __str__(self):
        return f'''
            Emp Id: {self.empId}
            Emp Name: {self.empName}
            Emp Age: {self.empAge}
            Emp Salary: {self.empSalary}
            Emp Designation: {self.empDesig}

'''

    def __repr__(self):
        return str(self)


def dummy_emp(no):
    emplist = []
    for item in range(1, no):
        emplist.append(Emp(empid=item, empnm='AAA' + str(item), empsal=2456.25 + float(item),
                           empag=random.randint(22, 35), empdes=random.choice(DESIGNATION)))
    return emplist



employee = dummy_emp(10)
# print("Original List: ", employee)
#
'# If we want emp whoes designation is manager'

# def filter_only_manager(employee):
#     emplist = []
#     for emp in employee:
#         if emp.empDesig == "MANAGER":
#             emplist.append(emp)
#     return emplist
#
# #
# manager = filter_only_manager(employee)
# print('managers: ', manager)

"Implementation through lambda (Above code)"

# manager = list(filter(lambda emp:emp.empDesig=="MANAGER",employee))
# print('managers: ', manager)

"Increment of salary Implementation through lambda (Above code)"
#
# employee = dummy_emp(10)
# se = list(filter(lambda emp: emp.empDesig == "SOFTWARE ENGINEER", employee))
# print(se)
#
# for item in se:
#     final_salary = item.empSalary * 1.10
#     item.empSalary = final_salary              # #########################
#
# print("10 % increment", se)

"-------------------------------------------------------------------------------------"
'''map()
Syntax : map(fun, iter)
If we want to apply function on the iterator like list, tuple etc. then we use map function'''


# def myfunc(a):
#   return len(a)
#
# x = map(myfunc, ('apple', 'banana', 'cherry'))
# print(x)
# print(list(x))   # convert the map into a list, for readability:


# numbers = (1, 2, 3, 4)
# result = map(lambda x: x + x, numbers)
# print(list(result))

# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 6]
#
# result = map(lambda x, y: x + y, numbers1, numbers2)
# print(list(result))
"-------------------------------------------------------------------------------------"
'''difference between filter() and map()
[1,2,3,4,5]
map(lambda x: x*2 if x%2==0 else x)   -->1 4 3 8 5
filter(lambda x: x%2==0, x)           -->4 8
'''
"-------------------------------------------------------------------------------------"
'''reduce()'''
from functools import reduce

# values = [random.randint(1,5) for item in range(5)]
# print("source: ",values)
# output = sum(values)
# print("Sum: ", output)
#
# item = reduce(lambda x, y: x*y, values)
# print(item)

"-------------------------------------------------------------------------------------"
from functools import reduce

# emplist = dummy_emp(10)
#
# #
# #
# def all_emp_salary():
#     total_sal = 0.0
#     for emp in emplist:
#         total_sal = total_sal + emp.empSalary
#     return total_sal
#
#
# output1 = sum(list(map(lambda emp: emp.empSalary, emplist)))
# output2 = all_emp_salary()
# output3 = reduce(lambda emp1, emp2: emp1 +emp2, [10, 20, 30, 40])
# #
# print("Sum Using Normal Function: ", output2)
# print("Sum Using Map: ", output1)
# print("Sum Using Reduce: ", output3)
