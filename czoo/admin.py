from django.contrib import admin
from czoo.models import *
# Register your models here.

admin.site.register(ComplexityClass)
admin.site.register(Inclusion)
admin.site.register(Tag)
admin.site.register(ComplexityClassToTag)


