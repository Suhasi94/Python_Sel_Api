# Non-Pythonic approach of writing getters and setters
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_radius(self):
        return self.radius
    
    def set_radius(self, value):
        if not isinstance(value, (int, float)):
            raise Exception("Radius must be an int or float")
        self.radius = value

    def circumference(self):
        return 2 * 3.14 * self.radius

class Circle:
    def __init__(self, radius):
        # private attribute. It is for internal use only
        # You are not suppose to access this attribute directly or change the value
        # You will be able to do it.. but you should not do it.
        # If you do it, then you might end up screwing up something
        self.radius = radius
    
    # Getter
    @property
    def radius(self):
        print("Getting...")
        return self._radius
    
    # Setter
    @radius.setter
    def radius(self, value):
        print("Setting...")
        if not isinstance(value, (int, float)):
            raise Exception("Only Numbers are allowed")
        self._radius = value

    def circumference(self):
        return 2 * 3.14 * self._radius

class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
    
    @property
    def pay(self):
        return self._pay
    
    @pay.setter
    def pay(self, value):
        if not isinstance(value, (int, float)):
            raise Exception("Pay should be a number")
        self._pay = value       # creates an internal variable by "_pay" and assigns value

    @property
    def fname(self):
        return self._fname
    
    @fname.setter
    def fname(self, value):
        if len(value) > 5:
            raise Exception("Fname cannot be more than 5 characters")
        self._fname = value

    def pay_raise(self, percent):
        hike_amount = self.pay * percent
        self.pay = self.pay + hike_amount

class BankAccount:
    # Class Variable
    _interest_rate = 0.04

    def demo(self):
        # self._interest_rate 
        # BankAccount._interest_rate
        # self.__class__._interest_rate
        print(f"Interest Rate: {self.__class__._interest_rate}")


class SBAccount(BankAccount):
    # Overriding class variable in child class
    _interest_rate = 0.05

class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    # private function or it is for internal use only
    def _is_int(self, number):
        if not isinstance(number, int):
            raise Exception
        return True

    @property
    def a(self):
        return self._a
    
    @a.setter
    def a(self, value):
        if self._is_int(value):
            self._a = value

    @property
    def b(self):
        return self._b
    
    @b.setter
    def b(self, value):
        if self._is_int(value):
            self._b = value
