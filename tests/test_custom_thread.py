from unittest import TestCase, mock

import cnvrg_endpoint_binary

__author__ = "Craig Smith"
__copyright__ = "Craig Smith"
__license__ = "MIT"


def test():
    return "test"


class TestInit(TestCase):
    @mock.patch("cnvrg_endpoint_binary.custom_thread.Thread.__init__")
    def test_init_good(self, mock_thread):
        mock_thread.return_value = None
        result = cnvrg_endpoint_binary.custom_thread.ThreadWithReturnValue(
            target="test"
        )
        self.assertIsNone(result._return)


class TestStart(TestCase):
    def test_start(self):
        thread = cnvrg_endpoint_binary.custom_thread.ThreadWithReturnValue(
            target=test
        )
        thread.start()
        result = thread.join()
        self.assertEqual(result, "test")
