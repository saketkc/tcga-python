import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "TCGA Python",
    version = "0.0.1",
    author = "Saket Choudhary",
    author_email = "saketkc@gmail.com",
    description = ("A python wrapper to query the  TCGA portal",
                   "https://wiki.nci.nih.gov/display/TCGA/TCGA+DCC+Web+Service+User%27s+Guide"),
    license = "GPLv3",
    keywords = "example documentation tutorial",
    url = "http://packages.python.org/tcga",
    packages=['TCGA', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    ],
)
