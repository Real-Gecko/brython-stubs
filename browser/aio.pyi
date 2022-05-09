from typing import Callable, Literal, Union

class Request:
    """Instances of class Request, as returned by await ajax(), await get() or await post()"""

    data: Union[str, bytes]
    response_headers: dict
    status: int
    statusText: str

class DOMEvent: ...

def ajax(
    method: Literal["GET", "POST", "PUT"],
    url: str,
    format: Literal["text", "binary", "dataURL"] = "text",
    headers: Union[dict, None] = None,
    data: Union[str, dict, None] = None,
    cache: bool = False,
) -> Request:
    """
    req = await ajax("GET", url) inside an asynchronous function gives back control to the main program, and resumes the function when the Ajax request of the type method ("GET", "POST", "PUT", etc.) to the specified URL is completed. The return value is an instance of the class Request (see below).
    format is the expected response format. It can be one of:
        "text" : the response is a string
        "binary" : an instance of class bytes
        "dataURL" : a string formatted as dataURL
    headers is a dictionary with the HTTP headers to send with the request.
    data is a string or a dictionary that will be sent with the request to form the query string for a "GET" request, or the request body for "POST".
    cache is a boolean indicating if the browser cache should be used
    """

def get(
    url: str,
    format: Literal["text", "binary", "dataURL"] = "text",
    headers: Union[dict, None] = None,
    data: Union[str, dict, None] = None,
    cache: bool = False,
) -> Request:
    """shortcut for ajax("GET", url...)"""

def post(
    url: str,
    format: Literal["text", "binary", "dataURL"] = "text",
    headers: Union[dict, None] = None,
    data: Union[str, dict, None] = None,
    cache: bool = False,
) -> Request:
    """shortcut for ajax("POST", url...)"""

def event(element: str, name: Literal["click"]) -> DOMEvent:
    """evt = await aio.event(element, "click") suspends execution of an asynchronous function until the user clicks on the specified element. The return value is an instance of the DOMEvent class (cf. section events)"""

def sleep(seconds: int):
    """In an asynchronous function, await sleep(n) gives back control to the main program and resumes function execution after n seconds."""

def run(coroutine: Callable):
    """Runs a coroutine, ie the result of a call to an asynchronous function defined by async def. This is a non blocking function: it doesn't wait until the asynchronous function is completed to execute the instructions in the following lines. The time when the next instructions are run is not (easily) predictable."""
