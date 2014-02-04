import re, time

import json

from MoinMoin.Page import Page
from MoinMoin import wikiutil
from MoinMoin.web.utils import check_surge_protect

from parsedatetime.parsedatetime import Calendar

CSS = '''
path.link {
  fill: none;
  stroke: #666;
  stroke-width: 1.5px;
}

circle {
  fill: #ccc;
  stroke: #fff;
  stroke-width: 1.5px;
}

text {
  fill: #000;
  font: 10px sans-serif;
  pointer-events: none;
}
'''

JS = '''
var WIDTH = 800, HEIGHT = 500;

var drawD3Document = function(links) {
    var nodes = {};
    links.forEach(function(link) {
        link.source = nodes[link.source] || (nodes[link.source] = {
            name: link.source
        });
        link.target = nodes[link.target] || (nodes[link.target] = {
            name: link.target
        });
        link.value = +link.value;
    });
    var width = WIDTH, height = HEIGHT;
    var force = d3.layout.force().nodes(d3.values(nodes)).links(links).size([ width, height ]).linkDistance(50).charge(-3000).on("tick", tick);
    nodes[4].fixed = true;
    nodes[4].x = 200;
    nodes[4].y = 200;
    var svg = d3.select("#canvas").append("svg").attr("width", width).attr("height", height);
    svg.append("svg:defs").selectAll("marker").data([ "end" ]).enter().append("svg:marker").attr("id", String).attr("viewBox", "0 -5 10 10").attr("refX", 15).attr("refY", -1.5).attr("markerWidth", 6).attr("markerHeight", 6).attr("orient", "auto").append("svg:path").attr("d", "M0,-5L10,0L0,5");
    var path = svg.append("svg:g").selectAll("path").data(force.links()).enter().append("svg:path").attr("class", "link").attr("marker-end", "url(#end)");
    var node = svg.selectAll(".node").data(force.nodes()).enter().append("g").attr("class", "node").call(force.drag);
    node.append("circle").attr("r", 5);
    node.append("text").attr("x", 12).attr("dy", ".35em").text(function(d) {
        return d.name;
    });
    force.start();
    for (var i = 0; i < 100; ++i) force.tick();
    force.stop();
    function tick() {
        path.attr("d", function(d) {
            var dx = d.target.x - d.source.x, dy = d.target.y - d.source.y, dr = Math.sqrt(dx * dx + dy * dy);
            return "M" + d.source.x + "," + d.source.y + "A" + dr + "," + dr + " 0 0,1 " + d.target.x + "," + d.target.y;
        });
        node.attr("transform", function(d) {
            return "translate(" + d.x + "," + d.y + ")";
        });
    }
};
'''


def json_for_d3 (graph):
    lst = []

    for (c1, c2) in graph.edges():
        lst.append( {"source": c1, "target": c2, "value": c1} )
    return json.dumps(lst)
#


def execute (pagename, request, fieldname='class_names'):
    _ = request.getText
    form = request.values

    needle = form.get(fieldname, '')
    class_names = form.get('class_names').split(',')

    pages = [ Page(request, "Class_%s" % c.strip(' ')) for c in class_names ]
    pages = [ p for p in pages if p.exists() ]

    graph = wikiutil.getRelationsAsNxGraph(pages)

    d3list = json_for_d3(graph)

    import pdb
    pdb.set_trace()

    # [
    #  { "source": "1",
    #    "target": "2",
    #    "value" : "3"
    #  }
    # ]

    #
    # Alright, 
    #

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
