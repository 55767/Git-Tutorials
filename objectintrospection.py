class Businessman:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@withkushal.dotel ."

    def explain(self):
        return f"This businessman is {self.fname}  {self.lname} . "


    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set. Please set it using setter."

        return f"{self.fname}.{self.lname}@withkushal.dotel "

    @email.setter
    def email(self, string):
        print("setting now....")
        names =  string.split ("@") [0]
        self.lname = names.split(".")[0]
        self.fname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


skillf = Businessman("skill","F")
# print(skillf.email)

# print(type(skillf))
print(id("hellow"))
# print(id("k xa bhai"))
# o = "k xa vai"?
# print(dir(skillf))

import inspect
print(inspect.getmembers(skillf))
