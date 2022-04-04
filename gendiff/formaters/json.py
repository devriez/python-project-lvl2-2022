import json


def json_render(diff_dict):
    '''
    Format diff result in json format.
    Parameters:
        diff_dict: Dictionary with the diff result.
    Returns:
        String of diff rows in json format.
    '''
    return json.dumps(diff_dict)
