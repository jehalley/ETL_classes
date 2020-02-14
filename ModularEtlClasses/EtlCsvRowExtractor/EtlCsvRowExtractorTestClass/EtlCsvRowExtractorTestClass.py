#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 09:02:55 2020

@author: JeffHalley
"""
import EtlCsvRowExtractor


class EtlCsvRowExtractorTestClass(EtlCsvRowExtractor):
    def __init__(self, csv_headers=[], csv_col_data_types=[], first_row=[]):

        self.csv_headers = csv_headers
        self.csv_col_data_types = csv_col_data_types
        self.first_row = first_row
        if not self.csv_col_data_types:
            self.get_col_data_types()
        # convert csv row into a json-like dict
        self.next_row = {k: {'value': v, 'type': vtype} for
                         k, v, vtype in zip(self.csv_headers,
                                            self.first_row,
                                            self.csv_col_data_types)}

        # reader needs to be mocked for testing next row and send
        self.next_file = None
        self.reader = iter([self.first_row])
