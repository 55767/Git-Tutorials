class A:
    classvar1 = "i am in class A"
    def __init__(self):
        self.var1 = "i am inside class A's constructor"
        self.special = " super special"
        self.classvar1 = " i am a good boy."

class B(A):
    def __init__(self):
        # super().__init__()
        self.var1 = "i am inside class B's constructor"
        self.classvar1 = " i am a bad boy."
        super().__init__()
        print(super().classvar1)

    # classvar1 = " i am inside class b"
    classvar2 = " i am inside class b"



a = A()
b = B()

print(b.special, b.var1,b.classvar1 )