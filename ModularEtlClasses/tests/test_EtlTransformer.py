#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:36:32 2020

@author: JeffHalley
"""
import EtlCsvRowExtractorTestClass
import EtlTransformerTestClass


def test_get_frequency_of_type():
    mock_extractor = EtlCsvRowExtractorTestClass()
    mock_counts = {1: 100, 2: 200, 3: 300}
    test_xformer = EtlTransformerTestClass(EtlExtractor=mock_extractor,
                                           counts_per_type=mock_counts,
                                           sums_of_values_per_type=mock_counts,
                                           total_counts=600)
    expected = {1: 0.16666666666666666, 2: 0.3333333333333333, 3: 0.5}
    assert test_xformer.frequency_of_type == expected


def test_get_average_price_of_type():
    mock_extractor = EtlCsvRowExtractorTestClass()
    mock_counts = {1: 100, 2: 200, 3: 300}
    mock_sums = {1: 1000, 2: 2000, 3: 0}
    test_xformer = EtlTransformerTestClass(EtlExtractor=mock_extractor,
                                           counts_per_type=mock_counts,
                                           total_counts=600,
                                           sums_of_values_per_type=mock_sums)
    expected = {1: 10.0, 2: 10.0, 3: 0}
    assert test_xformer.average_price_of_type == expected


def test_get_counts_and_sum():
    mock_headers = ['head_a', 'head_b', 'head_c']
    mock_types = [str, int, float]
    mock_row = ['foo', '1', '1.00']

    mock_extractor = EtlCsvRowExtractorTestClass(csv_headers=mock_headers,
                                                 csv_col_data_types=mock_types,
                                                 first_row=mock_row)

    test_xformer = EtlTransformerTestClass(mock_extractor, 'head_a',
                                           'head_c', total_counts=2)

    assert test_xformer.counts_per_type == {'foo': 1}
    assert test_xformer.sums_of_values_per_type == {'foo': 1.0}
