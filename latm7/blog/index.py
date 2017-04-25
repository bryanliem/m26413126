import cherrypy
cherrypy.server.socket_host = '0.0.0.0'
cherrypy.config.update({'server.socket_port': 13126})

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello World!"
    @cherrypy.expose
    def berita(self):
        return "Hello Berita!"

if __name__=='__main__':
    cherrypy.quickstart(HelloWorld())
