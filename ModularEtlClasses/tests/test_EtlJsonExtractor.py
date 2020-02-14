#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 15:54:37 2020

@author: JeffHalley
"""
import EtlJsonExtractorTestClass
import pytest


def test_next_row():
    mock_json = {'author': 'Dethcola',
                 'author_flair_css_class': '',
                 'author_flair_text': 'Clairemont',
                 'body': 'A quarry',
                 'can_gild': True,
                 'controversiality': 0,
                 'created_utc': 1506816000,
                 'distinguished': None,
                 'edited': False,
                 'gilded': 0,
                 'id': 'dnqik14',
                 'is_submitter': False,
                 'link_id': 't3_73ieyz',
                 'parent_id': 't3_73ieyz',
                 'permalink': '/r/granite_counter_tops/dnqik14/',
                 'retrieved_on': 1509189606,
                 'score': 3,
                 'stickied': False,
                 'subreddit': 'sandiego',
                 'subreddit_id': 't5_2qq2q'}
    test_j_ex = EtlJsonExtractorTestClass(first_json=mock_json)
    expected = {'author': {'value': 'Dethcola', 'type': str},
                'author_flair_css_class': {'value': '', 'type': str},
                'author_flair_text': {'value': 'Clairemont', 'type': str},
                'body': {'value': 'A quarry', 'type': str},
                'can_gild': {'value': True, 'type': bool},
                'controversiality': {'value': 0, 'type': int},
                'created_utc': {'value': 1506816000, 'type': int},
                'distinguished': {'value': None, 'type': None},
                'edited': {'value': False, 'type': bool},
                'gilded': {'value': 0, 'type': int},
                'id': {'value': 'dnqik14', 'type': str},
                'is_submitter': {'value': False, 'type': bool},
                'link_id': {'value': 't3_73ieyz', 'type': str},
                'parent_id': {'value': 't3_73ieyz', 'type': str},
                'permalink': {'value': '/r/granite_counter_tops/dnqik14/',
                              'type': str},
                'retrieved_on': {'value': 1509189606, 'type': int},
                'score': {'value': 3, 'type': int},
                'stickied': {'value': False, 'type': bool},
                'subreddit': {'value': 'sandiego', 'type': str},
                'subreddit_id': {'value': 't5_2qq2q', 'type': str}}

    assert test_j_ex.next_row == expected


def test_send():
    mock_fields = ['author', 'author_flair_css_class', 'author_flair_text',
                    'body', 'can_gild', 'controversiality', 'created_utc',
                    'distinguished', 'edited', 'gilded', 'id', 'is_submitter',
                    'link_id', 'parent_id', 'permalink', 'retrieved_on',
                    'score', 'stickied', 'subreddit', 'subreddit_id']
    mock_types = [str, str, str, str, bool, int, int, None, bool, int, str,
                  bool, str, str, str, int, int, bool, str, str]
    mock_json = {'author': 'Dethcola',
                 'author_flair_css_class': '',
                 'author_flair_text': 'Clairemont',
                 'body': 'A quarry',
                 'can_gild': True,
                 'controversiality': 0,
                 'created_utc': 1506816000,
                 'distinguished': None,
                 'edited': False,
                 'gilded': 0,
                 'id': 'dnqik14',
                 'is_submitter': False,
                 'link_id': 't3_73ieyz',
                 'parent_id': 't3_73ieyz',
                 'permalink': '/r/granite_counter_tops/dnqik14/',
                 'retrieved_on': 1509189606,
                 'score': 3,
                 'stickied': False,
                 'subreddit': 'sandiego',
                 'subreddit_id': 't5_2qq2q'}
    test_j_ex = EtlJsonExtractorTestClass(json_fields=mock_fields,
                                          field_data_types=mock_types,
                                          first_json=mock_json)
    expected = {'author': {'value': 'Dethcola', 'type': str},
                'author_flair_css_class': {'value': '', 'type': str},
                'author_flair_text': {'value': 'Clairemont', 'type': str},
                'body': {'value': 'A quarry', 'type': str},
                'can_gild': {'value': True, 'type': bool},
                'controversiality': {'value': 0, 'type': int},
                'created_utc': {'value': 1506816000, 'type': int},
                'distinguished': {'value': None, 'type': None},
                'edited': {'value': False, 'type': bool},
                'gilded': {'value': 0, 'type': int},
                'id': {'value': 'dnqik14', 'type': str},
                'is_submitter': {'value': False, 'type': bool},
                'link_id': {'value': 't3_73ieyz', 'type': str},
                'parent_id': {'value': 't3_73ieyz', 'type': str},
                'permalink': {'value': '/r/granite_counter_tops/dnqik14/',
                'type': str},
                'retrieved_on': {'value': 1509189606, 'type': int},
                'score': {'value': 3, 'type': int},
                'stickied': {'value': False, 'type': bool},
                'subreddit': {'value': 'sandiego', 'type': str},
                'subreddit_id': {'value': 't5_2qq2q', 'type': str}}

    assert test_j_ex.send() == expected


def test_throw():
    test_j_ex = EtlJsonExtractorTestClass()
    with pytest.raises(StopIteration):
        test_j_ex.send()
