class Employee:
    no_of_leaves = 10
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole



    def printdetails(self):
        return f" name is {self.name}. Salary is {self.salary} and role is {self.role}"



kushal = Employee("kushal", 100, "CEO")
# binod = Employee()
#
# kushal.name = "kushal dotel"
# kushal.salary = 100
# kushal.role = "CEO"
#
# binod.name = "binod chaudhary"
# binod.salary = 80
# binod.role = "branch manager"
#
# print(binod.printdetails())
# print(kushal.printdetails())
# print(kushal.no_of_leaves)

print(kushal.role)
