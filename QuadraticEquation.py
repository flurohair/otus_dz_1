#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 00:42:00 2023
ax^2 + bx + c = 0

@author: anton
"""
import sys
import math

e = sys.float_info.epsilon

def solve (a,b,c,e):
    # Примечание. Учесть, что a имеет тип double и сравнивать с 0 через == нельзя.
    if abs(a)<=e: 
        print ('Ошибка: \'a\' не должно быть равно нулю') 
        raise ValueError('\'a\' не должно быть равно нулю')

    # abc не NAN
    if math.isnan(a) or math.isnan(b) or math.isnan(c): 
        print ('Ошибка: \'a,b,c\' не могут быть NaN') 
        raise ValueError('\'a,b,c\' не могут быть NaN')

    # abc не infinity
    if math.isinf(a) or math.isinf(b) or math.isinf(c): 
        print ('Ошибка: \'a,b,c\' не могут быть Infinity') 
        raise ValueError('\'a,b,c\' не могут быть Infinity')
    
    # дискриминант
    d = b ** 2 - 4 * a * c;
    print ("d =", "{:.50f}".format(d))
    if d < -e :
        print ("Нет вещественных корней")
        return []
    if d > e : 
        print ("Два вещественных корня")
        return [-b+math.sqrt(d)/(2*a),-b-math.sqrt(d)/(2*a)]
    if abs(d) <= e : 
        print ("Один вещественный корень")
        return [-b/(2*a),-b/(2*a)]


#print (solve (1,0,e/4,e))





