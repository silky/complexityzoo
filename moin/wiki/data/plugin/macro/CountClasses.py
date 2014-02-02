# -*- coding: iso-8859-1 -*-

import random, re

from MoinMoin.Page import Page
from MoinMoin import wikiutil

Dependencies = ["time"]


def macro_CountClasses (macro):
    _ = macro.request.getText

    def classFilter (name):
        return (re.match("^Class", name) != None)

    # Return objects will be useful.
    pages = macro.request.rootpage.getPageList(filter=classFilter,
            return_objects=False)

    return len(pages)
