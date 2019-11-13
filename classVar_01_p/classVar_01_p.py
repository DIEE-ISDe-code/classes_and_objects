#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 10:47:49 2019

@author: didaci
"""

class Cat:

    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def getSpecies(cls):
        return cls.species

a=Cat('Fizz',3)
b=Cat('felix',2)
