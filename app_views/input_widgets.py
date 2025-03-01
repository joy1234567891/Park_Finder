# -*- coding: utf-8 -*-
'''
@author: Jiayi Qian
CS 5001, Fall 2023
Final project

This file contains functions which use streamlit input widgets.
'''


import streamlit as st


def button(button_label, key):
    '''
    This function uses streamlit's button input widget.

    Args:
        button_label(str): label of the button
        key(str or int): a key to differentiate
                         different buttons used in the app

    Returns: Bool

    Raises:
        TypeError: if label is not str, or if key is not str or int
    '''
    if not isinstance(button_label, str):
        raise TypeError('Label must be a str.')
    if not isinstance(key, (str, int)):
        raise TypeError('Key must be a str or int.')

    return st.button(button_label, key=key)


def multiselect(label, options, key):
    '''
    This function uses streamlit's multiselect input widget.

    Args:
        label(str): label of the multiselect box.
        options(list): a list of options for the multiselect box.
        key(str or int): a key to differentiate different
                         multiselect boxes used in the app

    Returns:
        multiselect_option(list): user's multiselect option

    Raises:
        TypeError: if label is not str, or if options is not a list.
                   or if key is not str or int
    '''
    if not isinstance(label, str):
        raise TypeError('Label must be a str.')
    if not isinstance(options, list):
        raise TypeError('Options must be a list.')
    if not isinstance(key, (str, int)):
        raise TypeError('Key must be a str or int.')

    multiselect_option = st.multiselect(label, options, key=key)
    return multiselect_option


def selctbox(label, options, key):
    '''
    This function uses streamlit's selectbox input widget.

    Args:
        label(str): label of the select box.
        options(list): a list of options for the select box.
        key(str or int): a key to differentiate
                         different selectboxes used in the app

    Returns:
        selectbox_option(list): user's selectbox option

    Raises:
        TypeError: if label is not str, or if options is not a list.
                   or if key is not str or int
    '''
    if not isinstance(label, str):
        raise TypeError('Label must be a str.')
    if not isinstance(options, list):
        raise TypeError('Options must be a list.')
    if not isinstance(key, (str, int)):
        raise TypeError('Key must be a str or int.')

    selectbox_option = st.selectbox(label, options, key=key)
    return selectbox_option
