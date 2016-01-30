### Running (at base dir)

```bash
$ python app/persist_to_rethink.py
$ python app/build_social_graph.py
$ python app/get_mutual_friends.py
$ python app/run_query_es.py
```

1. persist_to_rethink - to write the json documents to rethinkDB.
2. build_social_graph - to add nodes and create relationships, the social graph
3. get_mutual_frieds  - reccomend friends based on mutual friends, tags to demonstrate interests could have been used.
4. run_query_es       - ES query to perform full text search.


## Design Decisions

### Why RethinkDB

- It's a noSQL document data-store, I used this because it has no implicit schema definition. And also it provides json support, it's a built in type and one can run a query inserting a JSON document.
- noSQL with sql capabilities such as suport for joins
- ReQL with a better user experince and administration management.


### Why neo-4j

- A huge graph data-store that can support billions of nodes and relationships.
- Rock solid for mission critical applications
- Easier data modelling
- It has a huge community going for it
- High performance because of native storage
- High scalability


### Why ElasticSearch

- Support for full text search.
- available river plugins to pull data from various data stores to ES.
- Indexing and fast access to search data.


### Why rethinkDB - ES river

- To fetch data through rethinkDB change feeds, and adding this to ES for full text search.
- It's fast and polls the DB for changes, but can also support rethinkDB's change feeds feature.
- Ease of use
- Scalability