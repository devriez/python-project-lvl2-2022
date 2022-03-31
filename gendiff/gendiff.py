import json
from gendiff.parser import file_parsing


def generate_diff(file_path1, file_path2):
    dict1 = file_parsing(file_path1)
    dict2 = file_parsing(file_path2)
    diff_dict = make_diff_dict(dict1, dict2)
    return build_result_string(diff_dict)



def make_diff_dict(file1, file2):
    result = {}

    keys1 = set(file1.keys())
    keys2 = set(file2.keys())

    added_keys = keys2 - keys1
    deleted_keys = keys1 - keys2
    common_keys = keys1 & keys2

    for key in added_keys:
        result[key] = {'status': 'added', 'value': file2[key]}

    for key in deleted_keys:
        result[key] = {'status': 'deleted', 'value': file1[key]}

    for key in common_keys:
        if file1[key] == file2[key]:
            result[key] = {'status': 'unchanged', 'value': file1[key]}
        else:
            result[key] = {
                'status': 'changed',
                'value': {'old': file1[key], 'new': file2[key]}
            }

    return result


def build_result_string(diff_dict):
    diff_string = '{\n'
    sorted_keys = sorted(diff_dict.keys())

    for key in sorted_keys:
        if diff_dict[key]['status'] == 'added':
            diff_string += f"  + {key}: {diff_dict[key]['value']}\n"
        elif diff_dict[key]['status'] == 'deleted':
            diff_string += f"  - {key}: {diff_dict[key]['value']}\n"
        elif diff_dict[key]['status'] == 'unchanged':
            diff_string += f"    {key}: {diff_dict[key]['value']}\n"
        else:
            diff_string += f"  - {key}: {diff_dict[key]['value']['old']}\n"
            diff_string += f"  + {key}: {diff_dict[key]['value']['new']}\n"

    return diff_string + '}'