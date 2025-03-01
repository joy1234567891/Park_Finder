# -*- coding: utf-8 -*-
'''
@author: Jiayi Qian
CS 5001, Fall 2023
Final project

This file contains helper functions to implement
the app's search, explore, and charts features.
'''


from random import randint


# helper funtions for the search feature:
def get_neighbourhood_list(park_neighbourhood_objects):
    '''
    This function extracts all the neighbourhood names
    from a list of ParkNeighbourhood objects.

    Args:
        park_neighbourhood_objects(list): a list of ParkNeighbourhood objects

    Returns:
        neighbourhood_list(list): a list of all neighbourhood names

    Raises:
        TypeError: if park_neighbourhood_objects is not list
    '''
    if type(park_neighbourhood_objects) is not list:
        raise TypeError('Argument must be a list.')

    neighbourhood_list = []
    for park in park_neighbourhood_objects:
        if park.neighbourhood not in neighbourhood_list:
            neighbourhood_list.append(park.neighbourhood)
    return neighbourhood_list


def get_neighbourhood_parks(park_neighbourhood_objects, neighbourhood):
    '''
    This function generates a list of park names in a given neighbourhood.

    Args:
        park_neighbourhood_objects(list): a list of ParkNeighbourhood objects
        neighbourhood(str): a given neighbourhood

    Returns:
        neighbourhood_parks(list): a list of park names in a given neighbourhood

    Raises:
        TypeError: if park_neighbourhood_objects is not list,
                   or if neighbourhood is not str
    '''
    if type(park_neighbourhood_objects) is not list:
        raise TypeError('Argument must be a list.')
    if type(neighbourhood) is not str:
        raise TypeError('Neighbourhood must be a str.')

    neighbourhood_parks = []
    for park in park_neighbourhood_objects:
        if park.is_in_a_given_neighbourhood(neighbourhood):
            if park.name not in neighbourhood_parks:
                neighbourhood_parks.append(park.name)
    return neighbourhood_parks


def get_park_with_washrooms(park_washrooms_objects):
    '''
    This function generates a list of parks with washrooms.

    Args:
        park_washrooms_objects(list): a list of ParkWashrooms objects

    Returns:
        park_with_washrooms(list): a list of parks with washrooms

    Raises:
        TypeError: if park_washrooms_objects is not list
    '''
    if type(park_washrooms_objects) is not list:
        raise TypeError('Argument must be a list.')

    park_with_washrooms = []
    for park in park_washrooms_objects:
        if park.name not in park_with_washrooms:
            park_with_washrooms.append(park.name)
    return park_with_washrooms


def get_park_with_special_features(park_special_features_objects):
    '''
    This function generates a list of parks with special features.

    Args:
        park_special_features_objects(list): a list of ParkSpecialFeatures objects

    Returns:
        park_with_special_features(list): a list of parks with special features

    Raises:
        TypeError: if park_special_features_objects is not list
    '''
    if type(park_special_features_objects) is not list:
        raise TypeError('Argument must be a list.')

    park_with_special_features = []
    for park in park_special_features_objects:
        if park.name not in park_with_special_features:
            park_with_special_features.append(park.name)
    return park_with_special_features


def get_park_with_facilities(park_facilities_objects):
    '''
    This function generates a list of parks with facilities.

    Args:
        park_facilities_objects(list): a list of ParkFacilities objects

    Returns:
        park_with_facilities(list): a list of parks with facilities

    Raises:
        TypeError: if park_facilities_objects is not list
    '''
    if type(park_facilities_objects) is not list:
        raise TypeError('Argument must be a list.')

    park_with_facilities = []
    for park in park_facilities_objects:
        if park.name not in park_with_facilities:
            park_with_facilities.append(park.name)
    return park_with_facilities


def get_dog_off_leash_areas_parks(dog_off_leash_parks_objects, park_facilities_objects):
    '''
    This function generates a list of dog-off-leash areas and parks.

    Args:
        dog_off_leash_parks_objects(list): a list of DogOffLeashParks objects
        park_facilities_objects(list): a list of ParkFacilities objects

    Returns:
        dog_off_leash_areas_parks(list): a list of dog-off-leash areas and parks

    Raises:
        TypeError: if dog_off_leash_parks_objects or park_facilities_objects is not list
    '''
    if type(dog_off_leash_parks_objects) is not list:
        raise TypeError('Argument must be a list.')
    if type(park_facilities_objects) is not list:
        raise TypeError('Argument must be a list.')

    dog_off_leash_areas_parks = []
    for park in dog_off_leash_parks_objects:
        if park.name not in dog_off_leash_areas_parks:
            dog_off_leash_areas_parks.append(park.name)
    for park_facilities in park_facilities_objects:
        if park_facilities.facility_type == "Dogs Off-Leash Areas":
            if park_facilities.name not in dog_off_leash_areas_parks:
                dog_off_leash_areas_parks.append(park_facilities.name)
    return dog_off_leash_areas_parks


# helper funtion for the explore feature
def get_a_random_park(park_neighbourhood_objects):
    '''
    This function generates a random park name.

    Args:
        park_neighbourhood_objects(list): a list of ParkNeighbourhood objects

    Returns:
        random_park(str): a random park name

    Raises:
        TypeError: if park_neighbourhood_objects is not list
    '''
    if type(park_neighbourhood_objects) is not list:
        raise TypeError('Argument must be a list.')

    random_num = randint(0, len(park_neighbourhood_objects)-1)
    random_park = park_neighbourhood_objects[random_num].name
    return random_park


# helper funtion for the charts feature
def get_neighbourhood_park_number(park_neighbourhood_objects):
    '''
    This function gets the number of parks in each neighbourhood.

    Args:
        park_neighbourhood_objects(list): a list of ParkNeighbourhood objects

    Returns:
        neighbourhood_park_number(dict): keys are neighbourhood names,
            values are the number of parks in each neighbourhood.

    Raises:
        TypeError: if park_neighbourhood_objects is not list
    '''
    if type(park_neighbourhood_objects) is not list:
        raise TypeError('Argument must be a list.')

    neighbourhood_list = get_neighbourhood_list(park_neighbourhood_objects)
    neighbourhood_park_number = {}
    for neighbourhood in neighbourhood_list:
        if neighbourhood not in neighbourhood_park_number.keys():
            neighbourhood_park_number[neighbourhood] = []
            for park in park_neighbourhood_objects:
                if park.neighbourhood == neighbourhood:
                    neighbourhood_park_number[park.neighbourhood].append(park.name)
    for key in neighbourhood_park_number.keys():
        neighbourhood_park_number[key] = len(neighbourhood_park_number[key])
    return neighbourhood_park_number
