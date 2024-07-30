from setuptools import find_packages, setup

setup(
    name='dutwrapper',
    version='1.8.0',
    author='ZoeMeow',
    author_email='ZoeMeow1027@outlook.com',
    url='https://github.com/dutwrapper/dutwrapper-python',
    description='An unofficial wrapper for easier to use at sv.dut.udn.vn - Da Nang University of Technology student page.',
    # list folders, not files
    packages=find_packages(),
    install_requires=['beautifulsoup4', 'certifi', 'charset-normalizer', 'idna', 'lxml', 'requests', 'soupsieve', 'urllib3'],
)