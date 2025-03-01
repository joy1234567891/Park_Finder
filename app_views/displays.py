# -*- coding: utf-8 -*-
'''
@author: Jiayi Qian
CS 5001, Fall 2023
Final project

This file contains display functions to display home page, search results,
park detail table, and park charts.
'''


import streamlit as st
import pandas as pd


def display_home_page():
    '''
    This function displays the home page.

    No Args

    No Returns
    '''
    st.title('Park Finder :partying_face:')
    st.header("This web application helps you to find a park which satisfies your needs. :100:")
    st.subheader("Click 'Search' on the sidebar to start searching. :mag:")
    st.subheader("Click 'Explore' on the sidebar to generate a random park choice for you to explore. :game_die:")
    st.subheader("Click 'Charts' on the sidebar to view park charts. :bar_chart:")
    st.balloons()


def display_search_results(results):
    '''
    This function displays search results.

    Args:
        results(list): the search results

    No Returns

    Raises:
        TypeError: if results is not a list
    '''
    if not isinstance(results, list):
        raise TypeError('Results must be a list.')

    for result in results:
        st.write(result)


def display_park_details_table(park_details):
    '''
    This function displays a park details table.

    Args:
        park_details(dict): a dict storing a park's details

    No Returns

    Raises:
        TypeError: if park_details is not dict
    '''
    if not isinstance(park_details, dict):
        raise TypeError('Park details must be a dict.')

    df = pd.DataFrame(park_details, index=["Details"])
    st.table(df.T)


def display_park_neighbourhood_bar_chart(neighbourhood_park_number):
    '''
    This function displays a park-neighbourhood bar chart.

    Args:
        neighbourhood_park_number(dict): a dict where neighbourhood names are
        keys and the numbers of parks in each neighbourhood are values.

    No Returns

    Raises:
        TypeError: if neighbourhood_park_number is not dict
    '''
    if not isinstance(neighbourhood_park_number, dict):
        raise TypeError('Neighbourhood_park_number must be a dict.')

    df = pd.DataFrame(neighbourhood_park_number, index=["details"])
    st.bar_chart(df.T)
