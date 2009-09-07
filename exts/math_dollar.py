def convert_dollars(app, docname, source):
    print "-"
    print "so:"
    print app
    print docname
    print source
    print "-"

def setup(app):
    app.connect("source-read", convert_dollars)
