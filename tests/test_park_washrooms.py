#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Jiayi Qian
CS 5001, Fall 2023
Final Project

This file contains the unittest test suite for the ParkWashrooms class.
'''


import unittest
# The following two lines are to solve the ModuelNotFound Error
import sys
sys.path.append("./")
from models.park_washrooms import ParkWashrooms


class TestParkWashrooms(unittest.TestCase):
    """
    Unit tests for the ParkWashrooms class.
    """

    def test_init_success(self):
        park = ParkWashrooms("A", "B")
        self.assertEqual(park.name, "A")
        self.assertEqual(park.location, "B")

    def test_init_name_type_error(self):
        with self.assertRaises(TypeError):
            ParkWashrooms(1, "B")

    def test_init_location_type_error(self):
        with self.assertRaises(TypeError):
            ParkWashrooms("A", 1)

    def test_has_details_true(self):
        park = ParkWashrooms("A", "B")
        self.assertTrue(park.has_details())

    def test_has_details_false(self):
        park = ParkWashrooms("A", "")
        self.assertFalse(park.has_details())


if __name__ == "__main__":
    unittest.main()
