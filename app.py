# -*- coding: utf-8 -*-
'''
@author: Jiayi Qian
CS 5001, Fall 2023
Final project

This file serves as the controller for the web app.
'''


import streamlit as st
from requests.exceptions import (ConnectionError, HTTPError,
                                 Timeout, TooManyRedirects)
from app_views.displays import display_home_page, display_park_details_table, display_park_neighbourhood_bar_chart, display_search_results
from utils import convert_data as cvd, fetch_data as fd, clean_data as cld
from app_views.input_widgets import button, multiselect, selctbox
from utils.feature_helpers import (get_neighbourhood_list, get_neighbourhood_parks,
                                   get_a_random_park,
                                   get_dog_off_leash_areas_parks, get_park_with_facilities,
                                   get_park_with_special_features, get_park_with_washrooms,
                                   get_neighbourhood_park_number)
PARKS_URL = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/parks/exports/json?lang=en&timezone=America%2FLos_Angeles"
PARK_WASHROOMS_URL = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/parks-washrooms/exports/json?lang=en&timezone=America%2FLos_Angeles"
PARKS_SPECIAL_FEATURES_URL = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/parks-special-features/exports/json?lang=en&timezone=America%2FLos_Angeles"
PARKS_FACILITIES_URL = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/parks-facilities/exports/json?lang=en&timezone=America%2FLos_Angeles"
DOG_OFF_LEASH_PARKS_URL = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/dog-off-leash-parks/exports/json?lang=en&timezone=America%2FLos_Angeles"
FILTER_OPTIONS = ['Neighbourhood', 'Feature']
FEATURE_OPTIONS = ["Washroom", "Facilities", "Special Features", "Dog-off-leash areas/parks"]


def search_render():
    '''
    This function renders the search feature.

    No Args

    No Returns
    '''
    option = multiselect("Filter by", FILTER_OPTIONS, key="filter")
    if option == ['Neighbourhood']:
        data = fd.fetch_data_from_url(PARKS_URL)
        park_neighbourhood_list = cld.clean_park_neighbourhood_data(data)
        park_neighbourhood_objects = cvd.convert_data_into_park_neighbourhood_objects(park_neighbourhood_list)
        neighbourhood_list = get_neighbourhood_list(park_neighbourhood_objects)
        neighbourhood = selctbox('Select a neighbourhood', neighbourhood_list, key="nei")
        if button("Search", 1):
            results = get_neighbourhood_parks(park_neighbourhood_objects, neighbourhood)
            st.subheader("Parks in this neighbourhood:")
            display_search_results(results)
    elif option == ['Feature']:
        feature = selctbox('Select a feature', FEATURE_OPTIONS, key="fea")
        if button("Search", 2):
            if feature == "Washroom":
                data = fd.fetch_data_from_url(PARK_WASHROOMS_URL)
                park_washrooms_list = cld.clean_park_washrooms_data(data)
                park_washrooms_objects = cvd.convert_data_into_park_washrooms_objects(park_washrooms_list)
                results = get_park_with_washrooms(park_washrooms_objects)
                st.subheader("Parks with washrooms:")
                display_search_results(results)
            elif feature == "Facilities":
                data = fd.fetch_data_from_url(PARKS_FACILITIES_URL)
                park_facilities_list = cld.clean_park_facilities_data(data)
                park_facilities_objects = cvd.convert_data_into_park_facilities_objects(park_facilities_list)
                results = get_park_with_facilities(park_facilities_objects)
                st.subheader("Parks with facilities:")
                display_search_results(results)
            elif feature == "Special Features":
                data = fd.fetch_data_from_url(PARKS_SPECIAL_FEATURES_URL)
                park_special_features_list = cld.clean_park_special_features_data(data)
                park_special_features_objects = cvd.convert_data_into_park_special_features_objects(park_special_features_list)
                results = get_park_with_special_features(park_special_features_objects)
                st.subheader("Parks with special features:")
                display_search_results(results)
            elif feature == "Dog-off-leash areas/parks":
                data = fd.fetch_data_from_url(DOG_OFF_LEASH_PARKS_URL)
                dog_off_leash_parks_list = cld.clean_dog_off_leash_parks_data(data)
                dog_off_leash_parks_objects = cvd.convert_data_into_dog_off_leash_parks_objects(dog_off_leash_parks_list)
                facility_data = fd.fetch_data_from_url(PARKS_FACILITIES_URL)
                park_facilities_list = cld.clean_park_facilities_data(facility_data)
                park_facilities_objects = cvd.convert_data_into_park_facilities_objects(park_facilities_list)
                results = get_dog_off_leash_areas_parks(dog_off_leash_parks_objects, park_facilities_objects)
                st.subheader("Dog off leash areas/parks:")
                display_search_results(results)
    elif option == ["Neighbourhood", "Feature"] or option == ["Feature", "Neighbourhood"]:
        data = fd.fetch_data_from_url(PARKS_URL)
        park_neighbourhood_list = cld.clean_park_neighbourhood_data(data)
        park_neighbourhood_objects = cvd.convert_data_into_park_neighbourhood_objects(park_neighbourhood_list)
        neighbourhood_list = get_neighbourhood_list(park_neighbourhood_objects)
        neighbourhood = selctbox('Select a neighbourhood', neighbourhood_list, key="nei")
        feature = selctbox('Select a feature', FEATURE_OPTIONS, key="fea")
        if button("Search", 3):
            featured_parks_in_neighbourhood = []
            neighbourhood_parks = get_neighbourhood_parks(park_neighbourhood_objects, neighbourhood)
            if feature in ["Washroom", "Facilities", "Special Features"]:
                for park_neighbourhood in park_neighbourhood_objects:
                    if park_neighbourhood.name in neighbourhood_parks:
                        if feature == "Washroom":
                            if park_neighbourhood.washrooms == "Y":
                                featured_parks_in_neighbourhood.append(park_neighbourhood.name)
                        elif feature == "Facilities":
                            if park_neighbourhood.facilities == "Y":
                                featured_parks_in_neighbourhood.append(park_neighbourhood.name)
                        elif feature == "Special Features":
                            if park_neighbourhood.special_features == "Y":
                                featured_parks_in_neighbourhood.append(park_neighbourhood.name)
            elif feature == "Dog-off-leash areas/parks":
                data = fd.fetch_data_from_url(DOG_OFF_LEASH_PARKS_URL)
                dog_off_leash_parks_list = cld.clean_dog_off_leash_parks_data(data)
                dog_off_leash_parks_objects = cvd.convert_data_into_dog_off_leash_parks_objects(dog_off_leash_parks_list)
                facility_data = fd.fetch_data_from_url(PARKS_FACILITIES_URL)
                park_facilities_list = cld.clean_park_facilities_data(facility_data)
                park_facilities_objects = cvd.convert_data_into_park_facilities_objects(park_facilities_list)
                dog_off_leash_areas_parks = get_dog_off_leash_areas_parks(dog_off_leash_parks_objects, park_facilities_objects)
                for park in neighbourhood_parks:
                    if park in dog_off_leash_areas_parks:
                        featured_parks_in_neighbourhood.append(park)

            if featured_parks_in_neighbourhood != []:
                st.subheader("Parks in this neighbourhood with chosen feature:")
                display_search_results(featured_parks_in_neighbourhood)
            else:
                st.subheader("Sorry, no parks in this neighbourhood have the chosen feature. :cry:")


def explore_render():
    '''
    This function renders the explore feature.

    No Args

    No Returns
    '''
    st.header('Click button to explore')
    if button("Explore", 3):
        data = fd.fetch_data_from_url(PARKS_URL)
        park_neighbourhood_list = cld.clean_park_neighbourhood_data(data)
        park_neighbourhood_objects = cvd.convert_data_into_park_neighbourhood_objects(park_neighbourhood_list)
        random_park = get_a_random_park(park_neighbourhood_objects)
        for park in data:
            if park["name"] == random_park:
                del park["googlemapdest"]
                del park["parkid"]
                display_park_details_table(park)
                if park["specialfeatures"] == "Y":
                    st.subheader("This park has special features!")
                    special_feature_data = fd.fetch_data_from_url(PARKS_SPECIAL_FEATURES_URL)
                    park_special_features_list = cld.clean_park_special_features_data(special_feature_data)
                    park_special_features_objects = cvd.convert_data_into_park_special_features_objects(park_special_features_list)
                    for psf in park_special_features_objects:
                        if psf.name == random_park and psf.has_details():
                            park_special_features_details = {"Special Feature": psf.special_feature}
                            display_park_details_table(park_special_features_details)
                if park["facilities"] == "Y":
                    st.subheader("This park has facilities!")
                    facilities_data = fd.fetch_data_from_url(PARKS_FACILITIES_URL)
                    park_facilities_list = cld.clean_park_facilities_data(facilities_data)
                    park_facilities_objects = cvd.convert_data_into_park_facilities_objects(park_facilities_list)
                    for pf in park_facilities_objects:
                        if pf.name == random_park and pf.has_details():
                            park_facilities_details = {"Facility Type": pf.facility_type, "Facility Count": pf.facility_count}
                            display_park_details_table(park_facilities_details)
                if park["washrooms"] == "Y":
                    st.subheader("This park has washrooms!")
                    washrooms_data = fd.fetch_data_from_url(PARK_WASHROOMS_URL)
                    park_washrooms_list = cld.clean_park_washrooms_data(washrooms_data)
                    park_washrooms_objects = cvd.convert_data_into_park_washrooms_objects(park_washrooms_list)
                    for pw in park_washrooms_objects:
                        if pw.name == random_park and pw.has_details():
                            park_washrooms_details = {"Location": pw.location}
                            display_park_details_table(park_washrooms_details)


def charts_render():
    '''
    This function renders the charts feature.

    No Args

    No Returns
    '''
    data = fd.fetch_data_from_url(PARKS_URL)
    park_neighbourhood_list = cld.clean_park_neighbourhood_data(data)
    park_neighbourhood_objects = cvd.convert_data_into_park_neighbourhood_objects(park_neighbourhood_list)    
    neighbourhood_park_number = get_neighbourhood_park_number(park_neighbourhood_objects)
    st.header("Park numbers in each neighbouthood:")
    display_park_neighbourhood_bar_chart(neighbourhood_park_number)


def main():
    """
    Main function for the main page.

    No args

    No returns
    """
    try:
        st.sidebar.title("Navigation")
        if st.sidebar.button('Home', "Home"):
            st.session_state['page'] = 'home'
        if st.sidebar.button('Search', 'Search'):
            st.session_state['page'] = 'search'
        if st.sidebar.button('Explore', 'Explore'):
            st.session_state['page'] = 'explore'
        if st.sidebar.button('Charts', 'Charts'):
            st.session_state['page'] = 'charts'

        if 'page' in st.session_state:
            if st.session_state['page'] == 'home':
                display_home_page()
            if st.session_state['page'] == 'search':
                search_render()
            elif st.session_state['page'] == 'explore':
                explore_render()
            elif st.session_state['page'] == 'charts':
                charts_render()
    except ConnectionError as ex:
        print(f"ConnectionError: {ex}")
    except HTTPError as ex:
        print(f"HTTPError: {ex}")
    except Timeout as ex:
        print(f"Timeout: {ex}")
    except TooManyRedirects as ex:
        print(f"TooManyRedirects: {ex}")
    except ValueError as ex:
        print(f"ValueError: {ex}")
    except TypeError as ex:
        print(f"TypeError: {ex}")
    except IndexError as ex:
        print(f"IndexError: {ex}")


if __name__ == "__main__":
    main()
