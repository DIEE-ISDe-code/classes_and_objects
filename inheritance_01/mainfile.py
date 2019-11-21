#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import contact


a=contact.Contact('pippo', 'pippo@gmail.com')
b=contact.Supplier('pluto', 'pluto@gmail.com')
c=contact.Friend('paperino', 'pape@gmail.com', '131313')
d=contact.Friend('gastone', 'gasto.gmail.com', '777777')


print(a.who_I_am())
print(b.who_I_am())
print(c.who_I_am())
print(d.who_I_am())
print(d.phone)
b.order('aThing')
