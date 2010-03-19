from nose import tools as NT
from parser import parse



class ParserTest(object):

    schema = None
    input = None
    expected = None

    def setup(self):
        self.results = parse(self.input, self.schema)

    def test_results_matches_expected(self):
        NT.assert_equals(self.expected, self.results)


class DavesExample(ParserTest):

    schema = {
            "f": str,
            "x": None,  #specifies that a bool True will be returned if present
            "r": int
            }

    input = "-f foo.cfg -x -r 4286"

    expected = {
            "f": "foo.cfg",
            "x": True,
            "r": 4286
            }


class TestFlagPresent(DavesExample):

    input = "-x"

    expected = {
            "x": True
            }


class TestFlagMissing(DavesExample):

    input = ""

    expected = {
            }


class TestStringValue(DavesExample):

    input = "-f foo.cfg"

    expected = {
            "f": "foo.cfg"
            }



class TestIntegerValue(DavesExample):

    input = "-r 9999"

    expected = {
            "r": 9999
            }



class TestStringsAndFlags(DavesExample):

    input = "-f foo.cfg -x"

    expected = {
            "f": "foo.cfg",
            "x": True
            }


