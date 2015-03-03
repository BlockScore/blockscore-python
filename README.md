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

## People

### List all people

```python
people_list = client.people.all()
people_list = people_list.body
```

### List `5` people

```python
people_list = client.people.all(count=5)
people_list = people_list.body
```

### View a person by ID

```python
person = client.people.retrieve(person_id)
person = person.body
```

### Create a new person

```python
test_identity = {
            "name_first": "John",
            "name_middle": "Pearce",
            "name_last": "Doe",
            "birth_day": "23",
            "birth_month": "8",
            "birth_year": "1980",
            "document_type": "ssn",
            "document_value": "0000",
            "address_street1": "1 Infinite Loop",
            "address_street2": "Apt 6",
            "address_city": "Cupertino",
            "address_subdivision": "CA",
            "address_postal_code": "95014",
            "address_country_code": "US",
        }

person = client.people.create(test_identity)
person = person.body
```

## Question Sets

### Create a new question set

```python
question_set = client.question_sets.create(person_id)
question_set = question_set.body
```

### Score a question set

```python
score = self.client.question_sets.score(qset_id, [
	{'question_id':1, 'answer_id':1},
	{'question_id':2, 'answer_id':1},
	{'question_id':3, 'answer_id':1},
	{'question_id':4, 'answer_id':1},
	{'question_id':5, 'answer_id':1}
])
score = score.body
```

## Exceptions and Errors

### Error Description

* The generic error class is BlockscoreError. All other types of errors are derived from BlockscoreError.
* Errors contain information such as the HTTP response code, a short message describing the error, the type of error, and if applicable, the parameter and error code at issue.
* Also available in the error object is the full JSON text representation of the data.

### Error Types

* BlockscoreError (Generic error, base class)
* AuthenticationError (401 : Invalid API Key)
* ValidationError (400 : Input could not be validated)
* ParameterError (400 : Missing parameter)
* NotFoundError (404 : Attempting to reference nonexistent endpoint)
* InternalServerError (500 : Error on the Blockscore API)


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
