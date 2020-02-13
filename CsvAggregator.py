#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 06:50:11 2020

@author: JeffHalley
"""
import csv

class CsvAggregator():
    
    def __init__(self,csv_file_path, key_column,value_column, csv_headers=[], 
                 csv_col_data_types=[], counts_per_type={},
                 total_counts=0,sums={},frequency_of_type={}, 
                 average_price_of_type={}):
        
        self.csv_file_path = csv_file_path
        self.key_column = key_column
        self.value_column = value_column
        self.csv_headers = csv_headers
        self.csv_col_data_types = csv_col_data_types
        self.counts_per_type = counts_per_type
        self.total_counts = total_counts
        self.sums = sums
        self.average_price_of_type = average_price_of_type
        self.frequency_of_type = frequency_of_type
        self.invalid_rows = []
        
        # set member variables from csv file
        self.get_csv_headers()
        self.get_col_data_types()
        self.get_key_column_index()
        self.get_value_column_index()
        self.get_frequency_of_type()
        self.get_average_price_of_type()
    
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
            with open(self.csv_file_path, "r") as csv_file:
                reader = csv.reader(csv_file)
                #advance to the first row
                next(reader)
                #read in first row and determine data types
                self.csv_col_data_types = [self.get_cell_data_type(x)\
                                           for x in next(reader)]     
    
    def get_csv_headers(self):
        if not self.csv_headers:
            with open(self.csv_file_path, "r") as csv_file:
                reader = csv.reader(csv_file)
                #read in headers and remove whitespace and spaces between words
                self.csv_headers = [x.strip().replace(' ','_')\
                                    for x in next(reader)]
    
    def get_key_column_index(self):
        if type(self.key_column) != int:
            if type(self.key_column) == str:
                self.key_column = self.csv_headers.index(self.key_column)
            else:
                raise Exception('Key column must either be\
                                column index or column name')
    
    def get_value_column_index(self):
        if type(self.value_column) != int:
            if type(self.value_column) == str:
                self.value_column = self.csv_headers.index(self.value_column)
            else:
                raise Exception('Value column must either be int for\
                                column index or str for column name')
        if self.csv_col_data_types[self.value_column] not in (int,float):
            raise Exception('Value column must either be a numeric data type')
            
             
    def read_and_aggregate_csv(self):
        with open(self.csv_file_path, "r") as csv_file:
            reader = csv.reader(csv_file)
            #advance to the first row
            next(reader)
            for row in reader:
                try:
                    converted_row = [x(y) for\
                                     x,y in zip(self.csv_col_data_types,row)]
                    self.total_counts += 1
                    
                    try:
                        converted_row[self.key_column] in self.counts_per_type
                        self.counts_per_type[converted_row[self.key_column]] += 1
                        # don't have a price so using 'aisle_id' as stand in
                        self.sums[converted_row[self.key_column]]\
                        += converted_row[self.value_column]
                    except KeyError:
                        self.counts_per_type[converted_row[self.key_column]] = 1
                        self.sums[converted_row[self.key_column]]\
                        = converted_row[self.value_column]
                except TypeError:
                    print('Invalid data type for column')
                
                except ValueError:
                    print('Invalid row found, it was not counted\
                          and stored in the invalid_rows attribute')
                    self.invalid_rows.append(row)
                
    def get_frequency_of_type(self):
        if not self.frequency_of_type:
            if not self.counts_per_type or not self.total_counts:
                self.read_and_aggregate_csv()
        self.frequency_of_type = {k:(v/self.total_counts)\
                                  for k,v in self.counts_per_type.items()}
    
        
    def get_average_price_of_type(self):
        if not self.average_price_of_type:
            if not self.sums or not self.counts_per_type:
                self.read_and_aggregate_csv()
        self.average_price_of_type = {k:(self.sums[k]/self.counts_per_type[k])\
                                      for k in self.sums.keys()} 
    
        
        
        
        