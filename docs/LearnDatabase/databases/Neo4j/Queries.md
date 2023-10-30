1. Display database schema
	1. Basically displaying all types of nodes and relationships between each type of node
	2. `CALL db.schema.visualization();`
2. Data import
	1. See the stackoverflow sample dataset for JSON import from url
	2. [Data Import - Developer Guides (neo4j.com)](https://neo4j.com/developer/data-import/)

## Basic Queries

### Find labels and their frequencies
Label is basically node name/type.
```
MATCH (n)
RETURN labels(n) as label, count(*) as freq
ORDER BY freq DESC;
```


### Find all relationship types and their frequencies
```
MATCH ()-[r]->()
RETURN type(r) as type, count(*) as freq
ORDER BY freq DESC;
```

`()-[r]->()` is used to express relationship. The middle term is relationship. 
Left and right of the relationship are both nodes. 
`(A)-[reads]->(B)` means A reads B. The relation is the same as the direction of the arrow.

### Sorting by Attribute Count
What are the most popular tags?
```
MATCH (q:Question)-[:TAGGED]->(t:Tag)
RETURN t.name, count(q) AS questions
ORDER BY questions DESC
LIMIT 5;
```
Find all question tags, and count question for each tag.

## Path Finding
Find all shortest paths between 2 users with whatever relationships in between.

```
MATCH path = allShortestPaths(
(u1:User {display_name:"alexanoid"})-[*]-(u2:User {display_name:"InverseFalcon"}))
RETURN path LIMIT 1;
```


## Reference
- [Cypher Cheat Sheet - Neo4j Documentation Cheat Sheet](https://neo4j.com/docs/cypher-cheat-sheet/current/)
- 

