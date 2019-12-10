# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:48:56 2019

@author: User
"""

class Rechteck:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def get_width(self):
        return self.width
    def get_length(self):
        return self.length
    def get_area_r(self):
        return self.width * self.length
    def get_perimeter_r(self):
        return 2 * (self.width + self.length)
