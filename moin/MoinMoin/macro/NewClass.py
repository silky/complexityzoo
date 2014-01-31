# -*- coding: iso-8859-1 -*-


import random

from MoinMoin.Page import Page

Dependencies = ["time"]


def macro_NewClass(macro):
    _ = macro.request.getText

    return "Hello World, how are you?"
