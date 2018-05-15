from pidgin.markdown import load_ipython_extension
load_ipython_extension()
from pidgin.conventions import load_ipython_extension
load_ipython_extension()

with __import__('importnb').Notebook():
    from . import importing, testing, reuse
