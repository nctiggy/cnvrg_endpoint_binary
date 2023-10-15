import types
from threading import Thread
from unittest import TestCase, mock

import cnvrg_endpoint_binary

__author__ = "Craig Smith"
__copyright__ = "Craig Smith"
__license__ = "MIT"


def test_func():
    return True


eb = cnvrg_endpoint_binary.endpoint_thread.EndpointThread(
    function_name=test_func, endpoint="dummy"
)


class TestInit(TestCase):
    @mock.patch("cnvrg_endpoint_binary.endpoint_thread.Endpoint.__init__")
    def test_init_good_no_endpoint(self, mock_end_init):
        mock_end_init.return_value = None
        test_eb = cnvrg_endpoint_binary.EndpointThread(
            function_name=test_func, function_kwargs={"test": "answer"}
        )
        self.assertIsInstance(test_eb.function_name, types.FunctionType)
        self.assertIsInstance(
            test_eb.endpoint, cnvrg_endpoint_binary.endpoint_thread.Endpoint
        )
        self.assertEquals(
            test_eb.function_kwargs,
            {"test": "answer", "endpoint": test_eb.endpoint},
        )

    @mock.patch("cnvrg_endpoint_binary.endpoint_thread.Endpoint.__init__")
    def test_init_good_endpoint(self, mock_end_init):
        mock_end_init.return_value = None
        test_endpoint = cnvrg_endpoint_binary.endpoint_thread.Endpoint()
        test_eb = cnvrg_endpoint_binary.EndpointThread(
            function_name=test_func,
            function_kwargs={"test": "answer"},
            endpoint=test_endpoint,
        )
        self.assertTrue(
            isinstance(test_eb.function_name, types.FunctionType),
            "The function_name attribute is not a function type",
        )
        self.assertIsInstance(
            test_eb.endpoint, cnvrg_endpoint_binary.endpoint_thread.Endpoint
        )
        self.assertEquals(
            test_eb.function_kwargs,
            {"test": "answer", "endpoint": test_eb.endpoint},
        )


class TestRunThread(TestCase):
    def test_run_thread(self):
        thread = eb.run_thread()
        self.assertIsInstance(thread, Thread)
