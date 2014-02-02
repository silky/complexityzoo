# coding: utf-8
import py

from MoinMoin import wikiutil

from MoinMoin.PageEditor import PageEditor
from MoinMoin.web.contexts import ScriptContext

pagename = 'Class_%23AC0'
req = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = editor.normalizeText('''= #AC<sup>0</sup> = 

The class of functions from {0,1}<sup>n</sup> to nonnegative integers computed by polynomial-size constant-depth arithmetic circuits, using addition and multiplication gates and the constants 0 and 1.

Contained in GapAC<sup>0</sup>.''')
_, rev, _ = editor.get_rev()
editor.saveText(text, rev)
