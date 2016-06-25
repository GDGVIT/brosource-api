from modules import *
class MainHandler(RequestHandler):
	def get(self):
		jsonString = {'status' : 1, 'message' : 'API Working'}
		self.write(jsonString)