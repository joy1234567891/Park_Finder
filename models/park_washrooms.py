#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Jiayi Qian
CS 5001, Fall 2023
Final project

Class: ParkWashrooms
Description: This module contains the ParkWashrooms class, which represents
a park with washrooms with attributes and actions relevant to the web
application's search and explore features.
'''


class ParkWashrooms:
    """
    Represents a park with washrooms with attributes and actions
    relevant to the web application's search and explore features.

    Attributes:
        name(str): name of the park with washrooms
        location(str): location of the park's washrooms

    Methods:
        has_details(self):
            This method checks if a park with washrooms has
            washroom details such as the location of the washrooms.
    """

    def __init__(self, name, location):
        """
        Initializes a new ParkWashrooms object with given attributes.

        Args:
            name(str): name of the park with washrooms
            location(str): location of the park's washrooms

        Raises:
            TypeError: if name or locartion is not str

        """
        if not isinstance(name, str):
            raise TypeError('name must be a string')
        if not isinstance(location, str):
            raise TypeError('location must be a string')

        self.name = name
        self.location = location

    def has_details(self):
        '''
        This method checks if a park with washrooms has
        washroom details such as the location of the washrooms.

        No Args

        Returns: Bool
        '''
        if self.location != '':
            return True
        else:
            return False
