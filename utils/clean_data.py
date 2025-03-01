# -*- coding: utf-8 -*-
'''
@author: Jiayi Qian
CS 5001, Fall 2023
Final project

This file contains functions which clean the park data fetched from web url.
'''


def clean_park_neighbourhood_data(data):
    '''
    This function cleans park neighbourhood data fetched from web url.

    Args:
        data(list): the data fetched from web url

    Returns:
        parks_neighbourhood_list(list):
            a list of dictionaries containing cleaned data

    Raises:
        TypeError: if data is not list
    '''
    if not isinstance(data, list):
        raise TypeError("data must be a list")

    park_neighbourhood_list = []
    for park in data:
        park_details = {}
        park_details["name"] = park["name"]
        park_details["neighbourhood"] = park["neighbourhoodname"]
        park_details["washromms"] = park["washrooms"]
        park_details["special_features"] = park["specialfeatures"]
        park_details["facilities"] = park["facilities"]
        park_neighbourhood_list.append(park_details)
    return park_neighbourhood_list


def clean_park_washrooms_data(data):
    '''
    This function cleans park washrooms data fetched from web url.

    Args:
        data(list): the data fetched from web url

    Returns:
        park_washrooms_list(list):
            a list of dictionaries containing cleaned data

    Raises:
        TypeError: if data is not list
    '''
    if not isinstance(data, list):
        raise TypeError("data must be a list")

    park_washrooms_list = []
    for park in data:
        park_washroom_details = {}
        park_washroom_details["name"] = park["name"]
        park_washroom_details["location"] = park["location"]
        park_washrooms_list.append(park_washroom_details)
    return park_washrooms_list


def clean_park_special_features_data(data):
    '''
    This function cleans park special features data fetched from web url.

    Args:
        data(list): the data fetched from web url

    Returns:
        park_special_features_list(list):
            a list of dictionaries containing cleaned data

    Raises:
        TypeError: if data is not list
    '''
    if not isinstance(data, list):
        raise TypeError("data must be a list")

    park_special_features_list = []
    for park in data:
        park_special_feature_details = {}
        park_special_feature_details["name"] = park["name"]
        park_special_feature_details["special_feature"] = park["specialfeature"]
        park_special_features_list.append(park_special_feature_details)
    return park_special_features_list


def clean_park_facilities_data(data):
    '''
    This function cleans park facilities data fetched from web url.

    Args:
        data(list): the data fetched from web url

    Returns:
        park_facilities_list(list):
            a list of dictionaries containing cleaned data

    Raises:
        TypeError: if data is not list
    '''
    if not isinstance(data, list):
        raise TypeError("data must be a list")

    park_facilities_list = []
    for park in data:
        park_facilities_details = {}
        park_facilities_details["name"] = park["name"]
        park_facilities_details["facility_type"] = park["facilitytype"]
        park_facilities_details["facility_count"] = park["facilitycount"]
        park_facilities_list.append(park_facilities_details)
    return park_facilities_list


def clean_dog_off_leash_parks_data(data):
    '''
    This function cleans dog off leash parks data fetched from web url.

    Args:
        data(list): the data fetched from web url

    Returns:
        dog_off_leash_parks_list(list)
            a list of dictionaries containing cleaned data

    Raises:
        TypeError: if data is not list
    '''
    if not isinstance(data, list):
        raise TypeError("data must be a list")

    dog_off_leash_parks_list = []
    for park in data:
        dog_off_leash_parks_details = {}
        if park["name"] != None:
            dog_off_leash_parks_details["name"] = park["name"]
            if park["geo_local_area"] != None:
                dog_off_leash_parks_details["neighbourhood"] = park["geo_local_area"]
            else:
                if park["name"] == 'Spanish Banks Park':
                    dog_off_leash_parks_details["neighbourhood"] = "West Point Grey"
                elif park["name"] == 'Stanley Park':
                    dog_off_leash_parks_details["neighbourhood"] = "West End"
            dog_off_leash_parks_details["address"] = park["address"]
        else:
            if park["geo_local_area"] == "Renfrew-Collingwood":
                dog_off_leash_parks_details["name"] = "Renfrew Community Park"
                dog_off_leash_parks_details["neighbourhood"] = park["geo_local_area"]
                dog_off_leash_parks_details["address"] = f"geo_point_2d: {park['geo_point_2d']}"
            elif park["geo_local_area"] == "Hastings-Sunrise":
                dog_off_leash_parks_details["name"] = "Burrard View Park"
                dog_off_leash_parks_details["neighbourhood"] = park["geo_local_area"]
                dog_off_leash_parks_details["address"] = f"geo_point_2d: {park['geo_point_2d']}"
            elif park["geo_local_area"] == "Downtown":
                dog_off_leash_parks_details["name"] = "Andy Livingstone Park"
                dog_off_leash_parks_details["neighbourhood"] = park["geo_local_area"]
                dog_off_leash_parks_details["address"] = f"geo_point_2d: {park['geo_point_2d']}"
        dog_off_leash_parks_list.append(dog_off_leash_parks_details)
    return dog_off_leash_parks_list
