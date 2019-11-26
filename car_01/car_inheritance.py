#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


"""


class Engine():
    def __init__(self,displacement=1000):
        self.displacement=displacement

class EngineWithWheels(Engine):
    def __init__(self,displacement=1000, nWheels=4):
        super().__init__(displacement)
        self.nWheels=nWheels
        
class Car(EngineWithWheels):
    def __init__(self,displacement=1000, nWheels=4, nSeats=5):
        super().__init__(displacement, nWheels)
        self.nSeats=nSeats
        
                
a=Car(2000,5, 7)

print(a.displacement)
print(a.nWheels)
print(a.nSeats)
 