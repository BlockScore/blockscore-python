if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import blockscore
import unittest
import os, sys

class TestBlockscore(unittest.TestCase):

    def setUp(self):
        try:
            self.client = blockscore.Client({'api_key': os.environ['BLOCKSCORE_API']})
        except KeyError:
            sys.stderr.write("To run tests, you must have a BLOCKSCORE_API environment variable with a test api key\n")
            sys.exit(2)
        self.test_identity = ['us_citizen','1980-01-01',{'ssn': '0000'},{'first': 'john', 'last': 'doe'},{'street1': '1 Infinite Loop', 'city': 'Palo Alto', 'state': 'ca', 'postal_code': '94309', 'country': 'us'}]

    def test_create_verification(self):
        verif = self.client.verification.create(*self.test_identity)
        self.assertEqual(verif.body['date_of_birth'], self.test_identity[1])

    def test_retrieve_verification(self):
        verif = self.client.verification.create(*self.test_identity)
        verif_id = verif.body['id']
        verif2 = self.client.verification.retrieve(verif_id)
        self.assertEqual(verif.body, verif2.body)

    def test_list_verification(self):
        verif1 = self.client.verification.create(*self.test_identity)
        verif2 = self.client.verification.create(*self.test_identity)
        verif3 = self.client.verification.create(*self.test_identity)
        verif_list = self.client.verification.all(count=3)
        verif_list = verif_list.body
        self.assertTrue(len(verif_list) >= 3)
        verif_list2 = self.client.verification.all(count=3,offset=3)
        verif_list2 = verif_list2.body
        self.assertNotEqual(verif_list, verif_list2)



    def test_create_questions(self):
        verif = self.client.verification.create(*self.test_identity)
        verif = verif.body
        verif_id = verif['id']
        qset = self.client.question_set.create(verif_id)
        qset = qset.body
        self.assertEqual(qset['verification_id'],verif_id)

    def test_score_questions(self):
        verif = self.client.verification.create(*self.test_identity)
        verif = verif.body
        verif_id = verif['id']
        qset = self.client.question_set.create(verif_id)
        qset = qset.body
        qset_id = qset['id']
        score = self.client.question_set.score(verif_id, qset_id, [
            {'question_id':1, 'answer_id':1},
            {'question_id':2, 'answer_id':1},
            {'question_id':3, 'answer_id':1},
            {'question_id':4, 'answer_id':1},
            {'question_id':5, 'answer_id':1}
        ])
        score = score.body
        self.assertEqual(score['id'],qset_id)
        self.assertIsInstance(score['score'],float)



        # make sure the shuffled sequence does not lose any elements
        # random.shuffle(self.seq)
        # self.seq.sort()
        # self.assertEqual(self.seq, range(10))
        # self.assertEqual(1,1)

        # should raise an exception for an immutable sequence
        # self.assertRaises(TypeError, random.shuffle, (1,2,3))

    # def test_choice(self):
    #     element = random.choice(self.seq)
    #     self.assertTrue(element in self.seq)

    # def test_sample(self):
    #     with self.assertRaises(ValueError):
    #         random.sample(self.seq, 20)
    #     for element in random.sample(self.seq, 5):
    #         self.assertTrue(element in self.seq)

if __name__ == '__main__':
    unittest.main()