

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
                results[key] = args[args.index(expected_arg) + 1]
    return results



