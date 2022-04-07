class Employee:
    no_of_leaves = 10
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole



    def printdetails(self):
        return f" name is {self.name}. Salary is {self.salary} and role is {self.role}"
    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves
    def __add__(self, other):
        return self.salary + other.salary
    def __truediv__(self, other):
        return self.salary / other.salary
    def __repr__(self):
        return f" Employee( '{self.name}' {self.salary} '{self.role}')"

    # def __str__(self):
    #     return f" name is {self.name}. Salary is {self.salary} and role is {self.role}"

        #self.printdetails()


emp1 = Employee("kushal", 500, "CEO")
# emp2 = Employee("rohan", 20, "Cleaning")
#
# print(emp1 + emp2)
# print(emp1 / emp2)
print(repr(emp1))
# print(str(emp1))
