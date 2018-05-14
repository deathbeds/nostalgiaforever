from pathlib import Path
import setuptools

name = "nostalgiaforever"

__version__ = None

here = Path(__file__).parent

exec((here / name / "_version.py").read_text())

setup_args = dict(
    name=name,
    version=__version__,
    author="deathbeds",
    author_email="tony.fast@gmail.com",
    description="Import .ipynb files as modules in the system path.",
    long_description_content_type='text/markdown',
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
    install_requires=['pytest'],
)

setup_args.update(entry_points = {
        'pytest11': ['pytest-nostalgia = nostalgiaforever.plugin',],
})

if __name__ == "__main__":
    setuptools.setup(**setup_args)
