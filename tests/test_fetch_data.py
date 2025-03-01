#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Jiayi Qian
CS 5001, Fall 2023
Final Project

This file contains the unittest test suite for the data processing functions.
'''


import unittest
import requests
from requests.exceptions import (ConnectionError, HTTPError,
                                 Timeout, TooManyRedirects)
import requests_mock
# The following two lines are to solve the ModuelNotFound Error
import sys
sys.path.append("./")


class TestFetchDataFromUrl(unittest.TestCase):
    """
    Unit tests for the fetch_data_from_url function.
    """

    def test_fetch_data_from_url_success(self):
        test_url = "https://opendata.vancouver.ca/explore/dataset/parks-washrooms/export/"
        expected_data = {"parkid": 10, "name": "Andy Livingstone Park", "location": "South side, fieldhouse", "notes": None, "summerhours": "10:00 am - 11:00 pm", "winterhours": "10:00 am - 11:00 pm"}
        with requests_mock.Mocker() as m:
            m.get(test_url, json=expected_data)
            response = requests.get(test_url)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()["parkid"], 10)

    def test_fetch_data_from_url_with_http_error(self):
        test_url = "https://opendata.vancouver.ca/explore/dataset/parks-washrooms/export/"
        with requests_mock.Mocker() as m:
            m.get(test_url, status_code=404)
            self.assertRaises(HTTPError)

    def test_fetch_data_from_url_with_connection_error(self):
        test_url = "https://opendata.vancouver.ca/explore/dataset/parks-washrooms/export/"
        with requests_mock.Mocker() as m:
            m.get(test_url, exc=ConnectionError)
            self.assertRaises(ConnectionError)

    def test_fetch_data_from_url_with_timeout_error(self):
        test_url = "https://opendata.vancouver.ca/explore/dataset/parks-washrooms/export/"
        with requests_mock.Mocker() as m:
            m.get(test_url, exc=Timeout)
            self.assertRaises(Timeout)

    def test_fetch_data_from_url_with_too_many_redirects_error(self):
        test_url = "https://opendata.vancouver.ca/explore/dataset/parks-washrooms/export/"
        with requests_mock.Mocker() as m:
            m.get(test_url, exc=TooManyRedirects)
            self.assertRaises(TooManyRedirects)


if __name__ == "__main__":
    unittest.main()
