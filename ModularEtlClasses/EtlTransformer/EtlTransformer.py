#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:14:56 2020

@author: JeffHalley
"""


class EtlTransformer:
    def __init__(self, EtlExtractor, key_col_name, value_col_name):
        self.EtlExtractor = EtlExtractor
        self.key_col_name = key_col_name
        self.value_col_name = value_col_name
        self.counts_per_type = {}
        self.total_counts = 0
        self.sums_of_values_per_type = {}
        self.average_price_of_type = {}
        self.frequency_of_type = {}
        self.invalid_rows = []

        self.get_counts_and_sums()
        self.get_frequency_of_type()
        self.get_average_price_of_type()

    def get_counts_and_sums(self):
        while self.EtlExtractor.has_next():
            cur_row = self.EtlExtractor.send()
            cur_row_key = cur_row[self.key_col_name]['type'](
                    cur_row[self.key_col_name]['value'])
            cur_row_value = cur_row[self.value_col_name]['type'](
                    cur_row[self.value_col_name]['value'])

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

    def get_frequency_of_type(self):
        self.frequency_of_type = {k: (v/self.total_counts)
                                  for k, v in self.counts_per_type.items()}

    def get_average_price_of_type(self):
        self.average_price_of_type = {k: (self.sums_of_values_per_type[k] /
                                      self.counts_per_type[k])for k in
                                      self.sums_of_values_per_type.keys()}
