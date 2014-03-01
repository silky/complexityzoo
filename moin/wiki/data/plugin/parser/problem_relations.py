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

        if not self.raw.strip('\r\n '):
            return

        try:
            obj   = json.loads(self.raw)
            relns = obj["relations"]
            _in   = relns.get("contained_in", [])
            _comp = relns.get("complete_for", [])
            _hard = relns.get("hard_for", [])

            def maybeCondition (dct):
                if "condition" in dct:
                    return "\r\n\r\nIf %s" % dct["condition"]
                return ""
            
            def classesToLinks (classes):
                msg = "<ul>"
                msg += u"\r\n".join([ u'<li><a href="Class_%(class)s">%(class)s</a>  %(cond)s</li>' %
                    { "class": x["class"], "cond": maybeCondition(x) } for x in classes ])
                return msg

            str_in  = classesToLinks(_in)
            str_eq  = classesToLinks(_eq)


            output = """
            <table class='inclusions'>
                <tr><th>Complete For</th><td>%s</td></tr>
                <tr><th>Contained In</th><td>%s</td></tr>
                <tr><th>Hard For</th><td>%s</td></tr>
            </table>
            """ % (str_in, str_eq, str_contains)

        except Exception as e:
            print(e)
            import traceback
            traceback.print_exc()
            output = "<b>Error processing inclusions.</b>"

        self.out.write(formatter.rawHTML(output))
