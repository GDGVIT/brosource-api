#import all modules
from modules import *

'''
Login Controller to return user details if user exists.
'''

class AuthHandler(RequestHandler):
	@coroutine
	@removeslash
	def get(self):
		username = self.get_argument('username')
		password = self.get_argument('password')
		password=hashingPassword(password)
		password=hashlib.sha256(password).hexdigest()
		result = yield db.users.find_one({'username': username, 'password': password})
		#Don't ever pass User password in any of the API.
		if(bool(result)):
			userData = {

			'username' 				: result['username'],
			'name'     				: result['name'],
			'certifications' 		: result['certifications'],
			'category' 				: result['category'],
			'ratings'  				: result['ratings'],
			'educational_details' 	: result['education_details'],
			'joined_on' 			: result['joined_on'],
			'signup' 				: result['signup'],
			'views' 				: result['views'],
			'photo_link' 			: result['photo_link'],
			'mobile'				: result['mobile'],
			'services' 				: result['services'],
			'about_me' 				: result['aboutme'],
			'address' 				: result['address'],
			'social_accounts' 		: result['social_accounts'],
			'skills' 				: result['skills'],
			'date_of_birth' 		: result['dob'],
			'email' 				: result['email'],
			'projects'  			: result['projects'],
			'id' 					: str(ObjectId(result['_id']))

			}
			self.write(userData)
		else:
			self.write({
				'status'		:0,
				'message' 		: 'Invalid username/password',
				'error_code' 	: 1
				})