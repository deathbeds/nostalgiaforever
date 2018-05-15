---
---


```python
    from IPython import get_ipython
    from importnb.utils.pytest_plugin import *
    from importnb.utils import pytest_plugin
    import pytest
```


```python
    class Module(pytest.Module):
        def collect(self):
            global loader
            %load_ext pidgin
            %pidgin markdown conventions
            with pytest_plugin.Notebook():
                return super().collect()
```


```python
    pytest_plugin.Module = Module
```


```python
    if __name__ == '__main__':
        !jupyter nbconvert --to python plugin.ipynb
```

    [NbConvertApp] Converting notebook plugin.ipynb to python
    [NbConvertApp] Writing 608 bytes to plugin.py

