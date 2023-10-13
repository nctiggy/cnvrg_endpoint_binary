"""Module to assist threading a function in python for an endpoint"""
from threading import Thread

from cnvrgv2 import Endpoint


class EndpointThread:
    """
    A class used to manage running a threaded process from a cncvrg endpoint

    Attributes
    ----------
    endpoint : cnvrgv2.Endpoint
        A cnvrg Endpoint object. If you do not pass in, we assume you want us
        to create this on your behalf.
    function_name : function
        The name of the function you wish to execute from within the endpoint
    function_kwargs : dict, default={}
        Argurments in list format that you wish to pass to the function

    Examples
    --------
    >>> from cnvrg_endpoint_binary import EndpointThread
    >>> kwargs = {}
    >>> kwargs["flag"] = true
    >>> et = EndpointThread(function_name=demo, function_args=kwargs)
    >>> result = eb.predict("input_arg")
    >>> print(result)
    """

    def __init__(self, **kwargs):
        self.endpoint = kwargs.get("endpoint", None)
        self.function_name = kwargs["function_name"]
        self.function_kwargs = kwargs.get("function_kwargs", {})
        if not self.endpoint:
            self._generate_endpoint()
        self.function_kwargs["endpoint"] = self.endpoint

    def run_thread(self):
        thread = Thread(target=self.function_name, kwargs=self.function_kwargs)
        thread.start()

    def _generate_endpoint(self):
        self.endpoint = Endpoint()
