#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 06:33:58 2020

@author: JeffHalley
"""
from collections.abc import Generator


class etlgen(Generator):
    def __init__(self, final_val):
        self.final_val = final_val
        self.current_val = 0

    def has_next(self):
        if self.current_val < self.final_val + 1:
            return True
        else:
            return False

    def send(self):
        return_value = self.current_val
        self.current_val += 1
        if self.current_val <= self.final_val + 1:
            return return_value
        else:
            self.throw(self)

    def throw(self, type=None, value=None, traceback=None):
        raise StopIteration
            
           

class etlconsume:
    def __init__(self,etlgen):
        self.results = []
        self.etlgen = etlgen
        while etlgen.has_next():
            self.results.append(self.etlgen.send())
        