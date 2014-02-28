""" Lamely converts the {{Reference ...}} section into something MoinMoin
likes.

Used in conjunction with a lot of sed, like so:

sed 's#<span .*>\[\(.*\)\]</span>#====== \1 ======#g' refs.mediawiki | sed "s#<i>\(.*\)</i>#\'\'\1\'\'#g" | sed 's#\[\(.*\) \(.*\)\]# [[\1|\2]]#g' | sed 's#^===== \(.*\) =====#== \1 ==#g' | python convert_scripts.py | xclip -i 

"""
import re
import sys
import io

everything = sys.stdin.read()

def doRep (m):
    thing = m.group(1)
    meh = thing.split("|")
    def gt (thing, lst):
        for item in lst:
            if item.startswith(thing):
                return item.split("=")[1].strip()
        return ""

    tag= gt("tag", meh)
    title =gt("title", meh)
    authors= gt("authors", meh)
    journal= gt("journal", meh)
    srcdetail   = gt("srcdetail", meh)

    result = "====== %s ======\n" % tag
    result += authors + ", " + title
    if journal:
        result += ", ''" + journal + "''"

    if srcdetail:
        result += ", " + srcdetail

    result += "."
    return result

replaced = re.sub(u"{{(.+?)}}", doRep, everything, flags=re.DOTALL)
print replaced
