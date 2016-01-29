import py2neo
from py2neo import Graph, Node, Relationship, neo4j

import json

people = open("people.json").read()

data = json.loads(people)

graph = Graph()

# check if exists -> then if not create
try:
    graph.schema.create_uniqueness_constraint("Person", "name")
except Exception as e:
    pass


# Sophia Goldman
# Alexis Galbraith
def reccommend_friends(name, limit=5):
    query = """MATCH (person:Person)-[:FRIENDS_WITH]->(friend),
      (friend)-[:FRIENDS_WITH]->(friend_two:Person)

    WHERE person.name = "%s"
    RETURN friend_two.name as mutual_friend, count(*) as mutual
    ORDER BY mutual DESC
    LIMIT %d""" % (name, limit)

    return graph.cypher.execute(query)



if __name__ == "__main__":

    for person in data:
        print person.get('id'), person.get('gender')

        try:
            reccommend_friends(person.get('name'))

        except Exception as f:
            print f
