#!/usr/bin/python
# encoding = utf-8

def demo(name):
    print("Hello, {}, I am kickcmd package.".format(name))
    return "pass"


if __name__ == "main":
    demo("test")