### Dependencies
- python-2.7
- jdk 8
- py2neo
- rethinkDB
- neo4j
- elasticsearch


### Install RethinkDB
- Install Instructions -> https://download.rethinkdb.com/
- version of rethinkDB must be below 2.2


### Install ElasticSearch 1.4
- version of ES must be 1.4 or 1.3 on java 8


### Install ES, rethinkDB river
- Install instructions -> https://github.com/rethinkdb/elasticsearch-river-rethinkdb (java 8)


### Install neo-4J - 2.1.5
- any version should work fine


### Setup ES, rethinkDB river plugin to pull chnage feeds from rethinkDB to ES

- index
curl -XPUT localhost:9200/_river/rethinkdb/_meta -d '{
   "type":"rethinkdb",
   "rethinkdb": {
     "databases": {"People": {"Users": {"backfill": true}}},
     "host": "localhost",
     "port": 28015
   }}'


### Pulling data from RethinkDB with partial

```bash SUCCESS_PARTIAL:2
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
```


```python curl -XPUT localhost:9200/_river/rethinkdb/_meta -d '{
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
}'```

### With postman - sample queries on ES

GET http://localhost:9200/users/people/_search?q=max

GET http://localhost:9200/users/_search?about=et

GET http://localhost:9200/users/people/_search?name=Ian


#### Then the river plugin backfills and constantly polls - with change feeds in rethinkDB this is faster and more efficient


### Running
- start neo4j - service neo4j-service start
- start rethinkDB - service rethinkdb start
- start elasticsearch - service elasticsearch start


```bash
$ python persist_to_rethink.py
$ python graph.py
$ python run_query_es.py
$ python get_mutual_friends.py
```
