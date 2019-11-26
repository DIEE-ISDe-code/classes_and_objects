#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


"""


class Engine():
    def __init__(self,displacement=1000):
        self.displacement=displacement

class Wheel():
    def __init__(self,pressure=100):
        self.pressure=pressure

class Seat():
    def __init__(self, color=1):# 1, 2, 3
        self.color=color
        
class Car():
    def __init__(self,engine,wheels, seats):
        self.engine=engine
        self.wheels= wheels  
        self.seats=seats
        
 
engine=Engine()
wheels=[Wheel() for i in range(4) ]
seats=[Seat(color=3)  for i in range(4)]  
 
car=Car(engine,wheels, seats)

print('\nENGINE')
print(car.engine)
print('\nSEATS')
print(car.seats)
print('\nWHEELS')
print(car.wheels)
print('\nPRESSURE')
print(car.wheels[0].pressure)
wheels[0].pressure=10
print(car.wheels[0].pressure)