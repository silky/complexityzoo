# -*- coding: iso-8859-1 -*-
#
from MoinMoin import wikiutil, search

Dependencies = ["pages"]


def search_box (macro):
    _ = macro._
    html = [
        u'<form method="get" action="%s">' % macro.request.href(macro.request.formatter.page.page_name),
        u'<div>',
        u'<input type="hidden" name="action" value="class_relation_search">',
        u'Class names: <input type="text" name="class_names" size="30" value=""> (<small>Exact</small>)',
        u'<br /> <input type="submit" value="Search" />',
        u'</div>',
        u'</form>',
    ]
    html = u'\n'.join(html)
    return macro.formatter.rawHTML(html)


def execute (macro, needle):
    request = macro.request
    _ = request.getText

    if not(needle):
        return search_box(macro)

