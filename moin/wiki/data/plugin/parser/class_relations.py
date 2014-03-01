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
            _eq   = relns.get("equals", [])

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

            all_classes = [ c["class"] for c in (_in + contains + _eq) ]
            all_classes.append(me)

            output = """
            <table class='inclusions'>
                <tr><th>Contained In</th><td>%s</td></tr>
                <tr><th>Equals</th><td>%s</td></tr>
                <tr><th>Contains</th><td>%s</td></tr>
            </table>

            <p>
                <a href='ViewClassRelations?action=class_relation_search&class_names=%s'>View as graph</a>
            </p>
            """ % (str_in, str_eq, str_contains, ','.join(all_classes))

        except Exception as e:
            print(e)
            import traceback
            traceback.print_exc()
            output = "<b>Error processing inclusions.</b>"

        self.out.write(formatter.rawHTML(output))
