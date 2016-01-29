import requests

import json

people = open("people.json").read()

data = json.loads(people)

base_url = "GET http://localhost:9200/users/people/_search?%s=%s"


def full_text_search(some_value, search_by='name'):
	url = base_url %(search_by, some_value)
	response = requests.get(url)

	return response.text


if __name__ == "__main__":

    for person in data:
        print person.get('id'), person.get('gender')

        try:
        	full_text_search(person.get('name'))

        except Exception as f:
            print f