# -*- coding: iso-8859-1 -*-

import random, re

import urllib
from MoinMoin.Page import Page
from MoinMoin import wikiutil

Dependencies = ["time"]


def macro_ListClasses (macro):
    _ = macro.request.getText

    def classFilter (name):
        return (re.match("^Class", name) != None)

    pages = macro.request.rootpage.getPageList(filter=classFilter,
            return_objects=False)
    
    names = sorted( [ page_name.strip("Class_") for page_name in pages ] )


    def token (thing):
        if not(thing.isalpha()):
            return 'Symbols'
        return thing

    # Lame.
    last = None
    output = ""
    for name in names:
        tok = token(name[0])
        if tok != last:
            if last != None:
                output += "</ul>"

            output += "<h2>%(token)s</h2><a name='%(token)s'></a>" % {'token': tok }
            output += "<ul class='classes-list'>"
        last = tok

        output += "<li><a href='Class_%(url_name)s'>%(name)s</a></li>" % {"name": name,
                "url_name": urllib.quote_plus(name) } 
    output += "</ul>"

    return output
