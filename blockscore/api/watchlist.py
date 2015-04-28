WATCHLIST_CANDIDATE_URI = '/candidates'
WATCHLIST_SEARCH_URI = '/watchlists'


class Watchlist():
  def __init__(self, client):
    self.client = client

  @staticmethod
  def _create_body(date_of_birth=None, identification=None,
           name=None, address=None, note=None):
    body = {
      'date_of_birth': date_of_birth,
      'note': note
    }
    if identification:
      body['ssn'] = identification.get('ssn')
      body['passport'] = identification.get('passport')
    if name:
      body['name_first'] = name.get('first')
      body['name_middle'] = name.get('middle')
      body['name_last'] = name.get('last')
    if address:
      body['address_street1'] = address.get('street1')
      body['address_street2'] = address.get('street2')
      body['address_city'] = address.get('city')
      body['address_subdivision'] = address.get('state')
      body['address_postal_code'] = address.get('postal_code')
      body['address_country_code'] = address.get('country_code')
    return body

  def create(self, **kwargs):
    body = self._create_body(**kwargs)
    return self.client.post(WATCHLIST_CANDIDATE_URI, body)

  def edit(self, watchlist_candidate_id, **kwargs):
    body = self._create_body(**kwargs)
    return self.client.patch("%s/%s" % (WATCHLIST_CANDIDATE_URI,
                      watchlist_candidate_id), body)

  def retrieve(self, watchlist_candidate_id):
    return self.client.get("%s/%s" % (WATCHLIST_CANDIDATE_URI,
                      watchlist_candidate_id))

  def delete(self, watchlist_candidate_id):
    return self.client.delete("%s/%s" % (WATCHLIST_CANDIDATE_URI,
                       watchlist_candidate_id))

  def list(self, count=None, offset=None):
    body = {
      'count': count,
      'offset': offset
    }
    return self.client.get(WATCHLIST_CANDIDATE_URI, body)

  def search(self, watchlist_candidate_id, match_type=None):
    body = {
      'candidate_id': watchlist_candidate_id,
      'match_type': match_type
    }
    return self.client.post(WATCHLIST_SEARCH_URI, body)
