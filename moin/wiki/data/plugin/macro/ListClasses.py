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
            return_objects=True)
    
    def islatin (char):
        return not(not(re.match("[a-zA-Z]", char)))

    def token (char):
        if not(islatin(char)):
            return 'Symbols'

        return char.upper()

    def sorty (blob):
        (thing, _) = blob
        thing = thing.replace("Sharp", "#")
        if not thing:
            return -1

        if islatin(thing):
            return thing.lower()
        
        m = re.search("([a-zA-Z0-9])", thing)
        if not m:
            import pdb
            pdb.set_trace()

        return m.group(1)


    tuples = [ (p.page_name[len("Class_"):], wikiutil.getPageTitle(p)) for p in pages ]
    info   = sorted(tuples, key=sorty)

    last = None
    output = ""
    for (name, title) in info:
        disp_name = name.replace("Sharp", "#")
        if len(name) == 0:
            continue

        tok = token(disp_name[0])
        if tok != last:
            if last != None:
                output += "</ul>"

            output += "<h2>%(token)s</h2><a name='%(token)s'></a>" % {'token': tok }
            output += "<ul class='classes-list'>"
        last = tok

        output += "<li><a href='Class_%(url_name)s'>%(name)s</a> - %(title)s</li>" % {"name": disp_name,
                "url_name": urllib.quote(name.encode("utf-8")),
                "title": title } 
    output += "</ul>"

    return output
