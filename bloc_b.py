#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module: Block B
Description: Handles character substitution for encryption and decryption.

Functions:
- cipher(plain_text): Substitutes characters in the input text using a randomly chosen key.
- decipher(coded_msg): Restores the original text by reversing the substitution process.

Dependencies:
- Requires `keylib.txt` or generates it using the `key_lib_generator`.


"""

from configs.configs_setting import key_number, len_charac_sub, charac_sub
from random import choice
import os

# Ensure key library exists or generate it
if os.path.exists("keylib.txt"):
    with open('keylib.txt', 'r', encoding="utf-8") as key_file:
        key_list = key_file.readlines()
else:
    from key_generator import key_lib_generator
    key_lib_generator(key_number[0], key_number[1])
    with open('keylib.txt', 'r', encoding="utf-8") as key_file:
        key_list = key_file.readlines()

def cipher(plain_text):
    """
    Encrypts the input text by substituting each character using a random key.

    Args:
        plain_text (str): The text to be encrypted.

    Returns:
        str: The encrypted text.
    """
    if not isinstance(plain_text, str):
        raise ValueError("Input must be a string.")

    key = choice(key_list).strip().split(' ')

    for c in range(len_charac_sub):
        plain_text = plain_text.replace(charac_sub[c], key[c])

    return plain_text

def decipher(coded_msg):
    """
    Decrypts the input text by reversing the substitution process.

    Args:
        coded_msg (str): The text to be decrypted.

    Returns:
        str: The original text.
    """
    if not isinstance(coded_msg, str):
        raise ValueError("Input must be a string.")

    for key in key_list:
        key = key.strip().split(' ')

        for n in range(len_charac_sub):
            coded_msg = coded_msg.replace(key[n], charac_sub[n])

    return coded_msg



