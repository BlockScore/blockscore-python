from blockscore.http_client import HttpClient

# Assign all the api classes
from blockscore.api.people import People
from blockscore.api.question_set import QuestionSet
from blockscore.api.companies import Companies

class Client():

	def __init__(self, auth = {}, options = {}):
		self.http_client = HttpClient(auth, options)
		self.people = People(self.http_client)
		self.question_set = QuestionSet(self.http_client)
		self.companies = Companies(self.http_client)

