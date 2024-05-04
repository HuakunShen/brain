# Neo4j GraphQL

- [Neo4j GraphQL](#neo4j-graphql)
  - [Neo4j GraphQL Toolbox](#neo4j-graphql-toolbox)
  - [GraphQL Directives](#graphql-directives)
    - [Basics](#basics)
    - [Autogeneration](#autogeneration)
      - [`@id`](#id)
      - [`@timestamp`](#timestamp)
      - [`@populatedBy`](#populatedby)
        - [Example (slug)](#example-slug)
        - [Example (modifiedBy)](#example-modifiedby)
    - [`@cypher`](#cypher)
      - [`this`](#this)
      - [`auth`](#auth)
      - [`cypherParams`](#cypherparams)
      - [`alias`](#alias)
    - [Indexes and Constraints](#indexes-and-constraints)
      - [`@unique`](#unique)
      - [`@fulltext`](#fulltext)
    - [Schema Configuration](#schema-configuration)
      - [Type Configuration](#type-configuration)
        - [`@query`](#query)
        - [`@mutation`](#mutation)
        - [`@subscription`](#subscription)
      - [Field Configuration](#field-configuration)
  - [Query and Aggregation](#query-and-aggregation)
    - [Aggregation](#aggregation)
  - [Filtering](#filtering)
  - [Sorting](#sorting)
  - [Pagination](#pagination)
  - [Authentication and Authorization](#authentication-and-authorization)
    - [Authorization without Authentication](#authorization-without-authentication)
  - [Excluded Directives OGM](#excluded-directives-ogm)
  - [Introspector](#introspector)
  - [Codegen](#codegen)


Neo4j supports GraphQL with NodeJS, making it possible to interact with the database like a OGM.

There is the most comprehensive docs I found: https://neo4j.com/docs/graphql/current/

https://www.npmjs.com/package/@neo4j/graphql-ogm is a GraphQL OGM for Neo4j GraphQL.

## Neo4j GraphQL Toolbox

https://graphql-toolbox.neo4j.io/

> The Neo4j GraphQL Toolbox is an onboarding, low-code tool that can be integrated to Neo4j. It was created for development and experimentation with Neo4j GraphQL APIs. With it, you can:

1. Connect to a Neo4j database with valid credentials.
2. Define (or introspect) the type definitions.
3. Build the Neo4j GraphQL schema.
4. Experiment, query, and play.

Enter your GraphQL schema in toolbox, it will generate the full API server for experiment.

You can use the generated Queries and Mutations with type prompts. No real server is required to run the generated API.

Build a local graphql apollo server, with GraphQL codegen library, you can generate TypeScript GraphQL Client code.

Include the operations you've experimented, then you can use the generated client code to interact with the database.

## GraphQL Directives

### Basics

Direction of relationship means the direction of the arrow in the graph. `IN` is the direction the arrow in pointing to.

An edge can also have properties defined in interface.

```graphql
type Movie {
  title: String
  actors: [Actor!]!
    @relationship(type: "ACTED_IN", direction: IN, properties: "ActedIn")
}

type Actor {
  name: String
  movies: [Movie!]!
    @relationship(type: "ACTED_IN", direction: OUT, properties: "ActedIn")
}

interface ActedIn @relationshipProperties {
  roles: [String]
}
```

### Autogeneration

https://neo4j.com/docs/graphql/current/type-definitions/directives/autogeneration/

#### `@id`

Autogeneration of IDs for the field.

```graphql
type User {
  id: ID! @id
  username: String!
}
```

#### `@timestamp`

```graphql
type User {
  createdAt: DateTime! @timestamp(operations: [CREATE])
  updatedAt: DateTime! @timestamp(operations: [UPDATE])

  lastModified: DateTime! @timestamp
  # OR (these 2 are equivalent)
  lastModified: DateTime! @timestamp(operations: [CREATE, UPDATE])
}
```

#### `@populatedBy`

specify a callback function that gets executed during GraphQL query parsing, to populate fields which have not been provided within the input.

##### Example (slug)

```graphql
type Product {
  name: String!
  slug: String! @populatedBy(callback: "slug", operations: [CREATE, UPDATE])
}
```

Pass callback function from client side.

```js
const slugCallback = async (root) => {
  return `${root.name}_slug`;
};

new Neo4jGraphQL({
  typeDefs,
  driver,
  features: {
    populatedBy: {
      callbacks: {
        slug: slugCallback,
      },
    },
  },
});
```

##### Example (modifiedBy)

Context values can be used in callback function.

```graphql
type Record {
    content: String!
    modifiedBy: @populatedBy(callback: "modifiedBy", operations: [CREATE, UPDATE])
}
```

```js
const modifiedByCallback = async (_parent, _args, context) => {
  return context.username;
};

new Neo4jGraphQL({
  typeDefs,
  driver,
  features: {
    populatedBy: {
      callbacks: {
        modifiedBy: modifiedByCallback,
      },
    },
  },
});
```

### `@cypher`

https://neo4j.com/docs/graphql/current/type-definitions/directives/cypher/

#### `this`

This value is a reference to the currently resolved node, and it can be used to traverse the graph.

```graphql
query {
  Movie {
    title
    actors: ACTED_IN @this {
      role
      actor {
        name
      }
    }
    directors: DIRECTED @this {
      director {
        name
      }
    }
  }
}
```

#### `auth`

This value is represented by the following TypeScript interface definition:

```ts
interface Auth {
  isAuthenticated: boolean;
  roles?: string[];
  jwt: any;
}
```

You can use the JWT in the request to return the value of the currently logged in User:

```graphql
type User {
  id: String
}

type Query {
  me: User
    @cypher(
      statement: """
      MATCH (user:User {id: $jwt.sub})
      RETURN user
      """
      columnName: "user"
    )
}
```

#### `cypherParams`

Inject values into cypher query from GraphQL context function.

Can be used to parse JWT token and inject user id into context.

```js
const server = new ApolloServer({
  typeDefs,
});

await startStandaloneServer(server, {
  context: async ({ req }) => {
    const userId = parseJwt(req.headers.authorization);
    return { cypherParams: { userId: userId } };
  },
});
```

```graphql
type Query {
  userPosts: [Post]
    @cypher(
      statement: """
      MATCH (:User {id: $userId})-[:POSTED]->(p:Post)
      RETURN p
      """
      columnName: "p"
    )
}
```

#### `alias`

maps a GraphQL field to a Neo4j property on a node or relationship

```graphql
type User {
  id: ID! @id @alias(property: "dbId")
  username: String!
}
```

### Indexes and Constraints

https://neo4j.com/docs/graphql/current/type-definitions/directives/indexes-and-constraints/

#### `@unique`

```graphql
type Colour {
  hexadecimal: String! @unique
}

type Colour {
  hexadecimal: String! @unique(constraintName: "unique_colour")
}
```

#### `@fulltext`

Use `@fulltext` directive to add a Full text index.

```graphql
type Product
  @fulltext(indexes: [{ indexName: "ProductName", fields: ["name"] }]) {
  name: String!
  color: Color! @relationship(type: "OF_COLOR", direction: OUT)
}
```

This `@fulltext` directive will create a full text index on the `name` field of the `Product` type.

```sql
CREATE FULLTEXT INDEX ProductName FOR (n:Product) ON EACH [n.name]
```

This will generate a new query

```graphql
type Query {
  productsFulltextProductName(
    phrase: String!
    where: ProductFulltextWhere
    sort: [ProductFulltextSort!]
    limit: Int
    offset: Int
  ): [ProductFulltextResult!]!
}

"""
The result of a fulltext search on an index of Product
"""
type ProductFulltextResult {
  score: Float
  product: Product
}

"""
The input for filtering a fulltext query on an index of Product
"""
input ProductFulltextWhere {
  score: FloatWhere
  product: ProductWhere
}

"""
The input for sorting a fulltext query on an index of Product
"""
input ProductFulltextSort {
  score: SortDirection
  product: ProductSort
}

"""
The input for filtering the score of a fulltext search
"""
input FloatWhere {
  min: Float
  max: Float
}
```

**Sample Usage**

```graphql
query {
  productsFulltextProductName(
    phrase: "Hot sauce"
    where: { score: { min: 1.1 } }
    sort: [{ product: { name: ASC } }]
  ) {
    score
    product {
      name
    }
  }
}
```

### Schema Configuration

#### Type Configuration

https://neo4j.com/docs/graphql/current/schema-configuration/type-configuration/

##### `@query`

This directive is used to limit the availability of query operations in the library.

```graphql
directive @query(
  read: Boolean! = true
  aggregate: Boolean! = false
) on OBJECT | SCHEMA
```

```graphql
type Movie @query(read: false, aggregate: true) {
  title: String
  length: Int
}
```

##### `@mutation`

> This directive is used to limit the availability of mutation operations in the library.

```graphql
enum MutationFields {
  CREATE
  UPDATE
  DELETE
}

directive @mutation(
  operations: [MutationFields!]! = [CREATE, UPDATE, DELETE]
) on OBJECT | SCHEMA

# Enable only CREATE mutation
type Movie @mutation(operations: [CREATE]) {
  title: String
  length: Int
}
```

##### `@subscription`

>

```graphql
enum SubscriptionFields {
  CREATE
  UPDATE
  DELETE
  CREATE_RELATIONSHIP
  DELETE_RELATIONSHIP
}

directive @subscription(
  operations: [SubscriptionFields!]! = [
    CREATE
    UPDATE
    DELETE
    CREATE_RELATIONSHIP
    DELETE_RELATIONSHIP
  ]
) on OBJECT | SCHEMA

# Enable only movieCreated subscription for Movie
type Movie @subscription(operations: [CREATE]) {
  title: String
  length: Int
}
```

#### Field Configuration

https://neo4j.com/docs/graphql/current/schema-configuration/field-configuration/#_selectable

- `@relationship`
- `@selectable`
  - This directive sets the availability of fields on queries and aggregations. It has two arguments:
  - `onRead`: if disabled, this field is not available on queries and subscriptions.
  - `onAggregate`: if disabled, aggregations is not available for this field.
- `@settable`
  - This directive sets the availability of the input field on creation and update mutations. It has two arguments:
  - `onCreate`: if disabled, this field is not available on creation operations.
  - `onUpdate`: if disabled, this field is not available on update operations.
- `@filterable`
  - This directive defines the filters generated for the field to which this directive is applied. It has two arguments:
  - `byValue`: if disabled, this field does not generate value filters.
  - `byAggregate`: if disabled, this field does not generate aggregation filters.

## Query and Aggregation

### Aggregation

https://neo4j.com/docs/graphql/current/queries-aggregations/aggregations/

- `shortest`, `longest`
- `min`, `max`, `average`, `sum`
- `min`, `max`

## Filtering

- `_LT`
- `_LTE`
- `_GT`
- `_GTE`

```graphql
query {
  users(where: { age: { _lt: 50 } }) {
    id
    name
    age
  }
}
```

These features can be disabled or enabled

```js
const features = {
  filters: {
    String: {
      LT: true,
      GT: true,
      LTE: true,
      GTE: true,
    },
  },
};

const neoSchema = new Neo4jGraphQL({ features, typeDefs, driver });
```

There are much more aggregate functions.

## Sorting

https://neo4j.com/docs/graphql/current/queries-aggregations/sorting/

```graphql
query {
  movies(options: { sort: [{ runtime: ASC }] }) {
    title
    runtime
  }
}
```

## Pagination

https://neo4j.com/docs/graphql/current/queries-aggregations/pagination/

```graphql
query {
  users(options: { offset: 10, limit: 10 }) {
    name
  }
}
```

## Authentication and Authorization

https://neo4j.com/docs/graphql/current/authentication-and-authorization/

`@authentication` and `@authorization` directive can be used.

```graphql
type User
  @authentication(operations: [DELETE], jwt: { roles_INCLUDES: "admin" }) {
  id: ID!
  name: String!
  password: String!
}
```

### Authorization without Authentication

```graphql
type User {
  id: ID!
}

type Post
  @authorization(
    filter: [
      { where: { node: { author: { id: "$jwt.sub" } } } }
      {
        requireAuthentication: false
        operations: [READ]
        where: { node: { public: true } }
      }
    ]
  ) {
  title: String!
  content: String!
  public: Boolean!
  author: User! @relationship(type: "AUTHORED", direction: IN)
}
```

## Excluded Directives OGM

https://neo4j.com/docs/graphql/current/ogm/directives/#_excluded_directives

The following directives are excluded from the OGM. Reason: OGM is not designed to be exposed API which needs security measures.

- `@authentication`
- `@authorization`
- `@subscriptionsAuthorization`
- `@query`
- `@mutation`
- `@subscription`
- `@filterable`
- `@selectable`
- `@settable`


This doesn't mean you can't use GraphQL for exposed API. OMG is designed for internal use.

This is how ogm work. Like Prisma. It's always used programmatically on server so there is no need for Auth.

```ts
const ogm = new OGM({ typeDefs, driver });
const User = ogm.model("User");
 const users = await User.find({
    where: { name_REGEX: regex },
    options: {
        offset,
        limit,
        sort
    }
});
```

https://neo4j.com/docs/graphql/current/ogm/installation/

## Introspector

https://github.com/neo4j/graphql/tree/dev/packages/introspector

> This is a tool that enables you, with very little effort, to introspect the schema/data model in an existing Neo4j database and build up a set of data structures that can be transformed into any output format.

Basically it will generate the schema from database relationships.

This could be helpful when you have a database and you want to generate the schema from it, but may not help when you need to design the schema first.


## Codegen

In order to use codegen (https://the-guild.dev/graphql/codegen) to generate TypeScript types and sdk, you have to run a graphql server and pass the url to schema. 

```ts

import type { CodegenConfig } from '@graphql-codegen/cli';

const config: CodegenConfig = {
  overwrite: true,
  schema: "http://localhost:3000/graphql",
  documents: "operations/**/*.gql",
  generates: {
    "src/gql/": {
      preset: "client",
      plugins: []
    },
    'src/gql/req.ts': {
      plugins: ['typescript', 'typescript-operations', 'typescript-graphql-request'],
      config: {
        rawRequest: true
      },
    },
    "./graphql.schema.json": {
      plugins: ["introspection"]
    }
  }
};

export default config;
```

