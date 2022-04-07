dokan = ["chini", "dal", "masuro", "gahu", "200"]
print(dokan)

print(dokan[3])
numbers = [2,11,3,45,9,111]
numbers.sort()
print(numbers)
numbers.sort()
numbers.reverse()
print(numbers)
print(numbers[0:4])
print(numbers[0:4:2])
print(len(numbers))
print(min(numbers))
print(max(numbers))
numbers = [1,3,5,7,9,11,44]
numbers.append(444)
numbers.append(22)
print(numbers)
numbers = [4,7,11,34,555]
numbers.insert(1, 55)
numbers.insert(4, 777)
numbers.remove(34)
numbers.pop() #pop removes the last element
print(numbers)
numbers = [11,22,33,44]
numbers[2] =123
print(numbers)
#mutable = can be chaged
#immutable = cannot be changed
tp = (1,2,3,4)
# tp[2] = 444 it will be error cause tuple tp is immutable
print(tp)
a = 1
b = 4
# temp = a
# a = b
# b + temp this method is traditional for interchanging values. lets use python
a, b = b, a
print(a,b)






