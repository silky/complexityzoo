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

            str_in  = ", ".join([ '<a href="Class_%(class)s">%(class)s</a>' % x
                for x in _in ])
            str_eq  = ", ".join([ '<a href="Class_%(class)s">%(class)s</a>' % x
                for x in _eq ])
            # str_cts = ", ".join([ '<a href="Class_%(class)s">%(class)s</a>' % x
            #     for x in _cts ])

            str_contains = "TBA"

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
