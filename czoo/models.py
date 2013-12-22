import sys, datetime, re
from django.db import models
from django.utils.html import escape as djescape

class ComplexityClass (models.Model):
    code          = models.CharField(max_length=256, blank=True)
    html_code     = models.CharField(max_length=256, blank=True)
    html_name     = models.CharField(max_length=512, blank=True)
    date_added    = models.DateTimeField(auto_now_add=True)
    description   = models.TextField(blank=True)
    notes         = models.TextField(blank=True)
    deleted       = models.BooleanField(default=False)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__ (self):
        return self.html_code

    @property
    def notes_for_display (self):
        stuff = self.notes

        # Something lame with refs
        p = re.compile("\[([a-zA-Z0-9+]+)\]")
        stuff = p.sub("[<a href='#'>\\1</a>]", stuff)

        lines = stuff.splitlines()
        return "<br />".join(lines)


class Relation (models.Model):
        # One of:
        #   - subseteq
        #   - subset
        #   - eq
    name = models.CharField(max_length="30")

    def __unicode__ (self):
        return self.name


class Inclusion (models.Model):
    cclass1    = models.ForeignKey(ComplexityClass, related_name="cclass1")
    relation   = models.ForeignKey(Relation)
    cclass2    = models.ForeignKey(ComplexityClass, related_name="cclass2")

    refs       = models.TextField(blank=True)
    notes      = models.TextField(blank=True)
    conditions = models.TextField(blank=True)


    def __unicode__ (self):
        return "%s %s %s" % (unicode(self.cclass1), unicode(self.relation), 
                unicode(self.cclass2))


class Tag (models.Model):
    tagname = models.CharField(max_length=256)

    def __unicode__ (self):
        return self.tagname


class ComplexityClassToTag (models.Model):
    cclass = models.ForeignKey(ComplexityClass)
    tag    = models.ForeignKey(Tag)
