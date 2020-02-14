#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 09:02:55 2020

@author: JeffHalley
"""

from collections.abc import Generator
import csv

class EtlCsvExtractor(Generator):
    def __init__(self,csv_file_path, key_column, value_column, csv_headers=[], 
                 csv_col_data_types=[], test_row=None):
        
        self.csv_file_path = csv_file_path
        self.key_column = key_column
        self.value_column = value_column
        self.csv_headers = csv_headers
        self.csv_col_data_types = csv_col_data_types
        
        self.first_row = None
        
        if self.csv_file_path != 'test':
            self.csv_file = open(self.csv_file_path, "r")
            self.reader = csv.reader(self.csv_file)
            if not self.csv_headers:
                self.csv_headers = next(self.reader)
            if not self.first_row:
                self.first_row = next(self.reader)
            self.get_col_data_types()
            self.get_key_column_index()
            self.get_value_column_index()
        
        #self.next_row =[x(y) for x,y in zip(self.csv_col_data_types, self.first_row)]
        
        # convert csv row into a json-like dict
        self.next_row = {k:{'value':v,'type':vtype} for\
                         k,v,vtype in zip(self.csv_headers,
                                          self.first_row,
                                          self.csv_col_data_types)}  
    
    @staticmethod       
    def get_cell_data_type(cell):
        try:
            data_type = type(int(cell))
        except ValueError:
            try:
                data_type = type(float(cell))
            except ValueError:
                    data_type = type(cell)
        return data_type
    
    def get_col_data_types(self):
        if not self.csv_col_data_types:
            self.csv_col_data_types = [self.get_cell_data_type(x)\
                                       for x in self.first_row]     
           
  
    def get_key_column_index(self):
        if type(self.key_column) != int:
            if type(self.key_column) == str:
                self.key_column = self.csv_headers.index(self.key_column)
            else:
                raise Exception('Key column must either be\
                                int for column index or string for column name')
    
    def get_value_column_index(self):
        if type(self.value_column) != int:
            if type(self.value_column) == str:
                self.value_column = self.csv_headers.index(self.value_column)
            else:
                raise Exception('Value column must either be int for\
                                column index or str for column name')
        if self.csv_col_data_types[self.value_column] not in (int,float):
            raise Exception('Value column must either int or float type')
    
    def has_next(self):
        if self.next_row:
            return True
        else:
            return False
    
    def send(self):
        if self.next_row:
            row_to_send = self.next_row
            try:
                #self.next_row = [x(y) for x,y in zip(self.csv_col_data_types, next(self.reader))]
                self.next_row = {k:{'value':v,'type':vtype} for\
                                 k,v,vtype in zip(self.csv_headers,
                                                  next(self.reader),
                                                  self.csv_col_data_types)}
            except StopIteration:
                self.next_row = None
                self.csv_file.close()
            return row_to_send
        else:
            self.throw()
      
    def throw(self, type=None, value=None, traceback=None):
        raise StopIteration           
    
    
               