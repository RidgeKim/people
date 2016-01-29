import os

import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError, RqlDriverError

RDB_HOST = os.environ.get('RDB_HOST') or 'localhost'
RDB_PORT = os.environ.get('RDB_PORT') or 28015

import json

people = open("people.json").read()

data = json.loads(people)

connection = r.connect(host=RDB_HOST, port=RDB_PORT)


def persist_to_rethink(person):

    # total_friends = 0
    # total_friends = total_friends + len(person.get('friends')) + 1

    try:
        r.db('people').table('users').insert(person).run(connection)
    except RqlDriverError:
        abort(503, "No database connection could be established.")


if __name__ == "__main__":

    for person in data:
        print person.get('id'), person.get('gender')

        try:
            persist_to_rethink(person)
            # graph_person(person)
            # create_relationships_friends(person)
            # print reccommend_friends(person.get('name'), limit=10)
        except Exception as f:
            print f