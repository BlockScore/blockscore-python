from ..error import ClientError
from ..error.error import BlockscoreError, AuthorizationError, \
			InternalServerError, ValidationError, ParameterError, NotFoundError
from .response_handler import ResponseHandler

# ErrorHanlder takes care of selecting the error message from response body
class ErrorHandler():

	@staticmethod
	def check_error(response, *args, **kwargs):
		code = response.status_code
		typ = response.headers.get('content-type')

		# No error found
		if (200 <= code < 300):
			return

		body = ResponseHandler.get_body(response)
		message = ''
		error_type = None
		error_code = None
		param = None

		# If HTML, whole body is taken
		if isinstance(body, str):
			message = body

		# If JSON, a particular field is taken and used
		if typ.find('json') != -1 and isinstance(body, dict):

			if 'error' in body:
				error = body['error']

				message = error['message']
				error_type = error['type']

				if 'code' in error.keys():
					error_code = error['code']
				if 'param' in error.keys():
					param = error['param']

			else:
				message = 'Unable to select error message from json returned by request responsible for error'

		if message == '':
			message = 'Unable to understand the content type of response returned by request responsible for error'


		if code == 400:
			# Inputs could not be validated
			if param is not None:
				raise ValidationError(message, body, param, error_type, error_code)

			# Required parameter missing
			else:
				raise ParameterError(message, body, error_type)

		# Trying to access nonexistent endpoint
		elif code == 404:
			raise NotFoundError(message, body, error_type)

		# Error with an API Key
		elif code == 401:
			raise AuthorizationError(message, body, error_type)
		
		# Internal API Error
		elif code == 500:
			raise InternalServerError(message, body, error_type)
		
		# Generic BlockscoreError (fallback)
		else:
			raise BlockscoreError(message, body)


