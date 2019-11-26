#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

from abc import ABC, abstractmethod
class Polygon(ABC):
	def __init__(self, sides):
		self.sides = sides
			
	@abstractmethod
	def compute_area(self): #you are forced to redefine this method
		pass;

class Rectangle(Polygon):

    def compute_area(self):  # you are forced to redefine this method
        return self.sides[0]*self.sides[1]

class Triangle(Polygon):
    def compute_area(self):  # you are forced to redefine this method
        # https://en.wikipedia.org/wiki/Heron%27s_formula
        p=sum(self.sides)/2
        area=math.sqrt(p*(p-self.sides[0])*(p-self.sides[1])*(p-self.sides[2]))
    
    

        # A=sqrt(p*(p-a)*(p-b)*(p-c))
        return area
