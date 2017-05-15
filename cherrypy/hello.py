import cherrypy
cherrypy.server.socket_host = '0.0.0.0'
cherrypy.config.update('server.conf')

	  
class HelloWorld(object):
    def index(self):
        return "Hello World Class!"
    index.exposed = True

cherrypy.quickstart(HelloWorld())
