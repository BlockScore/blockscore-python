#!/usr/bin/env python
if __name__ == '__main__' and __package__ is None:
  from os import sys, path
  sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import blockscore
import unittest
import os, sys
from unittest import skip
import time

class TestWatchlistAPI(unittest.TestCase):
  def setUp(self):
    try:
      self.client = blockscore.Client({'api_key': os.environ['BLOCKSCORE_API']})
    except KeyError:
      sys.stderr.write("To run tests, you must have a BLOCKSCORE_API environment variable with a test api key\n")
      sys.exit(2)

    self.test_identity = {
      'date_of_birth': '1980-01-01',
      'identification': {
        'ssn': '0000',
        'passport': '12315235'
      },
      'name': {
        'first': 'john',
        'middle': 'a',
        'last': 'doe'
      },
      'address': {
        'street1': '1 Infinite Loop',
        'street2': 'Floor 3',
        'city': 'Palo Alto',
        'state': 'ca',
        'postal_code': '94309',
        'country_code': 'us'
      },
      'note': 'test'
    }

  def test_create_body(self):
    body = self.client.watchlist._create_body(**self.test_identity)
    self.assertDictEqual({
      'ssn': self.test_identity['identification']['ssn'],
      'date_of_birth': self.test_identity['date_of_birth'],
      'passport': self.test_identity['identification']['passport'],
      'name_first': self.test_identity['name']['first'],
      'name_middle': self.test_identity['name']['middle'],
      'name_last': self.test_identity['name']['last'],
      'address_street1': self.test_identity['address']['street1'],
      'address_street2': self.test_identity['address']['street2'],
      'address_city': self.test_identity['address']['city'],
      'address_subdivision': self.test_identity['address']['state'],
      'address_postal_code': self.test_identity['address']['postal_code'],
      'address_country_code': self.test_identity['address']['country_code'],
      'note': self.test_identity['note']
    }, body)

  def test_create_candidate(self):
    candidate = self.client.watchlist.create(**self.test_identity)
    expected_body = self.client.watchlist._create_body(**self.test_identity)
    self.assertDictContainsSubset(expected_body, candidate.body)

  def test_edit_candidate(self):
    candidate_id = self.client.watchlist.create(**self.test_identity).body['id']
    candidate = self.client.watchlist.edit(candidate_id, date_of_birth='1980-01-02')
    self.test_identity['date_of_birth'] = '1980-01-02'
    expected_body = self.client.watchlist._create_body(**self.test_identity)
    expected_body['id'] = candidate_id
    self.assertDictContainsSubset(expected_body, candidate.body)

  def test_retrieve_candidate(self):
    candidate_id = self.client.watchlist.create(**self.test_identity).body['id']
    candidate = self.client.watchlist.retrieve(candidate_id)
    expected_body = self.client.watchlist._create_body(**self.test_identity)
    expected_body['id'] = candidate_id
    self.assertDictContainsSubset(expected_body, candidate.body)

  def test_delete_candidate(self):
    candidate_id = self.client.watchlist.create(**self.test_identity).body['id']
    candidate = self.client.watchlist.delete(candidate_id)
    expected_body = self.client.watchlist._create_body(**self.test_identity)
    expected_body['id'] = candidate_id
    expected_body['deleted'] = True
    self.assertDictContainsSubset(expected_body, candidate.body)

  @skip('These tests do not pass consistently because of eventual consistency of candidate list')
  def test_list_candidates_with_params(self):
    candidate = self.client.watchlist.create()
    candidate_list = self.client.watchlist.list(count=1)
    self.assertListEqual([candidate.body], candidate_list.body)
    self.client.watchlist.create()
    candidate_list = self.client.watchlist.list(count=1, offset=1)
    self.assertListEqual([candidate.body], candidate_list.body)

  #@skip('These tests do not pass consistently because of eventual consistency of candidate list')
  def test_list_candidates_all(self):
    candidate = self.client.watchlist.create(**self.test_identity)
    expected_body = self.client.watchlist._create_body(**self.test_identity)
    candidate_id = candidate.body['id']
    time.sleep(5)
    candidate_list = self.client.watchlist.list()
    match = {}
    for c in candidate_list.body['data']:
      if c[u'id'] == candidate_id:
        match = c
    self.assertDictContainsSubset(expected_body, match)

  def test_search(self):
    candidate_id = self.client.watchlist.create().body['id']
    response = self.client.watchlist.search(candidate_id)
    self.assertIn('searched_lists', response.body)
    self.assertIn('matches', response.body)
