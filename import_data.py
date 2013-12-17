#!/usr/bin/env python
# coding: utf-8

import csv, codecs, cStringIO

from django.conf import settings
import dj_database_url
settings.configure(
    DATABASES = {
        'default': dj_database_url.config(default='postgres://cz:cz@localhost/czweb')
    }
)

from czoo.models import *


class UTF8Recoder:
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next().encode("utf-8")


class UnicodeReader:
    """
    A CSV reader which will iterate over lines in the CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)

    def next(self):
        row = self.reader.next()
        return [unicode(s, "utf-8") for s in row]

    def __iter__(self):
        return self


def go ():

    r = Relation(name = "subseteq")
    r.save()

    r = Relation(name = "subset")
    r.save()

    r = Relation(name = "eq")
    r.save()

    complexityClassesFile = "data/ComplexityClass.csv"
    with open(complexityClassesFile, "rb") as f:
        rdr = UnicodeReader(f)

        for row in rdr:
            code       = row[0]
            html_code  = row[1]
            html_name  = row[2]
            date_added = row[3]
            desc       = row[4]
            notes      = row[5]

            cc = ComplexityClass(
                    code        = code,
                    html_code   = html_code,
                    html_name   = html_name,
                    date_added  = date_added,
                    description = desc,
                    notes       = notes
                )
            cc.save()
#


if __name__ == "__main__":
    go()
