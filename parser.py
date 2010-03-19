

def parse(input, schema):
    args = input.split(" ")
    return _parse_list_of_args(args, schema)


def _parse_list_of_args(args, schema):
    results = {}
    for key, transform in schema.items():
        expected_arg = "-%s" % key
        if expected_arg not in args:
            continue
        if transform is None:
            results[key] = True
        else:
            val = _get_next_in_list(args, expected_arg)
            results[key] = transform(val)
    return results


def _get_next_in_list(args, predecessor):
    """ return the value that comes immediately after the given predecessor
    """
    try:
        return args[args.index(predecessor) + 1]
    except IndexError:
        raise ValueError("Missing argument value for %s" % predecessor)


