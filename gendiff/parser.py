import os
import yaml


def make_lowercase_for_boolean_name_in_data(json_file):
    for i in json_file:
        if type(json_file[i]) is bool:
            json_file[i] = str(json_file[i]).lower()


def file_parsing(path):
    full_path = os.path.abspath(path)
    data = yaml.safe_load(open(full_path))
    make_lowercase_for_boolean_name_in_data(data)
    return data