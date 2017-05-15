import cherrypy
import random
import string

cherrypy.server.socket_host = '0.0.0.0'
cherrypy.config.update('server.conf')

class StringGenerator(object):
   @cherrypy.expose
   def index(self):
       return "Good morning,class! from string generator"

   @cherrypy.expose
   def generate(self):
       return "".join(random.sample(string.hexdigits,int(length)))

if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())
