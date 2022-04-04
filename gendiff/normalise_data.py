
def normalise_data_stylish(data):
    """
    Normilize data for output format stylish.

    Parameters:
        data: income data (not dict)
    Return:
        Boolean - 'true' and 'false'
        None - 'null'
        other - without changes

    """
    if type(data) is bool:
        return str(data).lower()

    if data is None:
        return 'null'

    return data


def normalize_data_plain(data):
    """
    Normilize data for output format plain.

    Parameters:
        data: income data
    Return:
        dict and list - '[complex value]'
        Boolean - 'true' and 'false'
        None - 'null'
        string - '{string}'
        int - without changes

    """
    if type(data) == dict or type(data) == list:
        return '[complex value]'
    if type(data) == bool:
        return str(data).lower()
    if data is None:
        return 'null'
    if type(data) == str:
        return f"'{data}'"
    return data


NORMALIZE_DATA = {
    'plain': normalize_data_plain,
    'stylish': normalise_data_stylish
}
