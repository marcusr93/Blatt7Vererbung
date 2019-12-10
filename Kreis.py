# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:40:28 2019

@author: User
"""

from math import pi

class kreis:

    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def get_area_c(self):
        return self.radius**2 * pi
    def get_perimeter_c(self):
        return 2 * self.radius * pi
