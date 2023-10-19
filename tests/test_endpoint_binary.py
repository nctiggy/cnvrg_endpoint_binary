import io
from unittest import TestCase, mock

import cnvrg_endpoint_binary

__author__ = "Craig Smith"
__copyright__ = "Craig Smith"
__license__ = "MIT"


eb = cnvrg_endpoint_binary.endpoint_binary.EndpointBinary(
    binary_name="ls", binary_args=["-ltra"], endpoint="dummy"
)


class Object(object):
    pass


class TestInit(TestCase):
    @mock.patch("cnvrg_endpoint_binary.endpoint_binary.Endpoint.__init__")
    def test_init_good_endpoint(self, mock_end):
        mock_end.return_value = None
        test_eb = cnvrg_endpoint_binary.endpoint_binary.EndpointBinary(
            binary_name="./main"
        )
        self.assertEqual(test_eb.binary_name, "./main")
        self.assertIsInstance(
            test_eb.endpoint, cnvrg_endpoint_binary.endpoint_binary.Endpoint
        )
        self.assertEqual(test_eb.binary_args, [])
        self.assertEqual(test_eb.metrics_prefix, "cnvrg_tag")
        self.assertEqual(test_eb.delimiter, "_")

    def test_init_good_no_endpoint(self):
        test_eb = cnvrg_endpoint_binary.endpoint_binary.EndpointBinary(
            binary_name="./main",
            endpoint="dummy",
            binary_args=["-arg"],
            metrics_prefix="test_pre",
            delimiter=",",
        )
        self.assertEqual(test_eb.binary_name, "./main")
        self.assertEqual(test_eb.endpoint, "dummy")
        self.assertEqual(test_eb.binary_args, ["-arg"])
        self.assertEqual(test_eb.metrics_prefix, "test_pre")
        self.assertEqual(test_eb.delimiter, ",")


class TestConvCamCase(TestCase):
    def test_return(self):
        result = eb._convert_camelcase("test_camel")
        self.assertEqual(result, "testCamel")


class TestIsPrefix(TestCase):
    def test_is_metric(self):
        result = eb._is_prefix("cnvrg_tag_test: test_val")
        self.assertEqual(result, "metric")

    def test_is_regular_stdout(self):
        result = eb._is_prefix("Random strings")
        self.assertFalse(result)

    def test_is_result(self):
        result = eb._is_prefix('{"json": "object"}')
        self.assertEqual(result, "result")


class TestExtractTag(TestCase):
    def test_tag(self):
        key, value = eb._extract_tag("cnvrg_tag_key: value")
        self.assertEqual(key, "key")
        self.assertEqual(value, "value")


class TestDealWithStdOut(TestCase):
    def test_if_result(self):
        mock_process = Object()
        mock_process.stdout = io.StringIO('{"result_key": "value"}')
        result = eb._deal_with_stdout(mock_process)
        self.assertEqual(result["result_key"], "value")

    @mock.patch("cnvrg_endpoint_binary.endpoint_binary.Endpoint.__init__")
    @mock.patch("cnvrg_endpoint_binary.endpoint_binary.Endpoint.log_metric")
    def test_if_metric(self, mock_ep, mock_lm):
        mock_ep.return_value = None
        mock_lm.return_value = None
        mock_process = Object()
        mock_process.stdout = io.StringIO("cnvrg_tag_key: value")
        mock_eb = cnvrg_endpoint_binary.endpoint_binary.EndpointBinary(
            binary_name="./main"
        )
        result = mock_eb._deal_with_stdout(mock_process)
        self.assertIsNone(result)

    def test_if_metric_no_endpoint(self):
        mock_process = Object()
        mock_process.stdout = io.StringIO("cnvrg_tag_key: value")
        result = eb._deal_with_stdout(mock_process)
        self.assertIsNone(result)

    def test_if_other(self):
        mock_process = Object()
        mock_process.stdout = io.StringIO("non-key output")
        result = eb._deal_with_stdout(mock_process)
        self.assertIsNone(result)

    def test_if_bytes(self):
        mock_process = Object()
        mock_process.stdout = io.BytesIO(b"non-key output\nsecondline")
        result = eb._deal_with_stdout(mock_process)
        self.assertIsNone(result)


class TestPredict(TestCase):
    @mock.patch("cnvrg_endpoint_binary.endpoint_binary.Popen.__init__")
    @mock.patch(
        "cnvrg_endpoint_binary.endpoint_binary.ThreadWithReturnValue.__init__"
    )
    @mock.patch(
        "cnvrg_endpoint_binary.endpoint_binary.ThreadWithReturnValue.start"
    )
    @mock.patch(
        "cnvrg_endpoint_binary.endpoint_binary.ThreadWithReturnValue.join"
    )
    def test_return(self, mock_popen, mock_thread, mock_start, mock_join):
        mock_popen.return_value = None
        mock_thread.return_value = None
        mock_start.return_value = None
        mock_join.return_value = None
        result = eb.predict()
        self.assertIsNone(result)
