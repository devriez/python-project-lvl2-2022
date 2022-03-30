import json


def make_lowcase_for_boolean_name_in_json(json_file):
    for i in json_file:
        if type(json_file[i]) is bool:
            json_file[i] = str(json_file[i]).lower()


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    make_lowcase_for_boolean_name_in_json(file1)
    make_lowcase_for_boolean_name_in_json(file2)
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

    sorted_keys = sorted(result.keys())
    result_string = '{\n'
    for key in sorted_keys:
        if result[key]['status'] == 'added':
            result_string += f"  + {key}: {result[key]['value']}\n"
        elif result[key]['status'] == 'deleted':
            result_string += f"  - {key}: {result[key]['value']}\n"
        elif result[key]['status'] == 'unchanged':
            result_string += f"    {key}: {result[key]['value']}\n"
        else:
            result_string += f"  - {key}: {result[key]['value']['old']}\n"
            result_string += f"  + {key}: {result[key]['value']['new']}\n"

    return result_string + '}'
