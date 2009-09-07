import re

def process_dollars(app, docname, source):
    r"""
    Replace dollar signs with backticks.

    More precisely, do a regular expression search.  Replace a plain
    dollar sign ($) by a backtick (`).  Replace an escaped dollar sign
    (\$) by a dollar sign ($).  Don't change a dollar sign preceded or
    followed by a backtick (`$ or $`), because of strings like
    "``$HOME``".  Don't make any changes on lines starting with
    spaces, because those are indented and hence part of a block of
    code or examples.

    This also doesn't replaces dollar signs enclosed in curly braces,
    to avoid nested math environments, such as ::

      $f(n) = 0 \text{ if $n$ is prime}$

    Thus the above line would get changed to

      `f(n) = 0 \text{ if $n$ is prime}`
    """
    s = "\n".join(source)
    if s.find("$") == -1:
        return
    # This searches for "$blah$" inside a pair of curly braces --
    # don't change these, since they're probably coming from a nested
    # math environment.  So for each match, search to the left of its
    # start and to the right of its end, but not in between.
    s = re.sub(r"({[^{}$]*\$[^{}$]*\$[^{}$]*})", "3", s)
    # matches $...$
    dollars = re.compile(r"(?<!\$)(?<!\\)\$([^\$]+?)\$")
    # regular expression for \$
    slashdollar = re.compile(r"\\\$")
    s = dollars.sub(r":math:`\1`", s)
    s = slashdollar.sub(r"$", s)
    # now save results in "source"
    source[:] = [s]

def setup(app):
    app.connect("source-read", process_dollars)
