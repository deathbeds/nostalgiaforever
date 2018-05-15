---
---

# Reusing `importing` and `testing`

`importing` and `testing` contain tests that can be imported and reused by other testing tools.


```python
    
    from IPython import get_ipython
    o = __name__ == '__main__'
    with __import__('importnb').Notebook():
        try: from .util import __ipython__
        except:
            if o: 
                %reload_ext pidgin
                %pidgin markdown conventions
            from util import __ipython__
```


```python
<hr/><hr/><hr/><hr/><hr/>

# This notebook - `reuse.ipynb` - imports `testing`, `importing`, and `reuse`
    
    from importnb import Notebook, reload
    with Notebook():
        try:
            import importing, testing, reuse
        except:
            from . import importing, testing, reuse
        
```


<hr/><hr/><hr/><hr/><hr/>

# This notebook - `reuse.ipynb` - imports `testing`, `importing`, and `reuse`
    
    from importnb import Notebook, reload
    with Notebook():
        try:
            import importing, testing, reuse
        except:
            from . import importing, testing, reuse
        



```python
    import pytest
    if __name__ == '__main__':
        pytest.main([
            getattr(object, '__file__') for object in (importing, testing)
        ] + '-p no:pytest-importnb'.split())
```


    import pytest
    if __name__ == '__main__':
        pytest.main([
            getattr(object, '__file__') for object in (importing, testing)
        ] + '-p no:pytest-importnb'.split())


    ============================= test session starts ==============================
    platform darwin -- Python 3.6.3, pytest-3.5.0, py-1.5.3, pluggy-0.6.0
    benchmark: 3.1.1 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
    rootdir: /Users/tonyfast/ahypothesis, inifile:
    plugins: cov-2.5.1, benchmark-3.1.1, hypothesis-3.56.5, nostalgiaforever-0.0.2
    collected 4 items
    
    importing.ipynb ..                                                       [ 50%]
    testing.ipynb ..                                                         [100%]
    
    =============================== warnings summary ===============================
    None
      Module already imported so cannot be rewritten: hypothesis
    
    -- Docs: http://doc.pytest.org/en/latest/warnings.html
    ===================== 4 passed, 1 warnings in 0.06 seconds =====================



```python
    
    http://doc.pytest.org/
```



        <iframe
            width="800"
            height="600"
            src="http://doc.pytest.org/"
            frameborder="0"
            allowfullscreen
        ></iframe>
        



```python
# [Pytest plugins](https://docs.pytest.org/en/2.7.3/plugins_index/index.html)

## `pytest-importnb` 

Discovers notebooks as pytest python modules.  This idea builds off of [pytest-ipynb](https://github.com/zonca/pytest-ipynb/tree/master/pytest_ipynb), [nbval](https://github.com/computationalmodelling/nbval), and [ipynb](https://github.com/ipython/ipynb/tree/master/ipynb).
```


# [Pytest plugins](https://docs.pytest.org/en/2.7.3/plugins_index/index.html)

## `pytest-importnb` 

Discovers notebooks as pytest python modules.  This idea builds off of [pytest-ipynb](https://github.com/zonca/pytest-ipynb/tree/master/pytest_ipynb), [nbval](https://github.com/computationalmodelling/nbval), and [ipynb](https://github.com/ipython/ipynb/tree/master/ipynb).



```python
## `pytest-benchmark`

---
    
### Compare a `numpy` function and a `numba`

    def sum2d(arr):
        M, N = arr.shape
        result = 0.0
        for i in range(M):
            for j in range(N):
                result += arr[i,j]
        return result
    
---    

    def test_py(benchmark):
        from numpy import arange
        benchmark(sum2d, arange(100).reshape(10,10))

    try:
        from numba import jit
        from numpy import arange
        def test_jit(benchmark):
            benchmark(jit(sum2d), arange(100).reshape(10,10))
    except: ...
```


## `pytest-benchmark`

---
    
### Compare a `numpy` function and a `numba`

    def sum2d(arr):
        M, N = arr.shape
        result = 0.0
        for i in range(M):
            for j in range(N):
                result += arr[i,j]
        return result
    
---    

    def test_py(benchmark):
        from numpy import arange
        benchmark(sum2d, arange(100).reshape(10,10))

    try:
        from numba import jit
        from numpy import arange
        def test_jit(benchmark):
            benchmark(jit(sum2d), arange(100).reshape(10,10))
    except: ...



```python
# Run the benchmark tests
    
    import pytest
    if __name__ == '__main__':
        pytest.main([
            getattr(object, '__file__') for object in (importing, testing, reuse)
        ] + '-p no:pytest-importnb'.split())
```


# Run the benchmark tests
    
    import pytest
    if __name__ == '__main__':
        pytest.main([
            getattr(object, '__file__') for object in (importing, testing, reuse)
        ] + '-p no:pytest-importnb'.split())


    ============================= test session starts ==============================
    platform darwin -- Python 3.6.3, pytest-3.5.0, py-1.5.3, pluggy-0.6.0
    benchmark: 3.1.1 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
    rootdir: /Users/tonyfast/ahypothesis, inifile:
    plugins: cov-2.5.1, benchmark-3.1.1, hypothesis-3.56.5, nostalgiaforever-0.0.2
    collected 7 items
    
    importing.ipynb ..                                                       [ 28%]
    testing.ipynb ..                                                         [ 57%]
    reuse.ipynb ...                                                          [100%]
    
    
    ------------------------------------------------------------------------------------------------ benchmark: 2 tests -----------------------------------------------------------------------------------------------
    Name (time in ns)             Min                     Max                   Mean                StdDev                 Median                   IQR            Outliers  OPS (Kops/s)            Rounds  Iterations
    -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    test_jit                 403.0007 (1.0)        2,412.9986 (1.0)         674.8746 (1.0)        703.2401 (1.0)         418.0001 (1.0)         59.5010 (1.0)           1;1    1,481.7567 (1.0)           8           1
    test_py               24,781.0021 (61.49)    163,378.9980 (67.71)    28,165.2838 (41.73)    5,013.0852 (7.13)     27,169.0005 (65.00)    1,802.7504 (30.30)     691;908       35.5047 (0.02)      10831           1
    -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    Legend:
      Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
      OPS: Operations Per Second, computed as 1 / Mean
    =============================== warnings summary ===============================
    None
      Module already imported so cannot be rewritten: pytest_cov
      Module already imported so cannot be rewritten: pytest_benchmark
      Module already imported so cannot be rewritten: hypothesis
      Module already imported so cannot be rewritten: nostalgiaforever
    
    -- Docs: http://doc.pytest.org/en/latest/warnings.html
    ===================== 7 passed, 4 warnings in 2.12 seconds =====================



```python
# `hypothesis` has the best API in all of Python

    from hypothesis import given, assume, infer, HealthCheck, settings #


    
    @given(a=infer)
    @settings(suppress_health_check=[HealthCheck.return_value])
    def test_all_the_strings(a:str):
        """hypothesis will infer a strategy to test many strings!
        
        Use type annotations and 🏆🏆🏆🏆🏆!
        """
#         print(a)
#         assert a
        return a

    if __name__ == '__main__':
        test_all_the_strings()
```


# `hypothesis` has the best API in all of Python

    from hypothesis import given, assume, infer, HealthCheck, settings #


    
    @given(a=infer)
    @settings(suppress_health_check=[HealthCheck.return_value])
    def test_all_the_strings(a:str):
        """hypothesis will infer a strategy to test many strings!
        
        Use type annotations and 🏆🏆🏆🏆🏆!
        """
#         print(a)
#         assert a
        return a

    if __name__ == '__main__':
        test_all_the_strings()



```python
# Continuous Integration with [Travis](https://travis-ci.org/deathbeds/nostalgiaforever)

[![Build Status](https://travis-ci.org/deathbeds/nostalgiaforever.svg?branch=master)](https://travis-ci.org/deathbeds/nostalgiaforever)


`nostalgiaforever` using [Travis deployments](https://github.com/travis-ci/dpl) to simplify automated tasks

    
* `travis setup pypi`

[![PyPI version](https://badge.fury.io/py/nostalgiaforever.svg)](https://badge.fury.io/py/nostalgiaforever)
    
* [`travis setup pages`](https://deathbeds.github.io/nostalgiaforever/) (_This doesn't work right_)


    
    
```


# Continuous Integration with [Travis](https://travis-ci.org/deathbeds/nostalgiaforever)

[![Build Status](https://travis-ci.org/deathbeds/nostalgiaforever.svg?branch=master)](https://travis-ci.org/deathbeds/nostalgiaforever)


`nostalgiaforever` using [Travis deployments](https://github.com/travis-ci/dpl) to simplify automated tasks

    
* `travis setup pypi`

[![PyPI version](https://badge.fury.io/py/nostalgiaforever.svg)](https://badge.fury.io/py/nostalgiaforever)
    
* [`travis setup pages`](https://deathbeds.github.io/nostalgiaforever/) (_This doesn't work right_)


    
    



```python
<hr/><hr/><hr/><hr/><hr/>


# Summary [clear all output then "Run All" -- or it didn't happen]

* If a notebooks restart and run all then they may provide a foundation to build better software.
* tests can be designed incrementally across notebooks and aggregated.
* Others can and should use your shit.

* # Reuse ~~rewrite~~ the code you write in notebooks
```


<hr/><hr/><hr/><hr/><hr/>


# Summary [clear all output then "Run All" -- or it didn't happen]

* If a notebooks restart and run all then they may provide a foundation to build better software.
* tests can be designed incrementally across notebooks and aggregated.
* Others can and should use your shit.

* # Reuse ~~rewrite~~ the code you write in notebooks

