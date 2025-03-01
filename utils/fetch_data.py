# -*- coding: utf-8 -*-
'''
@author: Jiayi Qian
CS 5001, Fall 2023
Final project

This file contains a function which fetches the park json data from a url.
'''


import requests
from requests.exceptions import (ConnectionError, HTTPError,
                                 Timeout, TooManyRedirects)


def fetch_data_from_url(url):
    '''
    This function reads park json data from url.

    Args:
        url(str): the web url

    Returns:
        data(list): a list of dictionaries

    Raises:
        TypeError: if url is not str
        ConnectionError
        HTTPError
        Timeout
        TooManyRedirects
    '''
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
        return data

    except ConnectionError:
        raise ConnectionError
    except HTTPError:
        raise HTTPError
    except Timeout:
        raise Timeout
    except TooManyRedirects:
        raise TooManyRedirects
