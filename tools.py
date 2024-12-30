#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module: Tools
Description: Provides utility functions for file and text management within the MSE system.

Functions:
- reset(): Removes temporary files and caches.
- mixer(): Shuffles characters in the current substitution file.
- rebuild(): Cleans and rebuilds the special characters file by removing duplicates.
- gen_db_text(name, length): Generates a text database file with specified length.
- get_mse_hash(): Computes a hash of the entire project for integrity checks.
- first_mixer(): Initializes character mixing and parameter generation for first-time users.


"""

import os
from random import shuffle, randint
import shutil
from configs.configs_setting import name, charac_sub
from settings_generator import get_random_setting
from hashlib import sha3_512
from colorama import Fore, Style

def reset():
    """
    Removes temporary files and caches to clean the project directory.
    """
    files_to_remove = ["keylib.txt", "user.data", "configs/light_weight.txt", "configs/ultra_light_weight.txt", "configs/perso.txt"]
    
    for file in files_to_remove:
        if os.path.exists(file):
            os.remove(file)

    try:
        shutil.rmtree("__pycache__")
        shutil.rmtree("configs/__pycache__")
    except FileNotFoundError:
        pass

def mixer():
    """
    Shuffles characters in the current substitution file.
    Example:
        Input: AAAZZZ -> Output: ZAAZAZ
    """
    reset()

    with open(name, "r", encoding="utf-8") as file:
        init = list(file.read())

    shuffle(init)

    with open(name, "w", encoding="utf-8") as file:
        file.write("".join(init))

def rebuild():
    """
    Rebuilds the special characters file by removing duplicates and unused characters.
    """
    reset()

    with open(name, "r", encoding="utf-8") as file:
        old_carac = file.read()

    new_carac = [e for e in old_carac if e not in charac_sub and e not in "\n"]

    with open(name, "w", encoding="utf-8") as file:
        file.write("".join(set(new_carac)))

def gen_db_text(name, length=3000):
    """
    Generates a new text database file of the specified length.

    Args:
        name (str): The name of the file to be generated.
        length (int): The length of the text to be written.
    """
    with open("configs/all.txt", "r", encoding="utf-8") as file:
        rg = file.read()

    new_data = rg[:length]
    with open(f"configs/{name}", "w", encoding="utf-8") as file:
        file.write(new_data)

def get_mse_hash():
    """
    Computes a hash for the project files to ensure integrity.

    Returns:
        str: The computed hash.
    """
    all_files_datas = b""

    for root, _, files in os.walk(os.path.dirname(__file__)):
        for filename in files:
            if filename not in ["requirement.txt", "user.data", "README.md"] and "cpython" not in filename:
                with open(os.path.join(root, filename), "rb") as file:
                    all_files_datas += file.read()

    return sha3_512(all_files_datas).hexdigest()

def first_mixer():
    """
    Initializes character mixing and parameter generation for first-time users.
    """
    if not os.path.exists("user.txt"):
        db = "all.txt"

        get_random_setting(db)

        with open("configs/all.txt", "r", encoding="utf-8") as file:
            data_length = randint(250, len(file.read()))

        gen_db_text(db, data_length)
        mixer()
        rebuild()

        mse_version_hash = get_mse_hash()

        print(Fore.RED + f"MSE version hash: {mse_version_hash}")
        print(Style.RESET_ALL)

        with open("user.txt", "w") as file:
            file.write(mse_version_hash)

first_mixer()
