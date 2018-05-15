from pathlib import Path
import setuptools

name = "nostalgiaforever"

__version__ = None

here = Path(__file__).parent

exec((here / name / "_version.py").read_text())

description =""""""
for info in ("readme.md", ):
    with (here/info).open('r') as file:
        description += file.read()
        description += "\n\n"


setup_args = dict(
    name=name,
    version=__version__,
    author="deathbeds",
    author_email="tony.fast@gmail.com",
    description="Import .ipynb files as modules in the system path.",
    long_description_content_type='text/markdown',
    long_description=description,
    url="https://github.com/deathbeds/nostalgiaforever",
    packages=['nostalgiaforever'],
    setup_requires=[
        'importnb',
        'pytest-runner',
        'wheel>=0.31.0',
        'twine>=1.11.0',
        'setuptools>=38.6.',
    ],
    include_package_data=True,
    license="BSD-3-Clause",
    install_requires=[
        'ipython',
        'watchdog',
        'pytest',
        'importnb',
        'pidgin',
        'numba',
    ],
   classifiers=(
    "Development Status :: 4 - Beta",
    "Framework :: IPython",
    "Framework :: Jupyter",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.6',),
)

setup_args.update(entry_points = {
        'pytest11': ['pytest-nostalgia = nostalgiaforever.plugin',],
})

if __name__ == "__main__":
    setuptools.setup(**setup_args)
