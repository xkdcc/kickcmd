import setuptools
import sys

# import pdb

from setuptools.command.test import test as TestCommand

# pdb.set_trace()

class PyTest(TestCommand):
    description = "run pytest after in-place build"
    user_options = [
        ('pytest-args=', 'a', 'Arguments to pass to pytest')
        ]
  
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
    
    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        
        errno = pytest.main(self.pytest_args.split())
        sys.exit(errno)

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='kickcmd', 
     version='0.1',
     # You can use "scripts" to deliver any command line tool that happens to use python.
     # Example: https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html
     # For more details about "scripts": https://docs.python.org/3/distutils/setupscript.html#installing-scripts
     #  scripts=['file1-path', 'file2-path'] ,
     author="Brant Chen",
     author_email="brantchen2008@yahoo.com",
     description="A wrapper for calling external cmd/scripts",
     long_description=long_description,
     long_description_content_type="text/reStructuredText",
     url="https://github.com/xkdcc/kickcmd",
     packages=setuptools.find_packages(),

     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
    
     tests_require=['pytest'], # With tests_require, setup.py will install the packages if not installed yet.
     cmdclass = {'test': PyTest}, # This is to add "test" as our customized step into setup.py.
 )
