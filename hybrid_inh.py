# Base class
class A:
    def show_A(self):
        print("Class A")

# Derived class inheriting from A
class B(A):
    def show_B(self):
        print("Class B")

# Another derived class inheriting from A
class C(A):
    def show_C(self):
        print("Class C")

# Class D inherits from both B and C (Hybrid Inheritance)
class D(B, C):
    def show_D(self):
        print("Class D")

# Creating an object of class D
obj = D()

# Calling methods from different classes
obj.show_A()  # From Class A
obj.show_B()  # From Class B
obj.show_C()  # From Class C
obj.show_D()  # From Class D
