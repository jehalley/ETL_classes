#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 09:02:55 2020

@author: JeffHalley
"""
import EtlCsvRowExtractor


class EtlCsvRowExtractorTestClass(EtlCsvRowExtractor):
    def __init__(self, json_fields=[], field_data_types=[], first_json={}):
        self.first_json = first_json
        self.json_fields = json_fields
        if not self.json_fields:
            self.json_fields = [x for x in self.first_json.keys()]
        self.json_field_data_types = field_data_types
        if not self.json_field_data_types:
            self.json_field_data_types = [type(x) for x in
                                          self.first_json.values()]
        self.json_file = None
        self.next_row = {k: {'value': v, 'type': vtype} for
                         k, v, vtype in zip(self.json_fields,
                                            self.first_json.values(),
                                            self.json_field_data_types)}
