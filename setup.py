import pathlib

from setuptools import setup

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name="pydatabase",
    version="0.1",
    description="A tool for easily manage databases with Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="DanialAasari",
    author_email="mahanaasary54@gmail.com",
    url="https://github.com/Itzhep/Py-Database",
    keywords="database sqlite python-database python-sqlite database-management",
    project_urls={
        "Bug Tracker": "https://github.com/Itzhep/Py-Database/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    packages=['os', 'threading', 'pickle'],
)