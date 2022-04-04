import itertools
from gendiff.normalise_data import NORMALIZE_DATA


def stylish_render(diff_dict):  # noqa: C901
    '''
    Format diff result in stylish format.
    Parameters:
        diff_dict: Dictionary with the diff result.
    Returns:
        String of diff rows, structured by indents.
    '''

    def inner(tree, indent):
        result_string = ['{']
        step = indent * " "
        last_step = (indent - 2) * " "
        normalise_data = NORMALIZE_DATA['stylish']

        if type(tree) is not dict:
            return normalise_data(tree)

        sorted_nodes = sorted(tree.keys())

        for node in sorted_nodes:
            node_status = tree[node]['status']
            node_value = tree[node]['value']

            if node_status == 'added':
                line = f"{step}+ {node}: {inner(node_value, indent + 4)}"
            elif node_status == 'removed':
                line = f"{step}- {node}: {inner(node_value, indent + 4)}"
            elif node_status == 'common':
                line = f"{step}  {node}: {inner(node_value, indent + 4)}"
            elif node_status == 'updated':
                line = (
                    f"{step}- {node}: {inner(node_value['old'], indent + 4)}"
                    '\n'
                    f"{step}+ {node}: {inner(node_value['new'], indent + 4)}"
                )

            result_string.append(line)

        result = itertools.chain(result_string, [f"{last_step}" + "}"])
        return ('\n').join(result)

    return inner(diff_dict, 2)
