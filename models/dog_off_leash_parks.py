#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Jiayi Qian
CS 5001, Fall 2023
Final project

Class: DogOffLeashParks
Description: This module contains the DogOffLeashParks class, which represents
a dog-off-leash park with attributes and actions relevant to the web
application's search and explore features.
'''


class DogOffLeashParks:
    """
    Represents a dog-off-leash park with attributes and actions relevant to
    the web application's search and explore features.

    Attributes:
        name(str): name of the dog-off-leash park
        neighbourhood(str): neighbourhood the park belongs to
        address(str): address of the park

    Methods:
        has_details(self):
            This method checks if a dog-off-leash park has address details.
    """

    def __init__(self, name, neighbourhood, address):
        """
        Initializes a new DogOffLeashParks object with given attributes.

        Args:
            name(str): name of the dog-off-leash park
            neighbourhood(str): neighbourhood the park belongs to
            address(str): address of the park

        Raises:
            TypeError: if name, neighbourhood or address is not str

        """
        if not isinstance(name, str):
            raise TypeError('name must be a string')
        if not isinstance(neighbourhood, str):
            raise TypeError('neighbourhood must be a string')
        if not isinstance(address, str):
            raise TypeError('address must be a string')

        self.name = name
        self.neighbourhood = neighbourhood
        self.address = address

    def has_details(self):
        '''
        This method checks if a dog-off-leash park has address details.

        No Args

        Returns: Bool
        '''
        if self.address != '':
            return True
        else:
            return False
