"""
len() ----> __len__ 
index using [ ] ----> __getitem__(index)
names[0] = some_value   ----> __setitem__(index, value)
in -----> __contains__(item)
"""
class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __len__(self):
        print("executing __len__")
        return 2
    
    def __contains__(self, item):
        if item in self.__dict__.values():   # 10 in [10, 20].__contians__(1)
            return True
        return False
    
    def __getitem__(self, index):
        if index == 0:
            return self.a
        elif index == 1:
            return self.b
        else:
            raise Exception("Point Object is out of index")
        
    def __setitem__(self, index, value):
        if index == 0:
            self.a = value
        elif index == 1:
            self.b = value
        else:
            raise Exception("Point Object is out of index")
    
    def __eq__(self, other):
        if self.a == other.a and self.b == other.b:
            return True
        return False
    
    def __gt__(self, other):
        if self.a + self.b > other.a + other.b:
            return True
        return False
    
    def __lt__(self, other):
        if self.a + self.b < other.a + other.b:
            return True
        return False
    
    def __add__(self, other):
        x = self.a + other.a
        y = self.b + other.b
        return Point(x, y)
    
    def __sub__(self, other):
        x = self.a - other.a
        y = self.b - other.b
        return Point(x, y)
    
    def __mul__(self, other):
        x = self.a * other.a
        y = self.b * other.b
        return Point(x, y)


p1 = Point(1, 2)
p2 = Point(1, 2)


# class PositivePoint(Point):
#     def __init__(self, a, b):
#         super().__init__(a, b)
    
#     def __setitem__(self, index, item):
#         if item < 0:
#             raise Exception(f"Cannot set the negative value at index {index}")
#         super().__setitem__(index, item)

# class RangePoint(Point):
#     def __init__(self, a, b):
#         super().__init__(a, b)

#     def __setitem__(self, index, value):
#         if index == 0:
#             if value in range(1, 101):
#                 super().__setitem__(index, value)
#             else:
#                 raise Exception('Can set value of "a" between 1-100')
#         elif index == 1:
#             if value in range(1, 51):
#                 super().__setitem__(index, value)
#             else:
#                 raise Exception('Can set value of "b" between 1-50')
#         else:
#             raise Exception("Index out of range")
