# Returns user api instance
#
class Verifications():

	def __init__(self, client):
		self.client = client

	# 
	# '/verifications' POST
	#
	# type - 
	# date_of_birth - 
	# identification - 
	# name - 
	# address - 
	def new(self, type, date_of_birth, identification, name, address, options = {}):
		body = options['body'] if 'body' in options else {}
		body['type'] = type
		body['date_of_birth'] = date_of_birth
		body['identification'] = identification
		body['name'] = name
		body['address'] = address

		response = self.client.post('/verifications', body, options)

		return response

	# 
	# '/verifications/:id' GET
	#
	# id - 
	def retrieve(self, id, options = {}):
		body = options['query'] if 'query' in options else {}
		
		response = self.client.get('/verifications/'+str(id), body, options)

		return response

	# 
	# '/verifications' GET
	#
	def list(self, count=None, offset=None, options = {}):
		body = options['query'] if 'query' in options else {}

		if count != None:
			body['count'] = count
		if offset != None:
			body['offset'] = offset

		response = self.client.get('/verifications', body, options)

		return response
