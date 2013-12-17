from django.db import models

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
