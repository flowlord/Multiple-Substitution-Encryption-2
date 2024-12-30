#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module: Key Generator
Description: Generates encryption keys and key libraries for the substitution encryption system.

Functions:
- get_random_charac(x): Creates a random string of a specified length from group_a characters.
- key_gen(len_charac_sub): Generates a substitution key for all characters in the defined set.
- key_lib_generator(min_nbr_key, max_nbr_key): Generates a library of keys and saves it to `keylib.txt`.

Dependencies:
- Requires configurations from `configs_setting`.


"""

from random import randint, choice
from configs.configs_setting import group_a, charac_sub, charac_len, len_special_charac, special_charac, len_charac_sub

def get_random_charac(x):
    """
    Creates a random string of specified length from group_a characters.

    Args:
        x (int): The length of the random string.

    Returns:
        str: A random string of characters from group_a.
    """
    return ''.join(choice(group_a) for _ in range(x))

def key_gen(len_charac_sub):
    """
    Generates a substitution key for all characters in the defined set.

    Args:
        len_charac_sub (int): The total number of characters in the substitution set.

    Returns:
        str: A substitution key formatted as space-separated strings.
    """
    key = ''

    for charac in range(len_charac_sub):
        charac_len_ = randint(charac_len[0], charac_len[1])
        special_charac_ = randint(len_special_charac[0], len_special_charac[1])

        if charac_sub[charac] in special_charac:
            key += f'{get_random_charac(special_charac_)} '
        key += f'{get_random_charac(charac_len_)} '

    return key.strip()

def key_lib_generator(min_nbr_key, max_nbr_key):
    """
    Generates a key library containing multiple substitution keys.

    Args:
        min_nbr_key (int): The minimum number of keys to generate.
        max_nbr_key (int): The maximum number of keys to generate.

    Writes:
        Creates a `keylib.txt` file with all generated keys.
    """
    with open('keylib.txt', 'w', encoding='utf-8') as file:
        for _ in range(min_nbr_key, max_nbr_key):
            file.write(f'{key_gen(len_charac_sub)}\n')
