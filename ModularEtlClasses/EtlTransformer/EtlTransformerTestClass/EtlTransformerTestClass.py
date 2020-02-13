#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:14:56 2020

@author: JeffHalley
"""
import EtlTransformer


class EtlTransformerTestClass(EtlTransformer):
    def __init__(self, EtlExtractor, key_col_name=None, value_col_name=None,
                 counts_per_type={}, total_counts=0,
                 sums_of_values_per_type={}, frequency_of_type={},
                 average_price_of_type={}, test_row=None):

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

        if not self.counts_per_type or not self.sums_of_values_per_type:
            self.get_counts_and_sums()

        if not self.frequency_of_type:
            self.get_frequency_of_type()

        if not self.average_price_of_type:
            self.get_average_price_of_type()
