#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Jiayi Qian
CS 5001, Fall 2023
Final Project

This file contains the unittest test suite for the ParkNeighbourhood class.
'''


import unittest
# The following two lines are to solve the ModuelNotFound Error
import sys
sys.path.append("./")
from models.park_neighbourhood import ParkNeighbourhood


class TestParkNeighbourhood(unittest.TestCase):
    """
    Unit tests for the ParkNeighbourhood class.
    """

    def test_init_success(self):
        park = ParkNeighbourhood("A", "B", "Y", "Y", "Y")
        self.assertEqual(park.name, "A")
        self.assertEqual(park.neighbourhood, "B")
        self.assertEqual(park.washrooms, "Y")
        self.assertEqual(park.special_features, "Y")
        self.assertEqual(park.facilities, "Y")

    def test_init_name_type_error(self):
        with self.assertRaises(TypeError):
            ParkNeighbourhood(1, "B", "Y", "Y", "Y")

    def test_init_neighbourhood_type_error(self):
        with self.assertRaises(TypeError):
            ParkNeighbourhood("A", 1, "Y", "Y", "Y")

    def test_init_washrooms_type_error(self):
        with self.assertRaises(TypeError):
            ParkNeighbourhood("A", "B", 1, "Y", "Y")

    def test_init_special_features_type_error(self):
        with self.assertRaises(TypeError):
            ParkNeighbourhood("A", "B", "Y", 1, "Y")

    def test_init_facilities_type_error(self):
        with self.assertRaises(TypeError):
            ParkNeighbourhood("A", "B", "Y", "Y", 1)

    def test_is_in_a_given_neighbourhood_true(self):
        park = ParkNeighbourhood("A", "B", "Y", "Y", "Y")
        self.assertTrue(park.is_in_a_given_neighbourhood("B"))

    def test_is_in_a_given_neighbourhood_false(self):
        park = ParkNeighbourhood("A", "B", "Y", "Y", "Y")
        self.assertFalse(park.is_in_a_given_neighbourhood("A"))

    def test_is_in_a_given_neighbourhood_type_error(self):
        park = ParkNeighbourhood("A", "B", "Y", "Y", "Y")
        with self.assertRaises(TypeError):
            park.is_in_a_given_neighbourhood(1)


if __name__ == "__main__":
    unittest.main()
