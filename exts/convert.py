from textwrap import fill
import re
s = open("appendix.tex").read()
def repl1(obj):
    eq = obj.group(1)
    eq = eq.replace("\n", " ")
    eq = fill(eq, 100000)
    return "\n.. math::\n\n    %s\n" % eq
def repl6(obj):
    eq = obj.group(1)
    eq = eq.replace("\n", " ")
    eq = fill(eq, 100000)
    return "\n.. math::\n    :nowrap:\n\n    %s\n" % eq
def repl4(obj):
    eq = obj.group(1)
    label = obj.group(2)
    eq = eq.replace("\n", " ")
    eq = fill(eq, 100000)
    return "\n.. math::\n    :label:%s\n\n    %s\n" % (label, eq)
def repl2(obj):
    title = obj.group(1)
    return "%s\n%s\n" % (title, "="*len(title))
def repl3(obj):
    title = obj.group(1)
    return "%s\n%s\n" % (title, "-"*len(title))
s = re.sub("(?ms)\$\$(.+?)\$\$", repl1, s)
s = re.sub(r"(?ms)\\begin{equation\*}(.+?)\\end{equation\*}", repl1, s)
s = re.sub(r"(?ms)(\\begin{eqnarray\*}.+?\\end{eqnarray\*})", repl6, s)
s = re.sub(r"(?ms)\\begin{equation}(.+?)\\label{(.+?)}(\s+)\\end{equation}", repl4, s)
s = re.sub(r"\\chapter{(.+)}", repl2, s)
s = re.sub(r"\\section{(.+)}", repl3, s)
s = re.sub(r"(?ms)\\left\((\\mat{.+?})\\right\)", r"\1", s)
s = re.sub(r"\(\\ref{(.+?)}\)", r":eq:`\1`", s)
open("appendix.rst", "w").write(s)
