from .http_client import HttpClient

# Assign all the api classes
from .api.verifications import Verifications
from .api.questions import Questions

class Client():

	def __init__(self, auth = {}, options = {}):
		self.http_client = HttpClient(auth, options)

	# Returns user api instance
	#
	def verifications(self):
		return Verifications(self.http_client)

	# 
	#
	def questions(self):
		return Questions(self.http_client)

