#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 20:16:38 2020

@author: JeffHalley
"""

def test_get_cell_data_type():
    test_csv_ag = CsvAggregator(csv_file_path='test', key_column=0,
                                value_column=1, csv_headers=1, 
                                csv_col_data_types=[], counts_per_type=1,
                                total_counts=1,sums=1,frequency_of_type=1, 
                                average_price_of_type=1,test_row=None)
    types = ['foo','1','1.00']
    
    assert [test_csv_ag.get_cell_data_type(x) for x in types] == [str,int,float]
    
def test_get_col_data_type():
    mock_row = ['foo','1','1.00']
    test_csv_ag = CsvAggregator(csv_file_path='test', key_column=0,
                                value_column=1, csv_headers=1, 
                                csv_col_data_types=None, counts_per_type=1,
                                total_counts=1,sums=1,frequency_of_type=1, 
                                average_price_of_type=1,test_row=mock_row)
    
    assert test_csv_ag.csv_col_data_types == [str,int,float]


def test_get_csv_headers():
    mock_row = ['foo','1','baz']
    
    mock_types = [str,int,float]
    test_csv_ag = CsvAggregator(csv_file_path='test', key_column=0,
                                value_column=1, csv_headers=1, 
                                csv_col_data_types=mock_types, counts_per_type=1,
                                total_counts=1,sums=1,frequency_of_type=1, 
                                average_price_of_type=1,test_row=mock_row)
    assert test_csv_ag.csv_headers == ['foo','1','baz']

def test_get_key_column_index():
    mock_row = ['foo','1','baz']
    mock_types = [str,int,float]
    test_csv_ag = CsvAggregator(csv_file_path='test', key_column='foo',
                                value_column=1, csv_headers=mock_row, 
                                csv_col_data_types=mock_types, counts_per_type=1,
                                total_counts=1,sums=1,frequency_of_type=1, 
                                average_price_of_type=1, test_row=mock_row)
    assert test_csv_ag.key_column == 0

def test_get_value_column_index():
    mock_row = ['foo','1','baz']
    mock_types = [str,int,float]
    test_csv_ag = CsvAggregator(csv_file_path='test', key_column='foo',
                                value_column='1', csv_headers=mock_row, 
                                csv_col_data_types=mock_types, counts_per_type=1,
                                total_counts=1,sums=1,frequency_of_type=1, 
                                average_price_of_type=1, test_row=mock_row)
    assert test_csv_ag.value_column == 1

def test_get_frequency_of_type():
    mock_row = ['foo','1','1.00']
    mock_counts = {1:100,2:200,3:300}
    test_csv_ag = CsvAggregator(csv_file_path='test', key_column=0,
                                value_column=1, csv_headers=1, 
                                csv_col_data_types=None, counts_per_type=mock_counts,
                                total_counts=600,sums=1,frequency_of_type=None, 
                                average_price_of_type=1,test_row=mock_row)
    test_csv_ag.get_frequency_of_type()
    expected = {1: 0.16666666666666666, 2: 0.3333333333333333, 3: 0.5}
    assert test_csv_ag.frequency_of_type == expected
    
def test_get_average_price_of_type():
    mock_row = ['foo','1','1.00']
    mock_counts = {1:100,2:200,3:300}
    mock_sums = {1:1000,2:2000,3:0}
    test_csv_ag = CsvAggregator(csv_file_path='test', key_column=0,
                                value_column=1, csv_headers=1, 
                                csv_col_data_types=None, counts_per_type=mock_counts,
                                total_counts=600,frequency_of_type=None, 
                                average_price_of_type=1,test_row=mock_row, 
                                sums = mock_sums)
    test_csv_ag.get_average_price_of_type()
    expected = {1: 10.0, 2: 10.0, 3: 0}
    assert test_csv_ag.average_price_of_type == expected
    

