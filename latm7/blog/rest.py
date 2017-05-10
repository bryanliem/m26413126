import random
import string

import cherrypy
cherrypy.server.socket_host = '0.0.0.0'
cherrypy.config.update({'server.socket_port':13004})
class StringGenerator(object):
	@cherrypy.expose
	def index(self):
		return file('index.html')

class StringGeneratorWebService(object):
	exposed = True

	@cherrypy.tools.accept(media='text/plain')
	def GET(self):
		return cherrypy.session['mystring']

	def POST(self, length=8):
		some_string = ''.join(random.sample(string.hexdigits, int(length)))
		cherrypy.session['mystring']
		return some_string

	def PUT(self, another_string):
		cherrypy.session['mystring'] = another_string

	def DELETE(self, another_string):
		cherrypy.session.pop('mystring', None)

if __name__ == '__main__':
	conf = {
		'/':{
			'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
			'tools.sessions.on': True,
			'tools.response_headers.on': True,
			'tools.response_headers.headers': [('Content-Type', 'text/plain')],
		}
	}
	webapp = StringGenerator()
	webapp.generator = StringGeneratorWebService()
	cherrypy.quickstart(webapp, '/', conf)
