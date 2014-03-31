# AuthHandler takes care of devising the auth type and using it
class AuthHandler():

	HTTP_PASSWORD = 0

	def __init__(self, auth):
		self.auth = auth

	# Calculating the Authentication Type
	def get_auth_type(self):

		if 'username' in self.auth and 'password' in self.auth:
			return self.HTTP_PASSWORD

		return -1

	def set(self, request):
		if len(self.auth.keys()) == 0:
			return request

		auth = self.get_auth_type()
		flag = False

		if auth == self.HTTP_PASSWORD:
			request = self.http_password(request)
			flag = True

		if not flag:
			raise StandardError("Unable to calculate authorization method. Please check")

		return request

	# Basic Authorization with username and password
	def http_password(self, request):
		request['auth'] = (self.auth['username'], self.auth['password'])
		return request

