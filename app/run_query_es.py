import requests
import pprint

import json

pp = pprint.PrettyPrinter(indent=2)

people = open("people.json").read()

data = json.loads(people)

base_url = "http://localhost:9200/users/people/_search?%s=%s"


def full_text_search(search_value, search_by='name'):
	url = base_url % (search_by, search_value)
	response = requests.get(url)

	return response.text


"""
for person in data:
        print person.get('id'), person.get('gender')

        try:
            print full_text_search(person.get('name'))
        except Exception as f:
            print f
"""


if __name__ == "__main__":
    search_by = raw_input("Enter what to Search By: ")
    search_value = raw_input("Enter Search Value: ")

    print pp.pprint(full_text_search(search_value, search_by))