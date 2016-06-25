

from controllers import *

route = [
	(
		r"/",
		main.MainHandler
	),
	(
		r"auth/login",
		login.AuthHandler
	),
	(
		r"/auth/register",
		registerUser.registerHandler
	)

]