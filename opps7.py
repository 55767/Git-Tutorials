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






kushal = Employee("kushal", 100, "CEO")
binod = Employee("binod", 50, "branch manager")

kushal.printgood("kushal")



