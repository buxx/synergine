from setuptools import setup, find_packages
import synergine

try:
    import pypandoc
    description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    print('pypandoc not found')
    description = open('README.md').read()

setup(
    name='synergine',
    version='0.0.1.8',
    packages=find_packages(),
    install_requires=[],
    author='Bastien Sevajol',
    author_email="synergine@bux.fr",
    description='Synergy simulation framework',
    long_description=description,
    include_package_data=True,
    url='https://github.com/buxx/synergine',
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers.
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)"
    ]
)