#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:14:56 2020

@author: JeffHalley
"""

class EtlTransformer:
    def __init__(self,EtlExtractor,key_col_name,value_col_name, 
                 counts_per_type={},total_counts=0,
                 sums_of_values_per_type={},frequency_of_type={}, 
                 average_price_of_type={},test_row=None):
        
        self.EtlExtractor = EtlExtractor
        self.key_col_name = key_col_name
        self.value_col_name = value_col_name
        self.counts_per_type = counts_per_type
        self.total_counts = total_counts
        self.sums_of_values_per_type = sums_of_values_per_type
        self.average_price_of_type = average_price_of_type
        self.frequency_of_type = frequency_of_type
        self.invalid_rows = []
        self.test_row = test_row
        
        while self.EtlExtractor.has_next():
            cur_row = EtlExtractor.send()
            cur_row_key = cur_row[key_col_name]['type'](
                    cur_row[key_col_name]['value'])
            cur_row_value = cur_row[value_col_name]['type'](
                    cur_row[value_col_name]['value'])
            
            try:
                self.counts_per_type[cur_row_key] += 1
                self.sums_of_values_per_type[cur_row_key] += cur_row_value
                self.total_counts += 1
                
            except KeyError:
                self.counts_per_type[cur_row_key] = 1
                self.sums_of_values_per_type[cur_row_key] = cur_row_value
                self.total_counts += 1
                
            except TypeError:
                    print('Invalid row found because of data_type  it was not \
                          counted and it was stored in the invalid_rows attribute')
                    self.invalid_rows.append(cur_row)
                
            except ValueError:
                    print('Invalid row found, it was not counted \
                          and stored in the invalid_rows attribute')
                    self.invalid_rows.append(cur_row)
                        
            
            
            
        