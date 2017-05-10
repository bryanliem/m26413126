import os, os.path
import random
import string
import MySQLdb

import cherrypy
cherrypy.server.socket_host = '0.0.0.0'
cherrypy.config.update({'server.socket_port': 13126})

def connect(thread_index): 
    # Create a connection and store it in the current thread 
    cherrypy.thread_data.db = MySQLdb.connect('localhost', 'root', '', 'blog') 
 
cherrypy.engine.subscribe('start_thread', connect)
 
class Root: 
    def index(self): 
        # Sample page that displays the number of records in "table" 
        # Open a cursor, using the DB connection for the current thread 
        c = cherrypy.thread_data.db.cursor() 
        c.execute('select * from tbl_news where visible = 0') 
        res = c.fetchall()
        data = "<a href = '"+str(cherrypy.url())+"'><button>Add</button></a>"
        data += "<table border='1'><tr><td>No</td><td>Judul</td><td>Berita</td><td>Tanggal</td><td>Tindakan</td></tr>"
        for row in res:
            judul = row[1]
            berita = row[2]
            data += "<tr><td>%d</td><td>%s</td><td>%s</td><td>%s</td><td><a href=''><button>Edit</button></a><a href=''><button>Delete</button></a></td></tr>" % (row[0],row[1],row[2],row[3])			
        data += "</table>"
        if res:
           return "<html><body>%s</body></html>" % (data) 
        c.close() 
        
    index.exposed = True 

cherrypy.quickstart(Root())
