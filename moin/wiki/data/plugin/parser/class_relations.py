Dependencies = ['user']

import json
import os,re
from MoinMoin.Page import Page
from MoinMoin import wikiutil
from MoinMoin.action import AttachFile

class Parser:
    def __init__ (self, raw, request, **kw):
        self.raw = raw
        self.request = request

        self.out     = kw.get('out', request)
        attrs, msg   = wikiutil.parseAttributes(request, kw.get('format_args',''))


    def format (self, formatter):
        self.formatter = formatter

        try:
            obj = json.loads(self.raw)
            relns = obj["relations"]
            _in   = relns["contained_in"]
            _eq   = relns["equals"]
            # _cts  = relns["contains"]
            #
            
            def classesToLinks (classes):
                return u", ".join([ u'<a href="Class_%(class)s">%(class)s</a>' % x for x in classes ])

            str_in  = classesToLinks(_in)
            str_eq  = classesToLinks(_eq)
            # str_cts = ", ".join([ '<a href="Class_%(class)s">%(class)s</a>' % x
            #     for x in _cts ])

            str_contains = "TBA"

            # We have two ways of working this out (well, really one way.) We
            # need to go through every single page, load up the JSON, and
            # check to see if we are listed in their 'contained_in'.

            pages = self.request.rootpage.getPageList(
                    filter=wikiutil.classFilter,
                    return_objects=True)
            
            data = wikiutil.getRelationsAsDict(pages)

            # Hm.
            me   = self.request.page.page_name[len("Class_"):]

            contains = []
            for (k, v) in data.iteritems():
                if me == k: 
                    continue

                if "contained_in" in v["relations"] and \
                    me in [ d["class"] for d in v["relations"]["contained_in"] ]:
                    contains.append( {"class": k })

            str_contains = classesToLinks(contains)

            output = """
            <table class='inclusions'>
                <tr><th>Contained In</th><td>%s</td></tr>
                <tr><th>Equals</th><td>%s</td></tr>
                <tr><th>Contains</th><td>%s</td></tr>
            </table>
""" % (str_in, str_eq, str_contains)
        except Exception as e:
            # import pdb
            print(e)
            output = "<b>Error processing inclusions.</b>"

        self.out.write(formatter.rawHTML(output))
