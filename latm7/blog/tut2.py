import os, os.path
import random
import string

import cherrypy
cherrypy.server.socket_host = '0.0.0.0'
cherrypy.config.update({'server.socket_port': 13004})

class StringGenerator(object):
    @cherrypy.expose
    def hello(self):
        return "Hello world!"

    @cherrypy.expose
    def generate(self, length):
        some_string = ''.join(random.sample(string.hexdigits, int(length)))
	cherrypy.session['mystring'] = some_string
	return some_string

    @cherrypy.expose
    def display(self):
	return cherrypy.session['mystring']

    @cherrypy.expose
    def index(self):
	return file('index.html')

if __name__ == '__main__':
    conf = {
	'/': {
		'tools.sessions.on': True,
		'tools.staticdir.root': os.path.abspath(os.getcwd())
	},
	'/static': {
             'tools.staticdir.on': True,
             'tools.staticdir.dir': './public_html'
         }
    }
    cherrypy.quickstart(StringGenerator(), '/', conf)
