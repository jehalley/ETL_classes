#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 09:02:55 2020

@author: JeffHalley
"""

from collections.abc import Generator
import csv


class EtlCsvRowExtractor(Generator):
    def __init__(self, csv_file_path):

        self.csv_file_path = csv_file_path
        self.csv_headers = []
        self.csv_col_data_types = []
        self.csv_file = open(self.csv_file_path, "r")
        self.reader = csv.reader(self.csv_file)
        self.csv_headers = next(self.reader)
        self.first_row = next(self.reader)
        self.get_col_data_types()

        # self.next_row =[x(y) for x,y in zip(self.csv_col_data_types,
        # self.first_row)]

        # convert csv row into a json-like dict
        self.next_row = {k: {'value': v, 'type': vtype} for
                         k, v, vtype in zip(self.csv_headers,
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
        self.csv_col_data_types = [self.get_cell_data_type(x)
                                   for x in self.first_row]

    def has_next(self):
        if self.next_row:
            return True
        else:
            return False

    def send(self):
        if self.next_row:
            row_to_send = self.next_row
            try:
                # self.next_row = [x(y) for x,y in zip(self.csv_col_data_types,
                # next(self.reader))]
                self.next_row = {k: {'value': v, 'type': vtype} for
                                 k, v, vtype in zip(self.csv_headers,
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
