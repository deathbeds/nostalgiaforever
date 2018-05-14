
# coding: utf-8

# # A Notebook is a Hypothesis
# 
# 1. __[If a notebook is a hypothesis then it tests something.](nostalgiaforever/informal.ipynb)__
# 2. ~~[If a notebook is a hypothesis then it can be formally tested.](nostalgiaforever/formal.ipynb)~~
# 3. ~~[If a notebook is a hypothesis then it will be tested.](nostalgiaforever/social.ipynb)~~
# 
# [![Data Driven Journalism](https://camo.githubusercontent.com/a8d4be63da2f73339f35839d4c006f080b13104a/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f342f34382f446174615f64726976656e5f6a6f75726e616c69736d5f70726f636573732e6a7067)]()
# 
# > ### Science is rapidly becoming more relevent in popular culture & modern notebooks are having an impact.  POP CULTURE REFERENCES HERE

# In[1]:


__file__ = globals().get('__file__', 'informal.ipynb')
from IPython import get_ipython
try: 
    from .util import __ipython__
except: 
    if __name__ == '__main__':
        get_ipython().run_line_magic('reload_ext', 'pidgin')
        get_ipython().run_line_magic('pidgin', 'conventions markdown')

    from util import __ipython__

from graphviz import Source
interactive_computing = Source("""digraph {rankdir="LR" layout="fdp" 
         subgraph cluster_ic { label="Interactive Computing" subgraph cluster_human {label="human" read -> write}
             subgraph cluster_machine {label="machine" eval -> print}
             write -> eval; print -> read}}""")


# # __[If a notebook is a hypothesis then it tests something.](nostalgiaforever/informal.ipynb)__
# 
# * ### If something is a hypothesis then it can by tested.
# 
# * ### An interactive computing session that tests code or data the first time is the first test.
#     
# * ### _Informal_ testing does not explicitly test for errors while _formal_ testing does.

# In[2]:



from IPython.display import Markdown
notebook_session = Markdown("""# Lifecycle of a Notebook Session

A notebook session is semi-permanant.

---

1. $t_{0}$ - *setUp* and __init__ialize the Notebook 

    ~~Hope~~ Assume that your environment is set up.

2. $t_i$   - repeatedly __enter__ and __exit__ the _interactive computing_ session

    Lose your mind.

3. $t_{final}$ - tearDown the notebook session.

    Lose your memory.

4. # 😵😵😵😵"""); notebook_session


# In[3]:





interactive_computing


# In[4]:





# In[4]:


__import__('IPython').display.display(
            __import__('graphviz').Source('''
graph {rankdir="LR"; data--science--computing--data}''', format="png"))


# In[5]:





# In[5]:





# In[5]:


__import__('IPython').display.display(
            __import__('graphviz').Source('''
digraph {rankdir="RL"; subgraph clusterc{ label="literate computing"; data->"interactive computing" ->data -> "literate programming" ->data} {"interactive computing" "literate programming"} -> machines "literate programming" -> people {machines people} -> 🙉🙈🙊} ''', format="png"))


# In[6]:




from contextlib import contextmanager
@contextmanager
def theScientist(*independent_arguments, response=None, who: ['Human', 'Machine'] = 'Human', **experiment_settings):
    """A hypothesis requires an experimental design.
    """
    f"""Setup the experiment with {independent_arguments} and {experiment_settings}"""
    yield response
    f"""Clean up and communicate your results to {who}."""


# In[7]:





# In[7]:





# In[7]:





# In[7]:



nb_style = Markdown("""* ## focus on a concise "unit of thought"
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
"""); nb_style


# In[8]:



from pathlib import Path
from pidgin import markdown, conventions
from nbconvert.exporters.python import PythonExporter
from IPython.utils.capture import capture_output
from nbconvert.preprocessors.execute import ExecutePreprocessor


# In[9]:




exporter = PythonExporter(preprocessors=[markdown.Normalize(), conventions.Normalize(), ExecutePreprocessor()])    

if (
    __name__ == '__main__' 
    and Path(__file__).parts[-1].startswith('informal.')
):
    with capture_output():
        Path('informal_script.py').write_text(exporter.from_filename(__file__)[0])
        import informal_script
    assert informal_script, """The script was not created."""
    print('nbconvert is complete.')


# In[10]:








from importnb import Notebook, reload
get_ipython().run_line_magic('reload_ext', 'pidgin')
get_ipython().run_line_magic('pidgin', 'conventions markdown')
with Notebook():
    informal = reload(__import__('informal'))
    assert informal.__file__.endswith('.ipynb')


# ## Restart and run all as a watcher.
# 
#     watchmedo tricks tricks.yml
#     
# ...using [watchdog](https://github.com/gorakhargosh/watchdog)

# In[11]:




