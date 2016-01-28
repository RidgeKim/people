Hi Ian,

Please complete the following challenge and submit your solution as a privately shared bitbucket git pull request, latest by Friday 29th Jan at 23:59:59. The bitbucket user to share to is jobrefunite.

In the attached (linked) (http://ge.tt/4qEol8Z/v/0?c) file have we a JSON string of user profiles. Each user profile has the following fields:

id
guid
picture
age
name
gender
company
phone
email
address
about
registered
tags
friends

Using this information:

1. Create a simple search engine that improves its results by learning from past user behaviour (previous search queries and profile views).

2. Create a ‘people you may know’ feature. Next to each recommended profile, indicate the reason for being selected.

### ES - rethinkDB river - rethinkDB, ES - (full text search)
### "tags (interests) and 42 mutual friends" - neo4j, graphQL, python

Evaluation criteria:

- Functionality
- Creativity
- Coding Standards
- Efficiency

* Provide clear instruction on reproducing your work
* Give a write-up on your design decisions
* This problem is open-ended: LET YOUR CREATIVITY GUIDE YOU

Regards,
Makenja


 curl -XPUT localhost:9200/_river/rethinkdb/_meta -d '{
   "type":"rethinkdb",
   "rethinkdb": {
     "databases": {"People": {"Users": {"backfill": true}}},
     "host": "localhost",
     "port": 28015
   }}'

java - 8
rethinkDB 1.2
ES - 1.4/ 1.3
python 2.7


### fix java - java 1.8 for -> /usr/lib/jdk1.7.0_45/bin/javac

### Why full text search with ES, RethinkDB
 - SOLR based backend
 - graphing with neo4j -> social graph only natural - 5 billion nodes
 - document database with an ES river plugin -> because it's JSON document
 - ease of manipulation


### Pulling data from RethinkDB with partial

SUCCESS_PARTIAL:2
13:17:51.233 [elasticsearch[Franz Kafka][rethinkdb_river][T#1]] DEBUG com.rethinkdb.RethinkDBConnection - running type: CONTINUE
token: 2
 
SUCCESS_PARTIAL:2
13:17:51.733 [elasticsearch[Franz Kafka][rethinkdb_river][T#1]] DEBUG com.rethinkdb.RethinkDBConnection - running type: CONTINUE
token: 2
 
SUCCESS_PARTIAL:2
13:17:52.234 [elasticsearch[Franz Kafka][rethinkdb_river][T#1]] DEBUG com.rethinkdb.RethinkDBConnection - running type: CONTINUE
token: 2
 
SUCCESS_PARTIAL:2
13:17:52.734 [elasticsearch[Franz Kafka][rethinkdb_river][T#1]] DEBUG com.rethinkdb.RethinkDBConnection - running type: CONTINUE
token: 2
 
SUCCESS_PARTIAL:2
13:17:53.235 [elasticsearch[Franz Kafka][rethinkdb_river][T#1]] DEBUG com.rethinkdb.RethinkDBConnection - running type: CONTINUE
token: 2
 
SUCCESS_PARTIAL:2
13:17:53.735 [elasticsearch[Franz Kafka][rethinkdb_river][T#1]] DEBUG com.rethinkdb.RethinkDBConnection - running type: CONTINUE
token: 2
 
SUCCESS_PARTIAL:2
13:17:54.236 [elasticsearch[Franz Kafka][rethinkdb_river][T#1]] DEBUG com.rethinkdb.RethinkDBConnection - running type: CONTINUE
token: 2


curl -XPUT localhost:9200/_river/rethinkdb/_meta -d '{
  "type": "rethinkdb",
  "rethinkdb": {
    "host": "localhost",
    "port": 28015,
    "auth_key": "",
    "databases": {
      "people": {
        "users": {
          "backfill": true,
          "index": "people",
          "type": "users",
        }
      }
    }
  }
}'


### With postman

GET http://localhost:9200/users/people/_search?q=max

GET http://localhost:9200/users/_search?about=et

GET http://localhost:9200/users/people/_search?name=Ian


#### then ES backfillls and constantly polls - with change feeds in rethinkDB this is faster and more efficient