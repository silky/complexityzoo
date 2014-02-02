import re, time
from MoinMoin.Page import Page
from MoinMoin import wikiutil
from parsedatetime.parsedatetime import Calendar
from MoinMoin.web.utils import check_surge_protect


def execute (pagename, request, fieldname='class_names'):
    _ = request.getText
    form = request.values

    needle = form.get(fieldname, '')
    class_names = form.get('class_names').split(',')

    pages = [ Page(request, "Class_%s" % c.strip(' ')) for c in class_names ]
    pages = [ p for p in pages if p.exists() ]

    data = wikiutil.getRelationsAsDict(pages)

    outputResults(request, pagename, "%s" % len(pages), needle)
#


def outputResults (request, pagename, output, needle):
    # Need to regenerate everything ...
    request.setContentLanguage(request.lang)
    request.theme.send_title("Search: %s" % needle, pagename=pagename)
    request.write(request.formatter.startContent("content"))
    request.write(output)
    request.write(request.formatter.endContent())
    request.theme.send_footer(pagename)
    request.theme.send_closing_html()
#
