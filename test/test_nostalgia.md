---
---


```python
from functools import partial
from pytest import fixture
```


```python
@fixture
def ip(request):
    from IPython import get_ipython
    return get_ipython()
```


```python
def test_imports(ip):
    """These imports are lazy"""
    print(ip.user_ns.keys())
    from nostalgiaforever import informal, formal, continuous, ipyconfig
    assert all((informal, formal, automation, ipyconfig))
```
