# num = [1,2,3,4,5,6]
# square = list(map(lambda x: x*x, num))
# print(square)

# def square(a):
#     return a*a
#
# def cube(a):
#     return a*a*a
#
# func = [square,cube]
# for i in range(5):
#     value = list(map(lambda x:x(i),func))
#     print(value)

# list_1 = [1,2,3,4,5,6]
# def is_greater_5(num):
#     return num>5
#
# gr_than_5 = list(filter(is_greater_5, list_1))
# print(gr_than_5)

from functools import reduce
list2 = [1,2,4,5]
num = reduce(lambda x,y: x+y, list2)
print(num)