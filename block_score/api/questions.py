import json
# 
#
class Questions():

	def __init__(self, client):
		self.client = client

	# 
	# '/questions' POST
	#
	# verification_id - 
	def new(self, verification_id, options = {}):
		body = options['body'] if 'body' in options else {}
		body['verification_id'] = verification_id

		response = self.client.post('/questions', body, options)

		return response

	# 
	# '/questions/score' POST
	#
	# verification_id - 
	# question_set_id - 
	# answers - 
	def score(self, verification_id, question_set_id, answers, options = {}):
		body = options['body'] if 'body' in options else {}
		req_body = {
			'verification_id': verification_id,
			'question_set_id': question_set_id,
			'answers': answers
		}
		body = req_body#json.dumps(req_body)

		response = self.client.post('/questions/score', body, options)

		return response

