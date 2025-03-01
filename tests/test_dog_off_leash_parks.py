#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Jiayi Qian
CS 5001, Fall 2023
Final Project

This file contains the unittest test suite for the DogOffLeashParks class.
'''


import unittest
# The following two lines are to solve the ModuelNotFound Error
import sys
sys.path.append("./")
from models.dog_off_leash_parks import DogOffLeashParks


class TestDogOffLeashParks(unittest.TestCase):
    """
    Unit tests for the DogOffLeashParks class.
    """

    def test_init_success(self):
        park = DogOffLeashParks("A", "B", "C")
        self.assertEqual(park.name, "A")
        self.assertEqual(park.neighbourhood, "B")
        self.assertEqual(park.address, "C")

    def test_init_name_type_error(self):
        with self.assertRaises(TypeError):
            DogOffLeashParks(1, "B", "C")

    def test_init_neighbourhood_type_error(self):
        with self.assertRaises(TypeError):
            DogOffLeashParks("A", 1, "C")

    def test_init_address_type_error(self):
        with self.assertRaises(TypeError):
            DogOffLeashParks("A", "B", 1)

    def test_has_details_true(self):
        park = DogOffLeashParks("A", "B", "C")
        self.assertTrue(park.has_details())

    def test_has_details_false(self):
        park = DogOffLeashParks("A", "B", "")
        self.assertFalse(park.has_details())


if __name__ == "__main__":
    unittest.main()
