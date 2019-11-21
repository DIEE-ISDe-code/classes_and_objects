#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import polygons as pol
#a=pol.Polygon() 
#TypeError: Can't instantiate abstract class Polygon with abstract methods compute_area

b=pol.Rectangle([1,2,1,2])
c=pol.Triangle([1,1,1.4142])
print(b.compute_area())
print(c.compute_area())