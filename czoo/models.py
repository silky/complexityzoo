from django.db import models

class ComplexityClass (models.Model):
    code          = models.CharField(max_length=256)
    html_code     = models.CharField(max_length=256)
    html_name     = models.CharField(max_length=512)
    date_added    = models.DateTimeField(auto_now_add=True)
    description   = models.TextField()
    notes         = models.TextField()
    deleted       = models.BooleanField(default=False)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__ (self):
        return self.code


class Inclusion (models.Model):
    cclass1    = models.ForeignKey(ComplexityClass, related_name="cclass1")
    cclass2    = models.ForeignKey(ComplexityClass, related_name="cclass2")

    relation   = models.CharField(max_length="30")
        # One of:
        #   - subseteq
        #   - subset
        #   - eq

    refs       = models.TextField()
    notes      = models.TextField()
    conditions = models.TextField()


class Tag (models.Model):
    tagname = models.CharField(max_length=256)


class ComplexityClassToTag (models.Model):
    cclass = models.ForeignKey(ComplexityClass)
    tag    = models.ForeignKey(Tag)
