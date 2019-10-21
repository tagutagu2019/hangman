# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 22:05:30 2019

@author: buji1
"""
"""
#---1---
class Square:
    square_list = []
    
    def __init__(self, length):
        self.length = length
        self.square_list.append(self.length)

    def calculate_perimeter(self):
        return 4 * self.length
    
a_square = Square(5)
b_square = Square(50)
c_square = Square(500)

print(Square.square_list)
"""
#---2---
class Square:
    square_list = []
    
    def __init__(self, length):
        self.length = length
        self.square_list.append(self.length)
       
    def calculate_perimeter(self):
        return 4 * self.length
    
    def __repr__(self):
        return "{} by {} by {} by {}".format(self.length,self.length,self.length,self.length)

    
a_square = Square(10)
print(a_square)
"""
#---3---
class Two_num:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    
    def check_num(self):
        if self.n1 is self.n2:
            return "True"
        else:
            return "False"
    
nums1 = Two_num(1,2)
nums2 = Two_num(1,1)
print(nums1.check_num())
print(nums2.check_num())
"""