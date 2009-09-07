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
    # Indices will be a list of pairs of positions in s, to search between.
    # If the following search has no matches, then indices will be (0, len(s)).
    indices = [0]
    # This searches for "$blah$" inside a pair of curly braces --
    # don't change these, since they're probably coming from a nested
    # math environment.  So for each match, search to the left of its
    # start and to the right of its end, but not in between.
    for m in re.finditer(r"{[^{}$]*\$([^{}$]*)\$[^{}$]*}", s):
        indices[-1] = (indices[-1], m.start())
        indices.append(m.end())
    indices[-1] = (indices[-1], len(s))

    # regular expression for $ (not \$, `$, $`, and only on a line
    # with no leading whitespace).
    dollar = re.compile(r"""^ # beginning of line
                            ([^\s] # non whitespace
                            .*?)? # non-greedy match any non-newline characters
                            (?<!`|\\)\$(?!`) # $ with negative lookbehind and lookahead
                            """, re.M | re.X)
    dollar2 = re.compile(r"""\$""")
    # regular expression for \$
    slashdollar = re.compile(r"\\\$")
    for start, end in indices:
        # find the first dollar:
        m1 = dollar.search(s, start, end)
        if m1:
            # and the second dollar:
            m2 = dollar2.search(s, m1.end(), end)
        else:
            m2 = None
        while m1 and m2:
            s = s[:m1.end()-1] + ":math:`" + s[m1.end():m2.end()-1] + "`" + \
                    s[m2.end():]
            m1 = dollar.search(s, start, end)
            if m1:
                m2 = dollar2.search(s, m1.end(), end)
            else:
                m2 = None
        while slashdollar.search(s, start, end):
            m = slashdollar.search(s, start, end)
            s = s[:m.start()] + "$" + s[m.end():]
    # now save results in "source"
    source[:] = [s]

def setup(app):
    app.connect("source-read", process_dollars)
