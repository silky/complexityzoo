from MoinMoin.config import multiconfig, url_prefix_static
from wikiconfig import LocalConfig

class Config(LocalConfig):
    superuser = [u'noon']
    secrets = "bne08r57hgq93w48hvpai7rgv0pqw89ghvbliw3o576bf092384yvbpieruwoeruytwb54y"
    page_front_page = u'Home'

    # Allow xmlrpc.
    multiconfig.DefaultConfig.navi_bar = [
            u'Home',
            u'[[AllClasses|All classes]]', 
            # Recent changes is a little broken because I added so many
            # things.
            # u'[[RecentChanges|Recent Changes]]',
            u'[[FindPage|Find page]]',
            u'[[RandomPage|Random page]]',
            ]
    html_head = u"""
    <script type="text/x-mathjax-config">
                 MathJax.Hub.Config({
                    extensions: ["tex2jax.js"],
                    jax: ["input/TeX", "output/HTML-CSS"],
                    tex2jax: {
                      inlineMath: [ ['$','$'] ],
                      displayMath: [ ['$$','$$'] ],
                      processEscapes: true
                    },
                    "HTML-CSS": { availableFonts: ["TeX"] }
                  });
        </script>
        <script type="text/javascript"
          src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
        </script>
    """
