#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Jiayi Qian
CS 5001, Fall 2023
Final project

Class: ParkNeighbourhood
Description: This module contains the ParkNeighbourhood class, which
represents a park with attributes and actions relevant to the web application's
search, explore, and charts features.
'''


class ParkNeighbourhood:
    """
    Represents a park with attributes and actions relevant to the web
    application's search, explore, and charts features.

    Attributes:
        name(str): name of the park
        neighbourhood(str): neighbourhood the park belongs to
        washrooms(str): whether the park has washrooms
        special_features(str): whether the park has special features
        facilities(str): whether the park has facilities

    Methods:
        is_in_a_given_neighbourhood(self, neighbourhood):
            This method checks if a park is in a given neighbourhood.
    """

    def __init__(self, name, neighbourhood, washrooms,
                 special_features, facilities):
        """
        Initializes a new ParkNeighbourhood object with given attributes.

        Args:
            name(str): name of the park
            neighbourhood(str): neighbourhood the park belongs to
            washrooms(str): whether the park has washrooms
            special_features(str): whether the park has special_features
            facilities(str): whether the park has facilities

        Raises:
            TypeError: if name, neighbourhood, washrooms,
                       special_features, or facilities is not str
        """
        if not isinstance(name, str):
            raise TypeError('name must be a string')
        if not isinstance(neighbourhood, str):
            raise TypeError('neighbourhood must be a string')
        if not isinstance(washrooms, str):
            raise TypeError('washrooms must be a string')
        if not isinstance(special_features, str):
            raise TypeError('special features must be a string')
        if not isinstance(facilities, str):
            raise TypeError('facilities must be a string')

        self.name = name
        self.neighbourhood = neighbourhood
        self.washrooms = washrooms
        self.special_features = special_features
        self.facilities = facilities

    def is_in_a_given_neighbourhood(self, neighbourhood):
        """
        Checks if a park is in a given neighbourhood.

        Args:
            neighbourhood(str): a given neighbourhood

        Returns: Bool

        Raises:
            TypeError: if neighbourhood is not str
        """
        if not isinstance(neighbourhood, str):
            raise TypeError('neighbourhood must be a string')

        if self.neighbourhood == neighbourhood:
            return True
        else:
            return False
