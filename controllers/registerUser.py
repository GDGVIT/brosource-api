#import all modules

from modules import *

class registerHandler(RequestHandler):
	@coroutine
	@removeslash
	def post(self):
		username = self.get_argument('username_signup')
		password = self.get_argument('password_signup')
		name = self.get_argument('name')
		email = self.get_argument('emailID')
		result = yield db.users.find_one({'username':username, 'email':email})
		
		if(bool(result)):
			self.write({
				'status' 		: 0,
				'message' 		: 'username/email already taken',
				'error_code' 	: 2
				})
		else:
			password=hashingPassword(password)
			password=hashlib.sha256(password).hexdigest()
			now=datetime.now()
			time=now.strftime("%d-%m-%Y %I:%M %p")
			result = yield db.users.insert({
				'photo_link' : '',
				'username' : username,
				 'password' : password,
				 'email' : email,
				 'name' : name,
				 'mobile' : '',
                 'address' : '',
                 'skills' : [],
                 'dob': '',
                 'category' : '',
                 'certifications' : [],
                 'education_details' : [],
                 'signup' : 0,
                 'aboutme' : '',
                 'ratings' : 0,
                 'projects' : [],
                 'views' : 0,
                 'services' : [],
                 'social_accounts' : {},
                 'joined_on' : time})
			self.write({
				'status' : 1,
				'message' : 'User registered successfully',

				})