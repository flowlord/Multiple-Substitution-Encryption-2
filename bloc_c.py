#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module: Block C
Description: Performs advanced transformations on text after substitution.

Functions:
- get_random_charac_group_b(): Generates a random string from group_b characters.
- combine_charac_a(string_a, string_b): Merges two strings by alternating their characters.
- combine_charac_b(string_a): Combines a string with random characters from group_b.
- combine_charac_c(plain_text, x): Randomly inserts characters from group_b into the text x times.
- obscur(string): Applies multiple transformations to obscure the text.
- remove_group_charac_b(code): Removes all characters from group_b in the given text.

Dependencies:
- Uses configurations from `configs_setting`.


"""

from configs.configs_setting import len_charac_group_b, group_b, mini_add_group_b_charac, maxi_add_group_b_charac
from random import choice, randint

def get_random_charac_group_b():
    """
    Generates a random string using characters from group_b.

    Returns:
        str: A random string of characters from group_b.
    """
    mini, maxi = len_charac_group_b[0], len_charac_group_b[1]
    return ''.join(choice(group_b) for _ in range(mini, maxi))

def combine_charac_a(string_a, string_b):
    """
    Alternates characters from two strings to merge them.

    Args:
        string_a (str): The first string.
        string_b (str): The second string.

    Returns:
        str: The merged string.
    """
    string_c = ''
    min_len = min(len(string_a), len(string_b))

    for i in range(min_len):
        string_c += string_a[i] + string_b[i]

    if len(string_a) > len(string_b):
        string_c += string_a[min_len:]
    elif len(string_b) > len(string_a):
        string_c += string_b[min_len:]

    return string_c

def combine_charac_b(string_a):
    """
    Combines a string with random characters from group_b.

    Args:
        string_a (str): The input string.

    Returns:
        str: The combined string.
    """
    string_b = get_random_charac_group_b()
    return combine_charac_a(string_a, string_b)

def combine_charac_c(plain_text, x):
    """
    Randomly inserts characters from group_b into the text x times.

    Args:
        plain_text (str): The input text.
        x (int): The number of characters to insert.

    Returns:
        str: The modified text.
    """
    plain_text = list(plain_text)

    for _ in range(x):
        position = randint(0, len(plain_text))
        plain_text.insert(position, get_random_charac_group_b())

    return ''.join(plain_text)

def obscur(string):
    """
    Applies multiple transformations to obscure the text.

    Args:
        string (str): The input text.

    Returns:
        str: The obscured text.
    """
    string = combine_charac_a(string, get_random_charac_group_b())
    string = combine_charac_b(string)
    string = combine_charac_c(string, randint(mini_add_group_b_charac, maxi_add_group_b_charac))

    return string

def remove_group_charac_b(code):
    """
    Removes all characters from group_b in the given text.

    Args:
        code (str): The input text.

    Returns:
        str: The cleaned text.
    """
    return ''.join(char for char in code if char not in group_b)


