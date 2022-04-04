from gendiff.parser import file_parsing
from gendiff.formaters.stylish import stylish_render
from gendiff.formaters.plain import plain_render
from gendiff.formaters.json import json_render


def generate_diff(file_path1, file_path2, format_name='stylish'):
    """
    Generate a diff for a given files.
    Parameters:
        file_path1: A path to the first diff file.
        file_path2: A path to the second diff file.
        formater_name: Diff output format.
    Returns:
        Diff of the given files.
    """
    dict1 = file_parsing(file_path1)
    dict2 = file_parsing(file_path2)
    diff_dict = calc_diff_dict(dict1, dict2)
    formater = {
        'stylish': stylish_render,
        'plain': plain_render,
        'json': json_render
    }

    return formater[format_name](diff_dict)


def make_diff_representation(value):
    """
    Make diff_representation for value that didn't chnage.
    Parameters:
        value
    Returns:
        Representation in dict format.
    """
    if type(value) is not dict:
        return value
    result = {}
    for i in value:
        result[i] = {
            'status': 'common',
            'value': make_diff_representation(value[i])
        }
    return result


def calc_diff_dict(file1, file2):
    """
    Generate a diff for a given dictionaries.
    Parameters:
        dict1: The first dictionary to compare.
        dict2: The second dictionary to compare.
    Returns:
        Diff of the given dictionaries in a dict format.
    """

    result = {}

    keys1 = set(file1.keys())
    keys2 = set(file2.keys())

    added_keys = keys2 - keys1
    removed_keys = keys1 - keys2
    common_keys = keys1 & keys2

    for key in added_keys:
        result[key] = {
            'status': 'added',
            'value': make_diff_representation(file2[key])
        }

    for key in removed_keys:
        result[key] = {
            'status': 'removed',
            'value': make_diff_representation(file1[key])
        }

    for key in common_keys:
        if file1[key] == file2[key]:
            result[key] = {
                'status': 'common',
                'value': make_diff_representation(file1[key])
            }
        elif (type(file1[key]) is dict) and (type(file2[key]) is dict):
            result[key] = {
                'status': 'common',
                'value': calc_diff_dict(file1[key], file2[key])
            }
        else:
            result[key] = {
                'status': 'updated',
                'value': {
                    'old': make_diff_representation(file1[key]),
                    'new': make_diff_representation(file2[key])
                }
            }

    return result
