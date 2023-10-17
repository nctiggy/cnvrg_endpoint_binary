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
    >>> running = et.run_thread().thread.is_alive()
    >>> print(running)
    """

    def __init__(self, **kwargs):
        self.endpoint = kwargs.get("endpoint", None)
        self.function_name = kwargs["function_name"]
        self.function_kwargs = kwargs.get("function_kwargs", {})
        if not self.endpoint:
            self._generate_endpoint()
        self.function_kwargs["endpoint"] = self.endpoint
        self.thread = None

    def run_thread(self):
        """
        This method runs the specificed function in a thread. Code after this
        method will execute while the threaded function runs in parallel.

        Returns
        -------
        self : EndpointThread
            Returns an instance of the EndpointThread object that has an
            updated thread attribute with the new thread
        """
        self.thread = Thread(
            target=self.function_name, kwargs=self.function_kwargs
        )
        self.thread.start()
        return self

    def _generate_endpoint(self):
        self.endpoint = Endpoint()
