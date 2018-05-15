---
---

<hr/><hr/><hr/><hr/><hr/>


# Hypotheses accumulate

> ### If a notebook is a hypothesis then it can be tested.

* Managing assumptions and hypotheses is a challenge for any scientist.  
* Redundancy is a hinderance to innovation.


```python
    
    __file__ = globals().get('__file__', 'importing.ipynb')
    from IPython import get_ipython
    from IPython.display import Markdown
    with __import__('importnb').Notebook():
        try: 
            from .util import __ipython__
        except: 
            from util import __ipython__
            if __ipython__:
                %reload_ext pidgin
                %pidgin conventions markdown 
```


```python
<hr/><hr/><hr/><hr/><hr/>

# Importing notebooks

[`importnb`](https://github.com/deathbeds/importnb/tree/master/src/importnb) is a tool to import notebooks as python modules.
    
<pre><code>
pip install importnb
conda install -c conda-forge importnb
</code></pre>
<br/>
    
> `importnb` learns from of [`ipynb`](https://github.com/ipython/ipynb) and [`contentmanagement`](https://github.com/jupyter-incubator/contentmanagement)
    
## This notebook - `importing.ipynb` - imports itself as module `importing`
    
    from importnb import Notebook, reload
    with Notebook():
        try:
            # The module scope
            from . import importing
        except:
            # The interactive computing scope
            import importing   
```


<hr/><hr/><hr/><hr/><hr/>

# Importing notebooks

[`importnb`](https://github.com/deathbeds/importnb/tree/master/src/importnb) is a tool to import notebooks as python modules.
    
<pre><code>
pip install importnb
conda install -c conda-forge importnb
</code></pre>
<br/>
    
> `importnb` learns from of [`ipynb`](https://github.com/ipython/ipynb) and [`contentmanagement`](https://github.com/jupyter-incubator/contentmanagement)
    
## This notebook - `importing.ipynb` - imports itself as module `importing`
    
    from importnb import Notebook, reload
    with Notebook():
        try:
            # The module scope
            from . import importing
        except:
            # The interactive computing scope
            import importing   



```python
Create a test function to prove that the source file is in fact an `ipynb` file.
    
    def test_importing():
        assert importing.__name__.endswith('importing')
        assert importing.__file__.endswith('.ipynb')
```


Create a test function to prove that the source file is in fact an `ipynb` file.
    
    def test_importing():
        assert importing.__name__.endswith('importing')
        assert importing.__file__.endswith('.ipynb')



```python
<hr/><hr/><hr/><hr/><hr/>

# Interactive computing context vs. a module context

The `__name__`s are different.  Notebooks create the API as a script before a module, the opposite of standard Python.

    if __name__ == "__main__":
        # This function only gets when running the notebook or the script.
        test_importing()
    
---
* More on [`__name__ == '__main__'`](https://docs.python.org/3/library/__main__.html)
```


<hr/><hr/><hr/><hr/><hr/>

# Interactive computing context vs. a module context

The `__name__`s are different.  Notebooks create the API as a script before a module, the opposite of standard Python.

    if __name__ == "__main__":
        # This function only gets when running the notebook or the script.
        test_importing()
    
---
* More on [`__name__ == '__main__'`](https://docs.python.org/3/library/__main__.html)


<hr/><hr/><hr/><hr/><hr/>

# Style guides for the notebook.

---

> ## What we learned about teaching with notebooks (in Oriole)
>> [Paco Nathan - Oriole: a new learning medium based on Jupyter + Docker](http://nbviewer.jupyter.org/github/jupyterday-atlanta-2016/oriole_jupyterday_atl/blob/master/oriole_talk.ipynb#What-we-learned-about-teaching-with-notebooks)

* ## focus on a concise "unit of thought"
* invest the time and editorial effort to create a good introduction
* keep your narrative simple and reasonably linear
* "chunk" both the text and the code into understandable parts
* alternate between text, code, output, further links, etc.
* leverage markdown by providing interesting links for background, deep-dive, etc.
* code cells should not be long, < 10 lines
* code cells must show that they've run, producing at least *some* output 
* load data from the container, not the network
* ## clear all output then "Run All" -- or it didn't happen
* video narratives: there's text, and there's subtext...
* pause after each "beat" -- smile, breathe, allow people to follow you


```python
<hr/><hr/><hr/><hr/><hr/>


# Summary [clear all output then "Run All" -- or it didn't happen]

If a notebook will restart and run all then it may be executed or imported as a module.
```


<hr/><hr/><hr/><hr/><hr/>


# Summary [clear all output then "Run All" -- or it didn't happen]

If a notebook will restart and run all then it may be executed or imported as a module.



```python
---

## Reloading the `importing` module

    foo = 42
    def test_reload():
        with Notebook(stdout=True, display=True):
            reload(importing)
        assert importing.foo == 42
    if __ipython__: test_reload()
```


---

## Reloading the `importing` module

    foo = 42
    def test_reload():
        with Notebook(stdout=True, display=True):
            reload(importing)
        assert importing.foo == 42
    if __ipython__: test_reload()



```python
---


## Executing the `importing` notebook script

<pre></code>importnb-install</code></pre>

Install the importnb extensions to the ipython profile.

    
    from IPython.utils.capture import capture_output
    if __ipython__ and __name__ == '__main__':
        with capture_output(stdout=False):
            !source activate p6 && ipython --profile pidgin -m importing
        ...
        
```


---


## Executing the `importing` notebook script

<pre></code>importnb-install</code></pre>

Install the importnb extensions to the ipython profile.

    
    from IPython.utils.capture import capture_output
    if __ipython__ and __name__ == '__main__':
        with capture_output(stdout=False):
            !source activate p6 && ipython --profile pidgin -m importing
        ...
        


    ]0;IPython: ahypothesis/nostalgiaforever

---

## Watching the notebook for changes

    source activate p6 && cd .. && watchmedo tricks tricks.yml

<hr/><hr/><hr/><hr/><hr/>

## Our notebook can be reused by a test suite.

    if __name__ == '__main__':
        import pytest
        try: pytest.main(args="importing.ipynb".split())
        except SystemExit: ...

1. [`readme.ipynb`](../readme.ipynb)
1. [`importing.ipynb`](importing.ipynb)
2. [`testing.ipynb`](testing.ipynb)
3. [`reuse.ipynb`](reuse.ipynb)
