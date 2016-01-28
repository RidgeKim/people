import os

import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError, RqlDriverError

import py2neo
from py2neo import Graph, Node, Relationship, neo4j

graph = Graph()

RDB_HOST = os.environ.get('RDB_HOST') or 'localhost'
RDB_PORT = os.environ.get('RDB_PORT') or 28015

import json

people = open("people.json").read()

data = json.loads(people)

connection = r.connect(host=RDB_HOST, port=RDB_PORT)

# check if exists -> then if not create
try:
    graph.schema.create_uniqueness_constraint("Person", "name")
except Exception as e:
    pass

# assuming email is unique


def full_text_search():
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


# Sophia Goldman
# Alexis Galbraith
def reccommend_friends(name, limit=5):
    """MATCH (person:Person)-[:FRIENDS_WITH]->(friend),
      (friend)-[:FRIENDS_WITH]->(friend_two:Person)

    WHERE person.name = "%s"
    RETURN friend_two.name, count(*) as mutual
    ORDER BY mutual DESC
    LIMIT %d""" % (name, limit)


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


def persist_to_rethink(person):

    # total_friends = 0
    # total_friends = total_friends + len(person.get('friends')) + 1

    try:
        r.db('people').table('users').insert(person).run(connection)
    except RqlDriverError:
        abort(503, "No database connection could be established.")

    # print total_friends


if __name__ == "__main__":
    for person in data:
        print person.get('id'), person.get('gender')

        # persist_to_rethink(person)

        try:
            graph_person(person)
            # create_relationships_friends(person)

        except py2neo.GraphError as e:
            print e
        except Exception as f:
            print f
