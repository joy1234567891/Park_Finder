# -*- coding: utf-8 -*-
'''
@author: Jiayi Qian
CS 5001, Fall 2023
Final project

This file contains functions related to converting data into class ojbects.
'''

# If ModuleNotFound Error happens, uncomment the following 2 lines
# import sys
# sys.path.append("./")
from models.park_neighbourhood import ParkNeighbourhood
from models.park_washrooms import ParkWashrooms
from models.park_facilities import ParkFacilities
from models.park_special_features import ParkSpecialFeatures
from models.dog_off_leash_parks import DogOffLeashParks


def convert_data_into_park_neighbourhood_objects(park_neighbourhood_list):
    '''
    This function converts data into ParkNeighbourhood objects.

    Args:
        park_neighbourhood_list(list): the cleaned park neighbourhoood data

    Returns:
        park_neighbourhood_objects(list): a list of ParkNeighbourhood objects

    Raises:
        TypeError: if park_neighbourhood_list is not list
        ValueError: if park_neighbourhood_list is an empty list
    '''
    if not isinstance(park_neighbourhood_list, list):
        raise TypeError('Argument must be a list.')
    if park_neighbourhood_list == []:
        raise ValueError('Argument cannot be an empty list.')

    park_neighbourhood_objects = []
    for park in park_neighbourhood_list:
        park_neighbourhood_object = ParkNeighbourhood(park["name"], park["neighbourhood"], park["washromms"], park["special_features"], park["facilities"])
        park_neighbourhood_objects.append(park_neighbourhood_object)
    return park_neighbourhood_objects


def convert_data_into_park_washrooms_objects(park_washrooms_list):
    '''
    This function converts data into ParkWashrooms objects.

    Args:
        park_washrooms_list(list): the cleaned park washrooms data

    Returns:
        park_washrooms_objects(list): a list of ParkWashrooms objects

    Raises:
        TypeError: if park_washrooms_list is not list
        ValueError: if park_washrooms_list is an empty list
    '''
    if not isinstance(park_washrooms_list, list):
        raise TypeError('Argument must be a list.')
    if park_washrooms_list == []:
        raise ValueError('Argument cannot be an empty list.')

    park_washrooms_objects = []
    for park in park_washrooms_list:
        if park["location"] is not None:
            park_washrooms_object = ParkWashrooms(park["name"], park["location"])
        else:
            park_washrooms_object = ParkWashrooms(park["name"], "")
        park_washrooms_objects.append(park_washrooms_object)
    return park_washrooms_objects


def convert_data_into_park_special_features_objects(park_special_features_list):
    '''
    This function converts data into ParkSpecialFeatures objects.

    Args:
        park_special_features_list(list): the cleaned park special features data

    Returns:
        park_special_features_objects(list): a list of ParkSpecialFeatures objects

    Raises:
        TypeError: if park_special_features_list is not list
        ValueError: if park_special_features_list is an empty list
    '''
    if not isinstance(park_special_features_list, list):
        raise TypeError('Argument must be a list.')
    if park_special_features_list == []:
        raise ValueError('Argument cannot be an empty list.')

    park_special_features_objects = []
    for park in park_special_features_list:
        park_special_features_object = ParkSpecialFeatures(park["name"], park["special_feature"])
        park_special_features_objects.append(park_special_features_object)
    return park_special_features_objects


def convert_data_into_park_facilities_objects(park_facilities_list):
    '''
    This function converts data into ParkFacilities objects.

    Args:
        park_facilities_list(list): the cleaned park facilities data

    Returns:
        park_facilities_objects(list): a list of ParkFacilities objects

    Raises:
        TypeError: if park_facilities_list is not list
        ValueError: if park_facilities_list is an empty list
    '''
    if not isinstance(park_facilities_list, list):
        raise TypeError('Argument must be a list.')
    if park_facilities_list == []:
        raise ValueError('Argument cannot be an empty list.')

    park_facilities_objects = []
    for park in park_facilities_list:
        park_facilities_object = ParkFacilities(park["name"], park["facility_type"], park["facility_count"])
        park_facilities_objects.append(park_facilities_object)
    return park_facilities_objects


def convert_data_into_dog_off_leash_parks_objects(dog_off_leash_parks_list):
    '''
    This function converts data into DogOffLeashParks objects.

    Args:
        dog_off_leash_parks_list(list): the cleaned dog off leash parks data

    Returns:
        dog_off_leash_parks_objects(list): a list of DogOffLeashParks objects

    Raises:
        TypeError: if dog_off_leash_parks_list is not list
        ValueError: if dog_off_leash_parks_list is an empty list
    '''
    if not isinstance(dog_off_leash_parks_list, list):
        raise TypeError('Argument must be a list.')
    if dog_off_leash_parks_list == []:
        raise ValueError('Argument cannot be an empty list.')

    dog_off_leash_parks_objects = []
    for park in dog_off_leash_parks_list:
        dog_off_leash_parks_object = DogOffLeashParks(park["name"], park["neighbourhood"], park["address"])
        dog_off_leash_parks_objects.append(dog_off_leash_parks_object)
    return dog_off_leash_parks_objects
