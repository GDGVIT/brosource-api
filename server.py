'''
This file is only for application triggering
To add route go to routes/__init__.py
To add a new class controller go to controllers/{ create new file with a class }
To add frontend go to views/
'''

from tornado.web import RequestHandler, Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import os
from routes import *
from motor import MotorClient



db = MotorClient('mongodb://brsrc:brsrc@ds028559.mlab.com:28559/brosource')['brosource']
settings = dict(
		db=db,
		debug=True,
	)

#Application initialization

application = Application(route, **settings)


#main init
if __name__ == "__main__":
	server = HTTPServer(application)
	server.listen(8888)
	IOLoop.current().start()
