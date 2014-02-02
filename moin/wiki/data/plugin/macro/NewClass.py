# -*- coding: iso-8859-1 -*-

import random, re

from MoinMoin.Page import Page
from MoinMoin import wikiutil

Dependencies = ["time"]


def macro_NewClass(macro):
    _ = macro.request.getText

    def classFilter (name):
        cat = "CategoryDecisionProblems"
        page = Page(macro.request, name)

        if not (cat in page.getCategories(macro.request)):
            return False

        return (re.match("^Class", name) != None)

    def testPageFilter (name):
        return name == u'Test'

    # Return objects will be useful.
    pages = macro.request.rootpage.getPageList(filter=classFilter,
            return_objects=True)

    
    jsi   = [ wikiutil.getClassRelationJsonFromPage(p.get_data()) for p in pages ]
    names = [ p.page_name for p in pages ]

    # import pdb
    # pdb.set_trace()


    return "<br />".join(names)

    # import pdb
    # pdb.set_trace()

    # return "Hello World, how are you?"
