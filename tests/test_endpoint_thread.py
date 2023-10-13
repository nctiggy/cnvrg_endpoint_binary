import types
from unittest import TestCase

from cnvrg_endpoint_binary import EndpointThread

__author__ = "Craig Smith"
__copyright__ = "Craig Smith"
__license__ = "MIT"


def test_func():
    pass


class TestInit(TestCase):
    def test_init_good_no_endpoint(self):
        test_eb = EndpointThread(function_name=test_func, endpoint="dummy")
        self.assertTrue(
            isinstance(test_eb.function_name, types.FunctionType),
            "The function_name attribute is not a function type",
        )
