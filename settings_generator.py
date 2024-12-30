from random import randint

def gen(db):
    """
    Generates random settings for the encryption system.

    Args:
        db (str): The name of the database file to be used.

    Returns:
        str: A JSON-formatted string representing the settings.
    """
    min_len_carac = 5
    max_len_carac = randint(min_len_carac + 1, 7)

    min_len_carac_special = 3
    max_len_carac_special = 4

    min_nbr_key = 1000
    max_nbr_key = randint(min_nbr_key + 1, 5000)

    min_add_carac_b = 7
    max_add_carac_b = randint(min_add_carac_b + 1, 10)

    min_len_carac_group_b = randint(5, 8)
    max_len_carac_group_b = randint(min_len_carac_group_b, 15)

    text = f"""
        "cipher": "ascii_letters",
        "special_charac": "easintrluodchEASINTRLUODCH0123456789!#$%&'()*+,-./:;<=>?@[]",
        "substitue_with": "configs/{db}",
        "cipher_punctuation": "True",
        "cipher_accent": "True",
        "cipher_digits": "True",
        "charac_len": [{min_len_carac},{max_len_carac}],
        "len_special_charac": [{min_len_carac_special},{max_len_carac_special}],
        "key_number": [{min_nbr_key},{max_nbr_key}],
        "len_charac_group_b": [{min_len_carac_group_b},{max_len_carac_group_b}],
        "mini_add_group_b_charac": {min_add_carac_b},
        "max_add_group_b_charac": {max_add_carac_b}
    """

    return "{\n" + text + "\n}"

def get_random_setting(db):
    """
    Generates a random settings file and writes it to `configs/setting.json`.

    Args:
        db (str): The name of the database file to be used.
    """
    settings = gen(db)
    with open("configs/setting.json", "w") as config_file:
        config_file.write(settings)
