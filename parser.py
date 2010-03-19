

def parse(input, schema):
    args = input.split(" ")
    return _parse_list_of_args(args, schema)


def _parse_list_of_args(args, schema):
    results = {}
    for key, transform in schema.items():
        expected_arg = "-%s" % key
        if expected_arg in args:
            if transform is None:
                results[key] = True
            else:
                results[key] = transform(_get_next_in_list(args, expected_arg))
    return results


def _get_next_in_list(args, predecessor):
    """ return the value that comes immediately after the given predecessor
    """
    return args[args.index(predecessor) + 1]


