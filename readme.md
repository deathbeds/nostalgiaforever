
# A Notebook is a Hypothesis

Modern scientists are transitioning to a generation where notebooks are common currency. Consider how testing and documentation are crucial aspect of reusable open source software. Those best practices evolved to support the communities developing that software. Generations of open source established idioms and style guides which enable software collaboration at global scale. Now, access to reusable software is blending with modern science, where both disciplines share similar global ambitions to solve increasing complex, multi-objective problems.

Consequently, notebooks have evolved past being a medium for personal insight to become assets for community innovation. They represent extra-personal objects for scientists who have evaluated procedural "units of thought" as computational narratives. In a way, a notebook represents a modern form of hypothesis, and scientists must get comfortable sharing them rapidly. Unfortunately, new authors lack conventions for sharing notebooks as hypotheses within a scientific community. This talk presents tactics from literate programming to create readable, reusable, and reproducible notebooks. These notebook authoring practices promote improved documentation and unit testing.

## Key Takeaways

* Data and compute is modern research equipment.
* Style of creating reproducible and reusable interactive compute sessions.
* Best practices for composing testable computational essays.
* Existing testing frameworks can be used with notebooks.
* Notebooks can be used for testing and software.


```python
    from IPython import get_ipython
```

## Order

1. [`readme.ipynb`](readme.ipynb)
1. [`importing.ipynb`](nostalgiaforever/importing.ipynb)
2. [`testing.ipynb`](nostalgiaforever/testing.ipynb)
3. [`reuse.ipynb`](nostalgiaforever/reuse.ipynb)

## Before the talk

* Restart your machine
* Install the requirements
* Make sure a terminal is open a Python 3.6 environment @ ./nostalgiaforever/
* Start the watcher

        if True:
            !source activate p6 && pushd nostalgiaforever && watchmedo tricks tricks.yml
            
* Prepare the fonts.
* Hey art nerd! Turn the color on!


```python
    from nbconvert.exporters.markdown import MarkdownExporter
    from nbconvert.preprocessors import Preprocessor
    class ReplaceLinks(Preprocessor):
        def preprocess_cell(self, cell, resources=None, index=0):
            if cell['cell_type'] == 'markdown':
                if isinstance(cell['source'], list): 
                    cell['source'] = ''.join(cell['source'])
                cell['source'] = cell['source'].replace('.ipynb', '')
            return cell, resources
```


```python
    from pathlib import Path
    if __name__ == '__main__':
        !jupyter nbconvert --to markdown readme.ipynb
        for path in Path('.').rglob('*.ipynb'):
            if all(not part.startswith('.') for part in path.parts):
                to = ('docs' / path)
                print(path)
                to.parent.mkdir(exist_ok=True)
                MarkdownExporter(preprocessors=[ReplaceLinks()]).from_filename(path)[0]
                to.with_suffix('.md').write_text(
                    ("---\n"*2 if len(path.parts) > 1 else "") + MarkdownExporter(preprocess=[ReplaceLinks()]).from_filename(path)[0])
        
```

    [NbConvertApp] Converting notebook readme.ipynb to markdown
    [NbConvertApp] Writing 3367 bytes to readme.md
    readme.ipynb
    nostalgiaforever/continuous.ipynb
    nostalgiaforever/formal.ipynb
    nostalgiaforever/importing.ipynb
    nostalgiaforever/informal.ipynb
    nostalgiaforever/plugin.ipynb
    nostalgiaforever/reuse.ipynb
    nostalgiaforever/testing.ipynb
    nostalgiaforever/util.ipynb
    tests/test_nostalgia.ipynb
    [1m============================= test session starts ==============================[0m
    platform darwin -- Python 3.5.4, pytest-3.5.1, py-1.5.3, pluggy-0.6.0
    benchmark: 3.1.1 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
    rootdir: /Users/tonyfast/ahypothesis, inifile:
    plugins: ignore-flaky-0.1.1, cov-2.5.1, benchmark-3.1.1, importnb-0.2.6
    collected 0 items / 1 errors                                                   [0m
    
    ==================================== ERRORS ====================================
    _________________ ERROR collecting tests/test_nostalgia.ipynb __________________
    [31mImportError while importing test module '/Users/tonyfast/ahypothesis/tests/test_nostalgia.ipynb'.
    Hint: make sure your test modules/packages have valid Python names.
    Traceback:
    tests/__init__.py:1: in <module>
        from pidgin.markdown import load_ipython_extension
    E   ImportError: No module named 'pidgin'[0m
    !!!!!!!!!!!!!!!!!!! Interrupted: 1 errors during collection !!!!!!!!!!!!!!!!!!!!
    [31m[1m=========================== 1 error in 0.19 seconds ============================[0m



```python
    if __name__ == '__main__':
        try:
            __import__('unittest').main('test', argv='--verbose'.split())
        except SystemExit: ...
```


    if __name__ == '__main__':
        try:
            __import__('unittest').main('test', argv='--verbose'.split())
        except SystemExit: ...


    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.001s
    
    OK

