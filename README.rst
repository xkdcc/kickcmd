kickcmd
=======

.. image:: https://travis-ci.org/xkdcc/kickcmd.svg?branch=master
    :target: https://travis-ci.org/xkdcc/kickcmd
    
.. image:: https://codecov.io/gh/xkdcc/kickcmd/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/xkdcc/kickcmd


This repo is for me to learn:

1. How to create a Python pip package and test/use it
2. How to integrate pytest with Python pip setup.py and configure pytest (pytest.ini)
3. How to use Travis and integrate it with github repo, learn lifecyle of a Travis job
4. How to use codecov and integrate with Travis

How to test
------------
Support run test (pytest) from setup.py::

  python setup.py test -a "-vvv --tb=long"

