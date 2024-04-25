[Cypher Cheat Sheet - Neo4j Documentation Cheat Sheet](https://neo4j.com/docs/cypher-cheat-sheet/current/)
```
[USE]
[MATCH [WHERE]]
[OPTIONAL MATCH [WHERE]]
[WITH [ORDER BY] [SKIP] [LIMIT] [WHERE]]
RETURN [ORDER BY] [SKIP] [LIMIT]
```

## MATCH
`MATCH` is similar to `SELECT` in SQL. 
- `MATCH(n)`: match all node
- `MATCH (n:Person)-[:KNOWS]->(m:Person)`: Match nodes and relationships involved in the relationship
- `MATCH (a:Person {name: 'Andy'})`: Similar to `WHERE`, find node by property
- `MATCH p1=(u1:User)-[:COMMENTED]->(c1:Comment)-[:COMMENTED_ON]-(q:Question)`: Relationship can be chained. User commented comment "c1" that is commented on question "q"

## WHERE
Same as SQL `WHERE`, acts as a filter.
- `WHERE n.property <> $value`
- `WHERE r:R1|R2`: OR relationship
- `MATCH (a:Person)-[r:KNOWS WHERE r.since < minYear]->(b:Person)`: relationship used as predicate in a `WHERE` clause.







