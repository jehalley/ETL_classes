#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 06:50:11 2020

@author: JeffHalley
"""
import csv

class CsvAggregator():
    
    def __init__(self,csv_file_path):
        self.csv_file_path = csv_file_path
        self.csv_headers = []
        self.csv_col_data_types = []
        self.counts_per_type = {}
        self.total_counts = 0
        self.sums = {}
        self.frequency_of_type = {}
        self.frequency_of_type = self.get_frequency_of_type()
        self.average_price_of_type = {}
        self.average_price_of_type = self.get_average_price_of_type()
    
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
                self.csv_col_data_types = [self.get_cell_data_type(x) for x in next(reader)]     
    
    def get_csv_headers(self):
        if not self.csv_headers:
            with open(self.csv_file_path, "r") as csv_file:
                reader = csv.reader(csv_file)
                #read in headers and remove whitespace and spaces between words
                self.csv_headers = [x.strip().replace(' ','_') for x in next(reader)]
                
    def read_and_aggregate_csv(self):
        if not self.csv_headers:
            self.get_csv_headers()
        if not self.csv_col_data_types:
            self.get_col_data_types()
        with open(self.csv_file_path, "r") as csv_file:
            reader = csv.reader(csv_file)
            #advance to the first row
            next(reader)
            for row in reader:
                self.total_counts += 1
                converted_row = [x(y) for x,y in zip(self.csv_col_data_types,row)]
                if converted_row[3] in self.counts_per_type:
                    self.counts_per_type[converted_row[3]] += 1
                    # don't have a price so using 'aisle_id' as stand in
                    self.sums[converted_row[3]] += converted_row[2]
                else:
                    self.counts_per_type[converted_row[3]] = 1
                    self.sums[converted_row[3]] = converted_row[2]
            
    def get_frequency_of_type(self):
        if not self.frequency_of_type:
            if not self.counts_per_type or not self.total_counts:
                self.read_and_aggregate_csv()
        return {k:(v/self.total_counts) for k,v in self.counts_per_type.items()}
    
        
    def get_average_price_of_type(self):
        if not self.average_price_of_type:
            if not self.sums or not self.counts_per_type:
                self.read_and_aggregate_csv()
        return {k:(self.sums[k]/self.counts_per_type[k]) for k in self.sums.keys()} 
    
        
        
        
        