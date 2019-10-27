import setuptools

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
 )
