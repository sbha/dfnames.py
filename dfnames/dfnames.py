"""
    dfnames

"""
import re

def snake_caser(col_names):
    new_names = col_names.strip()
    #new_names = re.sub(r"((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))", r'_\1', new_names)
    new_names = re.sub(r"([a-z])([A-Z])", r'\1_\2', new_names)
    new_names = re.sub(r"[^A-Za-z0-9]+", "_", new_names)
    new_names = re.sub(r"_+", "_", new_names)
    new_names = re.sub(r"^_+|_+$", "", new_names).lower()
    return new_names  

def camel_caser(col_names):
    new_names = snake_caser(col_names)
    new_names = re.sub(r'_([a-z]|[0-9])', lambda x: x.group(1).upper(), new_names)
    return new_names  

def paschal_caser(col_names):
    new_names = snake_caser(col_names)
    new_names = re.sub(r"_", " ", new_names)
    new_names = new_names.title()
    new_names = re.sub(r" ", "", new_names)
    return new_names

def title_caser(col_names):
    new_names = snake_caser(col_names)
    new_names = re.sub(r"_", " ", new_names)
    new_names = new_names.title()
    return new_names









