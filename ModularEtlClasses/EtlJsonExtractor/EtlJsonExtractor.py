#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 09:02:55 2020

@author: JeffHalley
"""

from collections.abc import Generator
import json


class EtlJsonExtractor(Generator):
    def __init__(self, json_file_path):

        self.json_file_path = json_file_path
        self.json_file = open(self.json_file_path, "r")
        self.first_json = json.loads(self.json_file.readline())
        self.json_fields = self.first_json.keys()
        self.json_field_data_types = [type(x) for x in
                                      self.first_json.values()]

        # self.next_row =[x(y) for x,y in zip(self.csv_col_data_types,
        # self.first_row)]

        self.next_row = {k: {'value': v, 'type': vtype} for
                         k, v, vtype in zip(self.json_fields,
                                            self.first_json.values(),
                                            self.json_field_data_types)}

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
                new_json = json.loads(self.json_file.readline())
                self.next_row = {k: {'value': v, 'type': vtype} for
                                 k, v, vtype in zip(self.json_fields,
                                 new_json.values(),
                                 self.json_field_data_types)}
            except ValueError:
                self.next_row = None
                self.json_file.close()
            except AttributeError:  # here for the test case without file
                self.next_row = None
            return row_to_send
        else:
            self.throw()

    def throw(self, type=None, value=None, traceback=None):
        raise StopIteration
