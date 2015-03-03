
QUESTION_SET_PATH = '/question_sets'

class QuestionSets():

  def __init__(self, client):
    self.client = client

  #
  # '/question_sets' POST
  #
  # verification_id -
  def create(self, person_id, options = {}):
    body = options['body'] if 'body' in options else {}
    body['person_id'] = person_id

    response = self.client.post(QUESTION_SET_PATH, body)
    return response

  #
  # '/question_sets/:id/:score' POST
  #
  # answers -
  def score(self, id, answers):
    body = {}
    body['answers'] = answers

    options = {}
    options['request_type'] = 'json'

    response = self.client.post('%s/%s/score' % (QUESTION_SET_PATH, str(id)), body, options)
    return response

  #
  # '/question_sets/:id' GET
  #
  # id -
  def retrieve(self, id):
    body = {}
    response = self.client.get('%s/%s' % (QUESTION_SET_PATH, str(id)), body)
    return response

  #
  # '/question_sets' GET
  #
  def all(self, count=None, offset=None, options = {}):
    body = options['body'] if 'body' in options else {}

    if count:
      body['count'] = count
    if offset:
      body['offset'] = offset

    response = self.client.get(QUESTION_SET_PATH, body)
    return response

