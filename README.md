# blockscore-python

This is the official library for Python clients of the BlockScore API. [Click here to read the full documentation](https://manage.blockscore.com/docs).

## Install

Via pip:

```sh
pip install blockscore
```

## Getting Started

### Initializing BlockScore

```python
import blockscore
client = blockscore.Client({'api_key':'Your API Key'})
```

## Verifications
    
### List all verifications

```python
verification_list = client.verification.all()
verification_list = verification_list.body
```

### List `5` verifications

```python
verification_list = client.verification.all(count=5)
verification_list = verification_list.body
```
    
### View a verification by ID

```python
verification = client.verification.retrieve(verification_id)
verification = verification.body
```

### Create a new verification

```python
verification = client.verification.create('us_citizen','1980-01-01',{'ssn': '0000'},{'first': 'john', 'last': 'doe'},{'street1': '1 Infinite Loop', 'city': 'Palo Alto', 'state': 'ca', 'postal_code': '94309', 'country': 'us'})
verification = verification.body
```

## Question Sets

### Create a new question set

```python
question_set = client.question_set.create(verification_id)
question_set = question_set.body
```

### Score a question set

```python
score = self.client.question_set.score(verif_id, qset_id, [
	{'question_id':1, 'answer_id':1},
	{'question_id':2, 'answer_id':1},
	{'question_id':3, 'answer_id':1},
	{'question_id':4, 'answer_id':1},
	{'question_id':5, 'answer_id':1}
])
score = score.body
```

## Contributing to BlockScore
 
* Check out the latest master to make sure the feature hasn't been implemented or the bug hasn't been fixed yet.
* Check out the issue tracker to make sure someone already hasn't requested it and/or contributed it.
* Fork the project.
* Start a feature/bugfix branch.
* Commit and push until you are happy with your contribution.
* Make sure to add tests for it. This is important so I don't break it in a future version unintentionally.

## Copyright

Copyright (c) 2014 BlockScore. See LICENSE.txt for
further details.
