#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 15:54:37 2020

@author: JeffHalley
"""
import EtlCsvRowExtractorTestClass
import pytest


def test_get_cell_data_type():
    test_csv_ag = EtlCsvRowExtractorTestClass()
    types = ['foo', '1', '1.00']

    assert [test_csv_ag.get_cell_data_type(x)
            for x in types] == [str, int, float]


def test_get_col_data_type():
    mock_row = ['foo', '1', '1.00']
    test_csv_ag = EtlCsvRowExtractorTestClass(csv_headers=[],
                                              csv_col_data_types=[],
                                              first_row=mock_row)
    assert test_csv_ag.csv_col_data_types == [str, int, float]


def test_next_row():
    mock_headers = ['head_a', 'head_b', 'head_c']
    mock_types = [str, int, float]
    mock_row = ['foo', '1', '1.00']
    test_csv_ag = EtlCsvRowExtractorTestClass(csv_headers=mock_headers,
                                              csv_col_data_types=mock_types,
                                              first_row=mock_row)
    expected = {'head_a': {'value': 'foo', 'type': str},
                'head_b': {'value': '1', 'type': int},
                'head_c': {'value': '1.00', 'type': float}}

    assert test_csv_ag.next_row == expected


def test_send():
    mock_headers = ['head_a', 'head_b', 'head_c']
    mock_types = [str, int, float]
    mock_row = ['foo', '1', '1.00']
    test_csv_ag = EtlCsvRowExtractorTestClass(csv_headers=mock_headers,
                                              csv_col_data_types=mock_types,
                                              first_row=mock_row)
    expected = {'head_a': {'value': 'foo', 'type': str},
                'head_b': {'value': '1', 'type': int},
                'head_c': {'value': '1.00', 'type': float}}

    assert test_csv_ag.send() == expected


def test_throw():
    test_csv_ag = EtlCsvRowExtractorTestClass()
    with pytest.raises(StopIteration):
        test_csv_ag.send()
