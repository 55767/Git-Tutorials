class Employee:
    no_of_leaves = 10
    pass


kushal = Employee()
binod = Employee()

kushal.name = "kushal dotel"
kushal.salary = 100
kushal.role = "CEO"

binod.name = "binod chaudhary"
binod.salary = 80
binod.role = "branch manager"



print(kushal.salary, Employee.no_of_leaves)

Employee.no_of_leaves = 8

print(Employee.no_of_leaves)
print(binod.__dict__)
binod.no_of_leaves = 12
print(binod.__dict__)

print(binod.no_of_leaves)
print(Employee.__dict__)
