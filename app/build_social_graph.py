import py2neo
from py2neo import Graph, Node, Relationship, neo4j

graph = Graph()

import json

people = open("people.json").read()

data = json.loads(people)

# check if exists -> then if not create
try:
    graph.schema.create_uniqueness_constraint("Person", "name")
except Exception as e:
    pass


def graph_person(person):
    """
    person = Node(
        "Person", name=person.get('name'), gender=person.get('gender'),
        company=person.get('company'))
    """
    # person.push()
    # graph.merge_one(person)
    # neo-4j limitation

    return graph.merge_one("Person", "name", person.get('name'))


def create_relationships_friends(person):

    friend_one = graph.merge_one("Person", "name", person.get('name'))

    for friend in person.get('friends'):
        friend_two = graph.merge_one("Person", "name", friend.get('name'))

        rel = Relationship(friend_one, "FRIENDS_WITH", friend_two)
        # wrong! 
        # at least 3 rels? - shit
        return graph.create_unique(rel)


def create_relationships_tags(person):
    pass


if __name__ == "__main__":

    for person in data:
        print person.get('id'), person.get('gender')

        try:
            create_relationships_friends(person)

        except Exception as f:
            print f