from pidgin.markdown import load_ipython_extension
load_ipython_extension()
from pidgin.conventions import load_ipython_extension
load_ipython_extension()

with __import__('importnb').Notebook():
    from . import test_nostalgia

from pidgin.markdown import unload_ipython_extension
unload_ipython_extension()
from pidgin.conventions import load_ipython_extension
unload_ipython_extension()
