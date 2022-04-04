from gendiff.normalise_data import NORMALIZE_DATA


def plain_render(diff_dict):  # noqa: C901
    '''
    Format diff result in plain format.
    Parameters:
        diff_dict: Dictionary with the diff result.
    Return:
        String of diff rows. Which nodes and values were added, removed, deleted
        Ordered by name
    '''
    normalise_data = NORMALIZE_DATA['plain']

    def inner(tree, result=[], level=[]):
        sorted_nodes = sorted(tree.keys())

        for node in sorted_nodes:
            node_value = tree[node]['value']
            node_status = tree[node]['status']
            node_path = ('.').join(level + [node])

            if node_status == 'added':
                value = normalise_data(node_value)
                result.append(
                    f"Property '{node_path}' was added with value: {value}"
                )

            elif node_status == 'removed':
                result.append(f"Property '{node_path}' was removed")

            elif node_status == 'updated':
                value_old = normalise_data(node_value['old'])
                value_new = normalise_data(node_value['new'])
                result.append(
                    f"Property '{node_path}' was updated. From {value_old} to {value_new}"  # noqa: E501
                )

            elif node_status == 'common' and (type(node_value) is dict):
                inner(node_value, result, level + [node])

        return ('\n').join(result)

    return inner(diff_dict)
