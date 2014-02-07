Dependencies = ['user']

import json
import os,re
from MoinMoin.Page import Page
from MoinMoin import wikiutil
from MoinMoin.action import AttachFile

from MoinMoin.parser.text_moin_wiki import Parser as WikiParser
from MoinMoin.formatter.text_html import Formatter as HtmlFormatter


class Parser:
    def __init__ (self, raw, request, **kw):
        self.raw = raw
        self.request = request
        self.moin_parser = WikiParser(raw, request, **kw)

        self.out     = kw.get('out', request)
        attrs, msg   = wikiutil.parseAttributes(request, kw.get('format_args',''))


    def format (self, formatter):
        self.formatter = formatter
        self.moin_parser.formatter = formatter

        parser = WikiParser(self.raw, self.request, line_anchors=False)
        formatter.startContent('')
        output = self.request.redirectedOutput(parser.format, formatter)
        formatter.endContent('')

        output = '<div class="complete_problem"><hr />%s<hr /></div>' % output
        self.out.write(output)
