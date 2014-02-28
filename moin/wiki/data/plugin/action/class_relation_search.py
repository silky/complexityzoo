import re, time

import json

from MoinMoin.Page import Page
from MoinMoin import wikiutil
from MoinMoin.web.utils import check_surge_protect

from parsedatetime.parsedatetime import Calendar

# HACK: Worst possible thing just to get a PoC done; can be cleaned up a bit later.

CSS = '''
path.link {
  fill: none;
  stroke: #eaeaea;
  stroke-width: 1.5px;
}

circle {
  fill: #ccc;
  stroke: #fff;
  stroke-width: 1.5px;
}

text {
  fill: #000;
  font: bold 12px sans-serif;
  pointer-events: none;
}

div.info { 
    display: none;
    width: 230px;
    float: left;
    color: black;
}
'''

#
# Could fix a node position in the following way; need the key thought.
#
#    // nodes[1].fixed = true;
#    // nodes[1].x = 200;
#    // nodes[1].y = 200;
#

JS = '''
var WIDTH = 600, HEIGHT = 500;

var lastInfoBox = null;

var drawD3Document = function(links) {
    var nodes = {};
    links.forEach(function(link) {
        link.source = nodes[link.source] || (nodes[link.source] = {
            label: link.source
        });
        link.target = nodes[link.target] || (nodes[link.target] = {
            label: link.target
        });
        link.value = +link.value;
    });

    var width = WIDTH, height = HEIGHT;
    var force = d3.layout
        .force()
        .nodes(d3.values(nodes))
        .links(links)
        .size([ width, height ])
        .linkDistance(50)
        .charge(-3000)
        .on("tick", tick);

    var svg = d3.select("#canvas")
        .append("svg")
            .attr("width", width)
            .attr("height", height);

    svg.append("svg:defs")
        .selectAll("marker")
        .data(["end"])
        .enter()
        .append("svg:marker")
            .attr("id", String)
            .attr("viewBox", "0 -5 10 10")
            .attr("refX", 25)
            .attr("refY", -1.5)
            .attr("markerWidth", 6)
            .attr("markerHeight", 6)
            .attr("orient", "auto")
            .append("svg:path")
                .attr("d", "M0,-5L10,0L0,5");

    var path = svg.append("svg:g")
        .selectAll("path")
        .data(force.links())
        .enter()
            .append("svg:path")
                .attr("class", "link")
                .attr("marker-end", "url(#end)");

    var node = svg.selectAll(".node")
        .data(force.nodes())
            .enter()
                .append("g")
                .attr("class", "node")
                .call(force.drag);

    node.append("circle")
        .attr("r", 10)
        .attr("label", function(d){ return d.label; });

    node.append("text")
        .attr("x", 12)
        .attr("dy", ".35em")
        .text(function(d) { return d.label; });

    node.selectAll("circle").on("mouseover", function () {
        var label = d3.select(this).attr("label");

        if (d3.select(lastInfoBox) != null)  {
            d3.select(lastInfoBox).style("display", "none");    
        }
        d3.select("#info" + label).style("display", "block");
        lastInfoBox = "#info" + label;
        });

    force.start();

    for (var i = 0; i < 100; ++i){
        force.tick();
    }

    force.stop();

    function tick () {
        path.attr("d", function(d) {
            var dx = d.target.x - d.source.x;
            var dy = d.target.y - d.source.y;
            var dr = Math.sqrt(dx * dx + dy * dy);
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
        lst.append( {"source": c2, "target": c1, "label": c2} )
    return json.dumps(lst)
#


def execute (pagename, request, fieldname='class_names'):
    _ = request.getText
    form = request.values

    needle = form.get(fieldname, '')
    class_names = form.get('class_names').split(',')

    pages  = [ Page(request, "Class_%s" % c.strip(' ')) for c in class_names ]
    pages  = [ p for p in pages if p.exists() ]
    graph  = wikiutil.getRelationsAsNxGraph(pages)

    uniqueClasses = list(set(graph.nodes()))
    allPages      = [ Page(request, "Class_%s" % uc) for uc in uniqueClasses ]

    d3list = json_for_d3(graph)

    info_divs = ""

    def pname (x):
        return x[len("Class_"):]

    for p in allPages:
        info_divs += '''<div class="info" id="info%(page_name)s">
    <h4>
        <a href='Class_%(page_name)s'>%(page_name)s</a>
    </h4>
    <hr />
    <b>Description</b>
    <p>
        %(desc)s
    </p>

    <b>Complete Problem</b>
    <p>
        %(prob)s
    </p>

</div>''' % {
        "page_name": pname(p.page_name),
        "desc":      wikiutil.getPageSection("description",      p.get_data()),
        "prob":      wikiutil.getPageSection("complete_problem", p.get_data()),
        }

    js_data = "DATA = %s;" % d3list
    html    = '''<h1>Inclusion graph</h1>
<small>Notation: An arrow from A to B means A is <em>contained in</em> B.</small>

<script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script>


<style type='text/css'>%(css)s</style>
<script type="text/javascript">
    %(js_data)s

    %(js)s
</script>

<br style='clear: both' />
<div id="canvas" width="600" height="800" background="white" style='float: left'></div>

%(divs)s

<script>
    drawD3Document(DATA);
</script>''' % { 'css': CSS, 'js': JS, 'divs': info_divs, 'js_data': js_data }

    # Then we 

    #
    # Alright, 
    #

    outputResults(request, pagename, html, needle)
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
