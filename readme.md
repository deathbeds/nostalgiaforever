
# A Notebook is a Hypothesis

Modern scientists are transitioning to a generation where notebooks are common currency. Consider how testing and documentation are crucial aspect of reusable open source software. Those best practices evolved to support the communities developing that software. Generations of open source established idioms and style guides which enable software collaboration at global scale. Now, access to reusable software is blending with modern science, where both disciplines share similar global ambitions to solve increasing complex, multi-objective problems. 

Consequently, notebooks have evolved past being a medium for personal insight to become assets for community innovation. They represent extra-personal objects for scientists who have evaluated procedural "units of thought" as computational narratives. In a way, a notebook represents a modern form of hypothesis, and scientists must get comfortable sharing them rapidly. Unfortunately, new authors lack conventions for sharing notebooks as hypotheses within a scientific community. This talk presents tactics from literate programming to create readable, reusable, and reproducible notebooks. These notebook authoring practices promote improved documentation and unit testing.

## Key Takeaways

* Notebook can be used as modules.
* The first test is the hardest to write.
* Notebooks can be used for testing and software.
* Existing testing frameworks can be used with notebooks.
* Reproducible notebooks can be used as modules.
* Styles guides
* You are your own contextmanager with garbage collection.


```python
    from IPython import get_ipython
```

# A Notebook is a Hypothesis

1. [If a notebook is hypothesis then it can be tested.](nostalgiaforever/informal.ipynb)
2. [If a notebook is a hypothesis then it can be formally tested.](nostalgiaforever/formal.ipynb)
3. [If a notebook is a hypothesis then it will be tested.](nostalgiaforever/automation.ipynb)

# Watcher

if True:

    !source activate p6 && pushd nostalgiaforever && watchmedo tricks tricks.yml

## Before the talk

* Restart your machine
* Install the requirements
* Make sure a terminal is open a Python 3.6 environment @ ./nostalgiaforever/
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
    if __name__ == '__main__':
        !jupyter nbconvert --to markdown readme.ipynb
```
