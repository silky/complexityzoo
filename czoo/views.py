from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.template import Context, loader
from django.core.context_processors import csrf
from django.shortcuts import render_to_response as r

from czoo.models import *

def common_objects (c):
    categories = ['Symbols']
    for k in xrange(26):
        categories.append( chr(0x41 + k) )
    categories.append('All')

    c["categories"] = categories


def index (req):
    c = { "title": "Home" }
    common_objects(c)
    c.update(csrf(req))
    return r("index.html", c)


def view_category (req, category):
    c = { "title": category }
    common_objects(c)
    c.update(csrf(req))
    c["category"] = category
    #
    if category == 'All':
        classes = ComplexityClass.objects.all()
    else:
        classes = ComplexityClass.objects.filter(code__startswith=category)

    c["found"]   = len(classes)
    c["classes"] = classes
    return r("categories.html", c)


# TODO:
#   - Consider how to handle editing; want it to be wiki-like, but wany
#   formalism around:
#       - Inclusions
#       - ? Anything else?
#       - References?
#       - Can this be done with existing Wiki software easier?
#
# https://docs.djangoproject.com/en/1.6/intro/tutorial03/
# http://lightbird.net/dbe/todo_list.html
