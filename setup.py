import os
from setuptools import setup

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name="fuzzy-synonym",
    version="0.0.1",
    author="Hagino Takahiro",
    author_email="haginota@gmail.com",
    description=("Automated Synonym Aggregation."),
    license="Apache Software License",
    keywords="synonym",
    url="https://github.com/haginot/fuzzy-synonym",
    packages=['fuzzy_synonym'],
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    install_requires=['numpy', 'pandas', 'ndjson'],
    classifiers=[]
)
