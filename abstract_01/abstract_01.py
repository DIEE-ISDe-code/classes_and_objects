#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


"""

from abc import ABC, abstractmethod

class Z(ABC):
    def __init__(self):
        self.z=0
        self._post_init()
    @abstractmethod    
    def _post_init(self):
        pass

class A(Z):
    def _post_init(self):
        self.a=0
        
class B(Z):
    def _post_init(self):
        self.b=0
                
a=A()
b=B()
print(a.z)
print(a.a)
print(b.z)
print(b.b)
