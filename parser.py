

def parse(input, schema):
    args = input.split(" ")
    return Parser(args, schema).parse()


class Parser(object):

    def __init__(self, args, schema):
        self.args = args
        self.schema = schema

    def parse(self):
        results = {}
        for key, transform in self.schema.items():
            expected_arg = "-%s" % key
            if expected_arg not in self.args:
                continue
            if transform is None:
                results[key] = True
            else:
                val = self._get_next_in_list(expected_arg)
                self._verify_value(val)
                results[key] = transform(val)
        return results

    def _get_next_in_list(self,predecessor):
        """ return the value that comes immediately after the given predecessor
        """
        try:
            return self.args[self.args.index(predecessor) + 1]
        except IndexError:
            raise ValueError("Missing argument value for %s" % predecessor)

    def _verify_value(self, val):
        if val.strip("-") in self.schema:
            raise ValueError("Missing argument value")


