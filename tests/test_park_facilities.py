#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Jiayi Qian
CS 5001, Fall 2023
Final Project

This file contains the unittest test suite for the ParkFacilities class.
'''


import unittest
# The following two lines are to solve the ModuelNotFound Error
import sys
sys.path.append("./")
from models.park_facilities import ParkFacilities


class TestParkFacilities(unittest.TestCase):
    """
    Unit tests for the ParkFacilities class.
    """

    def test_init_success(self):
        park = ParkFacilities("A", "B", 3)
        self.assertEqual(park.name, "A")
        self.assertEqual(park.facility_type, "B")
        self.assertEqual(park.facility_count, 3)

    def test_init_name_type_error(self):
        with self.assertRaises(TypeError):
            ParkFacilities(1, "B", 3)

    def test_init_facility_type_type_error(self):
        with self.assertRaises(TypeError):
            ParkFacilities("A", 1, 3)

    def test_init_facility_count_type_error(self):
        with self.assertRaises(TypeError):
            ParkFacilities("A", "B", "3")

    def test_has_details_true(self):
        park = ParkFacilities("A", "B", 3)
        self.assertTrue(park.has_details())

    def test_has_details_false(self):
        park = ParkFacilities("A", "", 3)
        self.assertFalse(park.has_details())


if __name__ == "__main__":
    unittest.main()
