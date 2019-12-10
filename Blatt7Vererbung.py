# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:59:01 2019

@author: User
"""

import random
import numpy as np
from Kreis import kreis
from rechteck import Rechteck

class Formen:
    '''Definiere wie es in Aufgabe 2 verlangt ist:'''
    def flaeche(self):
        return
    def umfang(self):
        return
    def volumen(self):
        return 'Die Berechnung des Volumens ist noch nicht näher spezifiziert.'

class rechteck(Formen):
    '''rechteck erbt von Formen'''
    def __init__(self, laenge, breite):
        self.laenge = laenge
        self.breite = breite
    def flaeche(self):
        area = self.laenge * self.breite
        return area
    def umfang(self):
        perimeter = 2 * self.laenge + 2 * self.breite
        return perimeter
class Kreis(Formen):
    '''Kreis erbt von Formen'''
    def __init__(self, radius):
        self.radius = radius
    def flaeche(self):
        area = self.radius**2 * np.pi
        return area
    def umfang(self):
        perimeter = self.radius * 2 * np.pi
        return perimeter
class Quader(Rechteck):
    '''Quader erbt laut Aufgabenstellung von Rechteck'''
    def __init__(self, laenge, breite, hoehe):
        self.laenge = laenge
        self.breite = breite
        self.hoehe = hoehe
    def volumen(self):
        volume = self.laenge * self.breite * self.hoehe
        return volume

'''Ab hier ist die alte Aufgabe 3 aus dem 6.Übungsblatt, welche ich von der \n Besprechung aus der letzten Übungseinheit übernommen habe.'''

for i in range(10):
    x = random.randint(1, 10)
    
A1 = kreis(x)
A2 = Rechteck(x, x)
print('Flächeninhalt Kreis: ' + str(A1.get_area_c()) + 'm²')
print('Umfang Kreis: ' + str(A1.get_perimeter_c()) + 'm²')
print('Flächeninhalt Rechteck:' + str(A2.get_area_r()) + 'm²')
print('Umfang Rechteck: ' + str(A2.get_perimeter_r()) + 'm²')

def Zufallszahl():
    number = random.randint(1, 50)
    return number

Form = []
for i in range(10):
    y = random.choice(['Rechteck', 'Kreis'])
    Form.append(y)
    
areas_c = []
perimeters_c = []
areas_r = []
perimeters_r = []

for i in Form:
    if i == 'Rechteck':
        length = Zufallszahl()
        width = Zufallszahl()
        R_i = Rechteck(length, width)
        
        areas_r.append(R_i.get_area_r())
        perimeters_r.append(R_i.get_perimeter_r())
    elif i == 'Kreis':
        radius = Zufallszahl()
        K_i = kreis(radius)
        
        areas_c.append(K_i.get_area_c())
        perimeters_c.append(K_i.get_perimeter_c())

    print('Fläche aller Kreise: ' + str(areas_c) + 'm²')
    print('Umfang aller Kreise:' + str(perimeters_c) + 'm²')
    print('Fläche aller Rechtecke: ' + str(areas_r) + 'm²')
    print('Fläche aller Rechtrecke: ' + str(perimeters_r) + 'm²')
