from typing import Dict, Literal, Union

class Console:
    "an object with methods to interact with the browser console. Its interface is browser-specific. It exposes at least the method log(msg), which prints the message msg in the console"
    def log(self, message: str): ...

class Style:
    display: Literal["block", "inline", "none"]

class HTMLElement:
    style: Style

class Document(Dict[str, HTMLElement]):
    'an object that represents the HTML document currently displayed in the browser window. The interface of this object is described in section "Browser interface"'

class Window:
    "an object that represents the browser window"

def alert(message: str):
    "a function that prints the message in a pop-up window. Returns None"

def bind(target: str, event: str):
    "a function used as a decorator for event binding. Cf. section events."

def confirm(message: str):
    "a function that prints the message in a window, and two buttons (ok/cancel). Returns True if ok, False if cancel"

console = Console()
document = Document()

class DOMEvent:
    "the class of DOM events"

def load(script_url: str):
    """
    Load the Javascript library at address script_url.
    This function uses a blocking Ajax call. It must be used when one can't load the Javascript library in the html page by <script src="prog.js"></script>.
    The names inserted by the library inside the global Javascript namespace are available in the Brython script as attributes of the window object.
    """

def prompt(message: str, default: str = ""):
    "a function that prints the message in a window, and an entry field. Returns the entered value ; if no value was entered, return default if defined, else the empty string"

def run_script(src: str, name: Union[str, None] = None):
    "this function executes the Python source code in src with an optional name. It can be used as an alternative to exec(), with the benefit that the indexedDB cache is used for importing modules from the standard library."

window = Window()
