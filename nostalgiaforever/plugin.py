
# coding: utf-8

# In[1]:


from IPython import get_ipython
from importnb.utils.pytest_plugin import *
from importnb.utils import pytest_plugin
import pytest


# In[2]:


class Module(pytest.Module):

    def collect(self):
        global loader
        get_ipython().run_line_magic('load_ext', 'pidgin')
        get_ipython().run_line_magic('pidgin', 'markdown conventions')
        with pytest_plugin.Notebook():
            return super().collect()


# In[3]:


pytest_plugin.Module = Module


# In[ ]:


if __name__ == '__main__':
    get_ipython().system('jupyter nbconvert --to python plugin.ipynb')

