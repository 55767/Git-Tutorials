# public -
# protected -
# private -
#
#

class Employee:
    var = 10
    _protect = 8
    __private = 70
    no_of_leaves = 10 # yo public variable bhayo like expose garna milxa.
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole



    def printdetails(self):
        return f" name is {self.name}. Salary is {self.salary} and role is {self.role}"
    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves

    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1],params[2])
        return cls (*string.split("-"))
        pass
    @staticmethod
    def printgood(string):
        print("this is best " + string)

kus = Employee("don", 30, "CDO")
print(kus._protect)
# print(kus.__private)
print(kus._Employee__private)

# name mangling in python yo process ko name.