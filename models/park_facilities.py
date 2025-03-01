#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Jiayi Qian
CS 5001, Fall 2023
Final project

Class: ParkFacilities
Description: This module contains the ParkFacilities class, which represents
a park with facilities with attributes and actions relevant to the web
application's search and explore features.
'''


class ParkFacilities:
    """
    Represents a park with facilities with attributes and actions
    relevant to the web application's search and explore features.

    Attributes:
        name(str): name of the park with facilities
        facility_type(str): the park's facility type
        facility_count(int): the park's facility count

    Methods:
        has_details(self):
            This method checks if a park with facilities has
            facilities details such as the type of the facilities.
    """

    def __init__(self, name, facility_type, facility_count):
        """
        Initializes a new ParkFacilities object with given attributes.

        Args:
            name(str): name of the park with facilities
            facility_type(str): the park's facility type
            facility_count(int): the park's facility count

        Raises:
            TypeError: if name or facility_type is not str,
                       or if facility_count is not int

        """
        if not isinstance(name, str):
            raise TypeError('name must be a string')
        if not isinstance(facility_type, str):
            raise TypeError('facility type must be a string')
        if not isinstance(facility_count, int):
            raise TypeError('facility count must be an integer')

        self.name = name
        self.facility_type = facility_type
        self.facility_count = facility_count

    def has_details(self):
        '''
        This method checks if a park with facilities has
        facilities details such as the type of the facilities.

        No Args

        Returns: Bool
        '''
        if self.facility_type != '':
            return True
        else:
            return False
