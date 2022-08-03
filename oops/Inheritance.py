
# OOPS 4
class Parent:
    def __init__(self, value):
        self.value = value

    def apple(self):
        print(f"Executing Parent Apple {self.value}")

    def google(self):
        print("Executing Parent Google")
        self.apple()
#p = Parent(10)
#p.google()


#  Case 1 : child class having Independent Method
class Child1(Parent):
    def __init__(self, value):
        # calling parent class constructor
        # super is used to call the parent class attribute
        super().__init__(value)     

    def yahoo(self):
        print("Child1 Yahoo")

#c = Child1(15)
#c.yahoo()
#c.apple()
#c.google()


#  Case 2 : Child class overriding parent class method
class Child2(Parent):
    def __init__(self, value):
        super().__init__(value)

    # method overriding
    def apple(self):
        print(f"Executing Child2 Apple {self.value}")

#c = Child2(17)
#c.apple()
#c.google()


#  Case 3 : child class overriding parent, but re-using the parent class functionality
class Child3(Parent):
    def __init__(self, value):
        super().__init__(value)

    def apple(self):
        # this is the extra functionality
        print("Executing Child3 Apple")
        # reusing the parent class functionality
        super().apple()

#c = Child3(17)
#c.apple()
#c.google()


#Case 4 : child class having a separate attribute in __init__ method
class Child4(Parent):
    def __init__(self, value, extra_value):
        # super().__init__(value)
        Parent.__init__(self, value)
        self.extra_value = extra_value

#Child4(10, 20).google()
#c.apple()
#c.google()

#Case 5 : child inheriting from multiple parents
#                                     Multiple Inheritance
class Parent2:
    def __init__(self, a):
        self.a = a

    def facebook(self):
        print("Executing Parent2 Facebook")

class Child5(Parent, Parent2):
    def __init__(self, x, y):
        Parent.__init__(self, x)
        Parent2.__init__(self, y)

    def whatsapp(self):
        print("Executing child5 Whatsapp")


#c = Child5(10, 20)
#c.facebook()
#c.whatsapp()
#c.apple()
#c.google()

##                                    Multi-level Inheritance
class A:
    def demo(self):
        print("A")

class B(A):
    def demo(self):
        print("B")
        # super().demo()
        A.demo(self)

class C(B):
    def demo(self):
        print("C")
        # super().demo()
        B.demo(self)
        
#C().demo()

##                                       Hybrid Inheritance
class Parent:
    def spam(self):
        print("Parent Spam")

class Child1(Parent):
    def spam(self):
        print("Child1 Spam")
        super().spam()

class Child2(Parent):
    def spam(self):
        print("Child2 Spam")
        super().spam()

class Child3(Child1, Child2):
    def spam(self):
        print("Child3 Spam")
        super().spam()
    pass

c = Child3()
c.spam()

# __mro__(Method Resolution Order) is the order in which python looks up for an attribute in inheritance hierarchy
# Child3.__mro__
class Spam:
    a = 10  #class variable
    def apple(self):
        print(f"Spam Apple {Spam.a}")
        print(f"Spam Apple {self.__class__.a}")

class Demo(Spam):
    # overriding class variable
    a = 20 # class variable
    def google(self):
        print("Google")


















