#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Jiayi Qian
CS 5001, Fall 2023
Final Project

This file contains the unittest test suite for the ParkSpecialFeatures class.
'''


import unittest
# The following two lines are to solve the ModuelNotFound Error
import sys
sys.path.append("./")
from models.park_special_features import ParkSpecialFeatures


class TestParkSpecialFeatures(unittest.TestCase):
    """
    Unit tests for the ParkSpecialFeatures class.
    """

    def test_init_success(self):
        park = ParkSpecialFeatures("A", "B")
        self.assertEqual(park.name, "A")
        self.assertEqual(park.special_feature, "B")

    def test_init_name_type_error(self):
        with self.assertRaises(TypeError):
            ParkSpecialFeatures(1, "B")

    def test_init_special_feature_type_error(self):
        with self.assertRaises(TypeError):
            ParkSpecialFeatures("A", 1)

    def test_has_details_true(self):
        park = ParkSpecialFeatures("A", "B")
        self.assertTrue(park.has_details())

    def test_has_details_false(self):
        park = ParkSpecialFeatures("A", "")
        self.assertFalse(park.has_details())


if __name__ == "__main__":
    unittest.main()
