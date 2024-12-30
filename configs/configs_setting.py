#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module: Configurations Setting
Description: This script handles the loading and processing of cipher and substitution character configurations.

Requirements:
- A JSON configuration file located at `configs/setting.json`.
- A file specified by `substitute_with` in the configuration file containing substitution characters.

Usage:
- Used for encryption or text processing systems requiring specific cipher configurations.

K3rn3l
"""

import json
import os
from string import ascii_lowercase, ascii_uppercase, ascii_letters, digits, punctuation

# Define accent characters
ACCENT_CHARACTERS = "ÄÀÂÉÈÊËÎÏÔÙÛÜÇàâéèêëîïôùûüç"

# Load configuration data
try:
    with open("configs/setting.json", "r", encoding="utf-8") as config_file:
        config_data = json.load(config_file)
except FileNotFoundError:
    raise Exception("ERROR: Configuration file 'configs/setting.json' not found.")
except json.JSONDecodeError:
    raise Exception("ERROR: Failed to parse 'configs/setting.json'. Ensure it is a valid JSON file.")

# Validate and process cipher settings
cipher_type = config_data.get("cipher")
if cipher_type == "ascii_lowercase":
    charac_sub = ascii_lowercase
elif cipher_type == "ascii_uppercase":
    charac_sub = ascii_uppercase
elif cipher_type == "ascii_letters":
    charac_sub = ascii_letters
else:
    raise Exception("ERROR: Unknown cipher option. Expected 'ascii_lowercase', 'ascii_uppercase', or 'ascii_letters'.")

# Add punctuation to the character set if specified
if config_data.get("cipher_punctuation") == "True":
    charac_sub += punctuation
elif config_data.get("cipher_punctuation") != "False":
    raise Exception("ERROR: Invalid value for 'cipher_punctuation'. Use 'True' or 'False'.")

# Add digits to the character set if specified
if config_data.get("cipher_digits") == "True":
    charac_sub += digits
elif config_data.get("cipher_digits") != "False":
    raise Exception("ERROR: Invalid value for 'cipher_digits'. Use 'True' or 'False'.")

# Add accent characters to the character set if specified
if config_data.get("cipher_accent") == "True":
    charac_sub += ACCENT_CHARACTERS
elif config_data.get("cipher_accent") != "False":
    raise Exception("ERROR: Invalid value for 'cipher_accent'. Use 'True' or 'False'.")

# Add special characters and space
special_charac = config_data.get("special_charac", "") + '\"\\'
charac_sub += " "
len_charac_sub = len(charac_sub)

# Validate substitution file
substitute_file = config_data.get("substitue_with")
if not os.path.exists(substitute_file):
    raise Exception(f"ERROR: Substitution file '{substitute_file}' not found.")

# Read substitution characters
try:
    with open(substitute_file, "r", encoding="utf-8") as file:
        init_charac_group = "".join(file.readlines()).strip()
except Exception as e:
    raise Exception(f"ERROR: Failed to read substitution file: {e}")

# Split substitution characters into groups
middle_index = len(init_charac_group) // 2
group_a = init_charac_group[:middle_index]
group_b = init_charac_group[middle_index:]

# Load additional settings
charac_len = config_data.get("charac_len")
len_special_charac = config_data.get("len_special_charac")
key_number = config_data.get("key_number")
len_charac_group_b = config_data.get("len_charac_group_b")
mini_add_group_b_charac = config_data.get("mini_add_group_b_charac")
maxi_add_group_b_charac = config_data.get("max_add_group_b_charac")

# Debugging information (can be removed in production)
"""print(f"Character Substitution Set: {charac_sub}")
print(f"Group A: {group_a}")
print(f"Group B: {group_b}")"""



