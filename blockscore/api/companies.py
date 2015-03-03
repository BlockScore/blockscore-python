# returns company api instance

COMPANIES_PATH = '/companies'

class Companies():

  def __init__(self, client):
    self.client = client

  #
  # '/companies' POST
  #
  def create(self, options = {}):
    return self.client.post(COMPANIES_PATH, options)

  #
  # '/companies/:id' GET
  #
  def retrieve(self, id, options = {}):
    body = options['query'] if 'query' in options else {}
    return self.client.get('%s/%s' % (COMPANIES_PATH, str(id)), body)

  #
  # '/companies' GET
  #
  def all(self, count = None, offset = None, options = {}):
    body = options['body'] if 'body' in options else {}

    if count:
      body['count'] = count
    if offset:
      body['offset'] = offset

    return self.client.get(COMPANIES_PATH, body)

