#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# Copyright 2019-2023 by Enron Group. All Rights Reserved.
#
# Permission to use, copy, modify, and distribute this software and its
# documentation for any purpose and without fee is hereby granted,
# provided that the above copyright notice appear in all copies and that
# both that copyright notice and this permission notice appear in
# supporting documentation, and that the name of Enron Group
# not be used in advertising or publicity pertaining to distribution
# of the software without specific, written prior permission.
# Enron Group DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING
# ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL
# Enron Group BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR
# ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER
# IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
# OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

	███╗   ███╗  ██████╗ ███████╗
	████╗ ████║ ██╔════╝ ██╔════╝
	██╔████╔██║ ╚█████╗  █████╗
	██║╚██╔╝██║  ╚═══██╗ ██╔══╝
	██║ ╚═╝ ██║ ██████╔╝ ███████╗
	╚═╝     ╚═╝ ╚═════╝  ╚══════╝
	
	MSE (multiple substitution encryption)

	Game engine for puzzle creation

	Created on Tuesday, January 22nd, 2019 at 01:10

Module: Multiple Substitution Encryption (MSE)
Description: Provides an engine for creating and solving puzzles using encryption and decryption mechanisms.

Functions:
- mse_cipher(msg, auto_copy=True): Encrypts a message using multiple algorithms.
- mse_decipher(msg, auto_copy=False): Decrypts a message to its original form.

Dependencies:
- Uses Block A (`complexify` and `decomplexify`), Block B (`cipher` and `decipher`), and Block C (`obscur` and `remove_group_charac_b`).

Author: enrongroup.fr
Version: 28.0.0
Date: January 30, 2024
"""

from pyperclip import copy
from bloc_a import complexify, decomplexify
from bloc_b import cipher, decipher
from bloc_c import obscur, remove_group_charac_b

def mse_cipher(msg, auto_copy=True):
    """
    Encrypts a message using a sequence of transformations.

    Args:
        msg (str): The input message to be encrypted.
        auto_copy (bool): If True, copies the encrypted message to the clipboard.

    Returns:
        str: The encrypted message.
    """
    if not isinstance(msg, str):
        raise ValueError("Input must be a string.")

    a = complexify(msg)
    b = cipher(a)
    c = obscur(b)

    if auto_copy:
        copy(c)

    return c

def mse_decipher(msg, auto_copy=False):
    """
    Decrypts a message to its original form.

    Args:
        msg (str): The encrypted message to be decrypted.
        auto_copy (bool): If True, copies the decrypted message to the clipboard.

    Returns:
        str: The original message.
    """
    if not isinstance(msg, str):
        raise ValueError("Input must be a string.")

    c = remove_group_charac_b(msg)
    b = decipher(c)
    a = decomplexify(b)

    if auto_copy:
        copy(a)

    return a

