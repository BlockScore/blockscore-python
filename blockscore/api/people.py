# Returns user api instance

PEOPLE_PATH = '/people'

class People():

  def __init__(self, client):
    self.client = client

  #
  # '/people' POST
  #
  # date_of_birth -
  # identification -
  # name -
  # address -
  def create(self, options = {}):
    response = self.client.post(PEOPLE_PATH, options)
    return response

  #
  # '/people/:id' GET
  #
  # id -
  def retrieve(self, id, options = {}):
    body = options['query'] if 'query' in options else {}
    response = self.client.get('%s/%s' % (PEOPLE_PATH, str(id)), body)
    return response

  #
  # '/people' GET
  #
  def all(self, count=None, offset=None, options = {}):
    body = options['body'] if 'body' in options else {}

    if count != None:
      body['count'] = count
    if offset != None:
      body['offset'] = offset

    response = self.client.get(PEOPLE_PATH, body)
    return response

