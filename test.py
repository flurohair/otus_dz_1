#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 02:05:40 2023

@author: anton
"""
import sys
import unittest
from QuadraticEquation import solve

e = sys.float_info.epsilon



class TestQuadraticEquasion(unittest.TestCase):
 
    # вспомогательная функция для проверки массивов из 2х элементов ))
    def assertArr(self, arr1, arr2, e):
        self.assertAlmostEqual(arr1[0], arr2[0], delta=e)
        self.assertAlmostEqual(arr1[1], arr2[1], delta=e)
        
    # 3 Написать тест, который проверяет, что для уравнения x^2+1 = 0 корней нет 
    # (возвращается пустой массив)   
    def test_no_roots(self):
        self.assertListEqual(solve(1,0,1,e), [])

    # 5 Написать тест, который проверяет, что для уравнения x^2-1 = 0 есть 
    # два корня кратности 1 (x1=1, x2=-1)
    def test_two_roots(self):
        self.assertArr(solve(1,0,-1,e), [1.0,-1.0], e)
        
    # 7 Написать тест, который проверяет, что для уравнения x^2+2x+1 = 0 есть 
    # один корень кратности 2 (x1= x2 = -1).
    def test_one_root(self):
        self.assertArr(solve(1,2,1,e), [-1.0,-1.0], e)
        
    # 9 Написать тест, который проверяет, что коэффициент a не может быть 
    # равен 0. В этом случае solve выбрасывает исключение.
    def test_a_not_null(self):
        with self.assertRaises(ValueError):
            solve(0,2,1,e)
            
    # 11 С учетом того, что дискриминант тоже нельзя сравнивать с 0 через знак 
    # равенства, подобрать такие коэффициенты квадратного уравнения для 
    # случая одного корня кратности два, чтобы дискриминант был отличный 
    # от нуля, но меньше заданного эпсилон. Эти коэффициенты должны заменить 
    # коэффициенты в тесте из п. 7.
    def test_d_not_null(self):
        self.assertArr(solve(1,0,e/4,e), [0,0], e)
        #self.assertListEqual(solve(1,0,e/3,e), [0,0])
    
    # Посмотреть какие еще значения могут принимать числа типа double, 
    # кроме числовых и написать тест с их использованием на все коэффициенты. 
    # solve должен выбрасывать исключение.
    def test_abc_not_nan(self):
        n = float('NaN')
        with self.assertRaises(ValueError):
            solve(n,n,n,e)

    def test_abc_not_inf(self):
        inf = float('Inf')
        with self.assertRaises(ValueError):
            solve(inf,inf,inf,e)
        with self.assertRaises(ValueError):
            solve(-inf,-inf,-inf,e)            
            

if __name__ == '__main__':
    unittest.main()