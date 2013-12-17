from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.template import Context, loader
from django.core.context_processors import csrf
from django.shortcuts import render_to_response as r

from czoo.models import *

def index (req):
    c = { "title": "Home" }
    c.update(csrf(req))
    return r("index.html", c)
