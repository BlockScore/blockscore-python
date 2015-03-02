if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import blockscore
import unittest
import os, sys

class TestBlockscoreCompanies(unittest.TestCase):

    def setUp(self):
        try:
            self.client = blockscore.Client({'api_key': os.environ['BLOCKSCORE_API']})
        except KeyError:
            sys.stderr.write("To run tests, you must have a BLOCKSCORE_API environment variable with a test api key\n")
            sys.exit(2)

        self.test_company = {
            "entity_name": "BlockScore",
            "tax_id": "123410000",
            "incorp_date": "1980-08-25",
            "incorp_state": "DE",
            "incorp_country_code": "US",
            "incorp_type": "corporation",
            "dbas": "BitRemite",
            "registration_number": "123123123",
            "email": "test@example.com",
            "url": "https://blockscore.com",
            "phone_number": "6505555555",
            "ip_address": "67.160.8.182",
            "address": {
                "street1": "1 Infinite Loop",
                "street2": None,
                "city": "Cupertino",
                "state": "CA",
                "postal_code": "95014",
                "country_code": "US",
            }
        }

    def test_list_companies(self):
        response = self.client.companies.all()
        self.assertEqual(200, response.code)

        response = self.client.companies.all(count=2)
        self.assertEqual(200, response.code)

        response = self.client.companies.all(count=2, offset=2)
        self.assertEqual(200, response.code)

    def test_retrieve_company(self):
        response = self.client.companies.create(self.test_company)
        body = response.body

        response = self.client.companies.retrieve(body['id'])
        body = response.body

        self.assertEqual(200, response.code)
        self.assertEqual(self.test_company['entity_name'], body['entity_name'])

    def test_create_company(self):
        response = self.client.companies.create(self.test_company)
        self.assertEqual(201, response.code)

if __name__ == '__main__':
    unittest.main()

