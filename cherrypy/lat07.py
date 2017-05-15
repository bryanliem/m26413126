import os, os.path
import cherrypy
import random
import string

cherrypy.server.socket_host = '0.0.0.0'
cherrypy.config.update('server.conf')

class StringGenerator(object):
    exposed = True
    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return cherrypy.session['mystring']

    def POST(self, length=8):
        some_string = ''.join(random.sample(string.hexdigits, int(length)))
        cherrypy.session['mystring'] = some_string
        return some_string

    def PUT(self, another_string):
        cherrypy.session['mystring'] = another_string

    def DELETE(self):
        cherrypy.session.pop('mystring', None)


if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator(),'/', 'app.conf')
