

from controllers import *

route = [
	(
		r"/",
		main.MainHandler
	),
	(
		r"/login",
		login.AuthHandler
	)
]