#!/usr/bin/python
# encoding = utf-8

import kickcmd.runcmd as kr
import pytest


def test_start():
    assert kr.demo("yo") == "pass"