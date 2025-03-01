#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Jiayi Qian
CS 5001, Fall 2023
Final project

Class: ParkSpecialFeatures
Description: This module contains the ParkSpecialFeatures class,
which represents a park with special features with attributes and
actions relevant to the web application's search and explore features.
'''


class ParkSpecialFeatures:
    """
    Represents a park with special features with attributes and
    actions relevant to the web application's search and explore features.

    Attributes:
        name(str): name of the park with special features
        special_feature(str): name of the park's special feature

    Methods:
        has_details(self):
            This method checks if a park with special features has
            feature details such as the name of the feature.
    """

    def __init__(self, name, special_feature):
        """
        Initializes a new ParkSpecialFeatures object with given attributes.

        Args:
            name(str): name of the park with special features
            special_feature(str): name of the park's special feature

        Raises:
            TypeError: if name or special_feature is not str

        """
        if not isinstance(name, str):
            raise TypeError('name must be a string')
        if not isinstance(special_feature, str):
            raise TypeError('special feature must be a string')

        self.name = name
        self.special_feature = special_feature

    def has_details(self):
        '''
        This method checks if a park with special features has feature details
        such as the name of the feature.

        No Args

        Returns: Bool
        '''
        if self.special_feature != '':
            return True
        else:
            return False
