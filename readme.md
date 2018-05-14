
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

# A Notebook is a Hypothesis

|Section|Topic|Idiom|
|---|---|---|
| 1 | Informal Testing | [If a notebook is hypothesis then it tests something.](nostalgiaforever/informal.ipynb) |
| 2 | Formal Testing   | [If a notebook is a hypothesis then it can be tested.](nostalgiaforever/formal.ipynb) |
| 3 | Continuous Testing |  [If a notebook is a hypothesis then it will be tested.](nostalgiaforever/continuous.ipynb) |


## Before the talk

* Restart your machine
* Install the requirements
* Make sure a terminal is open a Python 3.6 environment @ ./nostalgiaforever/
* Start the watcher

        if True:
            !source activate p6 && pushd nostalgiaforever && watchmedo tricks tricks.yml
            
* Prepare the fonts.


```python
    %%file nostalgiaforever/tricks.yml
    tricks:
    - importnb.utils.watch.ModuleTrick:
        patterns: ['*.ipynb']
        shell_command: >
            ipython --profile pidgin -m ${watch_dest_path}  && echo '---'
```

    Overwriting nostalgiaforever/tricks.yml



```python
    from nbconvert.exporters.markdown import MarkdownExporter
    from nbconvert.preprocessors import Preprocessor
    class ReplaceLinks(Preprocessor):
        def preprocess_cell(self, cell, resources=None, **kwargs):
            if cell['cell_type'] == 'markdown':
                if isinstance(cell['source'], list): cell['source'] = ''.join(cell['source'])
                cell['source'] = cell['source'].replace('.ipynb', '.md')
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
                to.with_suffix('.md').write_text(MarkdownExporter(preprocess=[ReplaceLinks]).from_filename(path)[0])
```
