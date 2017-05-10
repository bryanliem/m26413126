import cherrypy
cherrypy.server.socket_host = '0.0.0.0'
cherrypy.config.update({'server.socket_port': 13126})

	  
class HelloWorld(object):
    def index(self):
        return "Hello World!"
    index.exposed = True

cherrypy.quickstart(HelloWorld())
