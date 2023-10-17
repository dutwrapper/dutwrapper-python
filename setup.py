from setuptools import find_packages, setup

setup(
    name='dutwrapper',
    version='1.7.0',
    author='ZoeMeow',
    author_email='ZoeMeow1027@outlook.com',
    url='https://github.com/ZoeMeow1027/dutwrapper',
    description='This library provides wrapper (for this repository - crawl data from a page) for access for some features in Da Nang University of Technology student page.',
    # list folders, not files
    packages=find_packages(),
    install_requires=['beautifulsoup4', 'certifi', 'charset-normalizer', 'idna', 'lxml', 'requests', 'soupsieve', 'urllib3'],
)