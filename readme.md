
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/deathbeds/nostalgiaforever/master)

# A Notebook is a Hypothesis

Modern scientists are transitioning to a generation where notebooks are common currency. Consider how testing and documentation are crucial aspect of reusable open source software. Those best practices evolved to support the communities developing that software. Generations of open source established idioms and style guides which enable software collaboration at global scale. Now, access to reusable software is blending with modern science, where both disciplines share similar global ambitions to solve increasing complex, multi-objective problems.

Consequently, notebooks have evolved past being a medium for personal insight to become assets for community innovation. They represent extra-personal objects for scientists who have evaluated procedural "units of thought" as computational narratives. In a way, a notebook represents a modern form of hypothesis, and scientists must get comfortable sharing them rapidly. Unfortunately, new authors lack conventions for sharing notebooks as hypotheses within a scientific community. This talk presents tactics from literate programming to create readable, reusable, and reproducible notebooks. These notebook authoring practices promote improved documentation and unit testing.

## Key Takeaways

* Notebooks can be used for testing and software.
* Best practices for composing testable computational essays.
* Existing testing frameworks can be used with notebooks.



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
* Start the watcher

    source activate p6 && cd nostalgiaforever && watchmedo tricks tricks.yml
            
* Prepare the Fira Code fonts https://github.com/deathbeds/jupyterlab-fonts.
* Hey art nerd! Turn the color on!


```python
# Build the docs.
```


# Build the docs.



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
    [NbConvertApp] Writing 3847 bytes to readme.md
    readme.ipynb
    nostalgiaforever/importing.ipynb
    nostalgiaforever/plugin.ipynb
    nostalgiaforever/reuse.ipynb
    nostalgiaforever/testing.ipynb
    nostalgiaforever/util.ipynb
    test/test_nostalgia.ipynb



```python
# Run unit tests.
```


# Run unit tests.



```python
    if __name__ == '__main__':
        try:
            __import__('unittest').main('test', argv='--verbose'.split())
        except SystemExit: ...
```

    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.002s
    
    OK

