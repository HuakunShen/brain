---
title: NestJS + Neo4j + GraphQL Setup
authors: huakun
tags: [Web, GraphQL, NestJS, Neo4j, Database]
---

- [GraphQL Schema](#graphql-schema)
- [NestJS Server Configuration](#nestjs-server-configuration)
  - [GraphQL Module](#graphql-module)
- [Codegen](#codegen)

**GitHub Repo:** https://github.com/HuakunShen/nestjs-neo4j-graphql-demo

I haven't found a good update-to-date example of using Neo4j with NestJS and GraphQL. So I decided to write one myself.

Neo4j's graphql library has updated its API, some examples I found online were outdated (https://neo4j.com/developer-blog/creating-api-in-nestjs-with-graphql-neo4j-and-aws-cognito/). This demo uses v5.x.x.

## GraphQL Schema

```graphql
type Mutation {
  signUp(username: String!, password: String!): String
  signIn(username: String!, password: String!): String
}

# Only authenticated users can access this type
type Movie @authentication {
  title: String
  actors: [Actor!]! @relationship(type: "ACTED_IN", direction: IN)
}

# Anyone can access this type
type Actor {
  name: String
  movies: [Movie!]! @relationship(type: "ACTED_IN", direction: OUT)
}

# Only authenticated users can access this type
type User @authentication {
  id: ID! @id
  username: String!
  # this is just an example of how to use @authorization to restrict access to a field
  # If you list all users without the plaintextPassword field, you will see all users
  # If you list all users with the plaintextPassword field, you will only see the user whose id matches the jwt.sub (which is the id of the authenticated user)
  # in reality, never store plaintext passwords in the database
  plaintextPassword: String!
    @authorization(filter: [{ where: { node: { id: "$jwt.sub" } } }])
  password: String! @private
}
```

## NestJS Server Configuration

### GraphQL Module

A GraphQL module can be generated with `bunx nest g mo graphql`.

Here is the configuration. In `new Neo4jGraphQL()`, authorization key is provided for JWT auth. Queries can be restricted by adding `@authentication` or `@authorization` to the type.

One important thing to note is the custom auth resolvers. `Neo4jGraphQL` auto-generate types, queries, mutations implementations for the types in the schema to provide basic CRUD operations, but custom functions like sign in and sign up must be implemented separately. Either as regular REST endpoints in other modules or provide a custom resolver to the `Neo4jGraphQL` instance.

Usually in NestJS, you would add resolvers to the `providers` list of the module, but in this case, the resolvers must be added to the `Neo4jGraphQL` instance. Otherwise you will see the custom queries defined in schema in the playground, but they always return `null`.

```typescript
@Module({
  imports: [
    GraphQLModule.forRootAsync<ApolloDriverConfig>({
      driver: ApolloDriver,
      useFactory: async () => {
        export const { NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD } =
          envSchema.parse(process.env);
        export const neo4jDriver = neo4j.driver(
          NEO4J_URI,
          neo4j.auth.basic(NEO4J_USERNAME, NEO4J_PASSWORD)
        );

        const typedefPath = path.join(RootDir, "src/graphql/schema.gql");
        export const typeDefs = fs.readFileSync(typedefPath).toString();

        const neoSchema = new Neo4jGraphQL({
          typeDefs: typeDefs,
          driver: neo4jDriver,
          resolvers: authResolvers, // custom resolvers must be added to Neo4jGraphQL instead of providers list of NestJS module
          features: {
            authorization: {
              key: "huakun",
            },
          },
        });

        const schema = await neoSchema.getSchema();
        return {
          schema,
          plugins: [ApolloServerPluginLandingPageLocalDefault()],
          playground: false,
          context: ({ req }) => ({
            token: req.headers.authorization,
          }),
        };
      },
    }),
  ],
  providers: [],
})
export class GraphqlModule {}
```

The resolver must be provided to `Neo4jGraphQL` constructor. It must be an object, so NestJS's class-based resolver won't work.

You must provide regular apollo stype resolvers. See https://neo4j.com/docs/graphql/current/ogm/installation/ for similar example.

```ts
export const authResolvers = {
  Mutation: {
    signUp: async (_source, { username, password }) => {
      ...
      return createJWT({ sub: users[0].id });
    },
    signIn: async (_source, { username, password }) => {
      ...
      return createJWT({ sub: user.id });
    },
  },
};
```

Read the README.md of this repo for more details. Run the code and read the source code to understand how it works. It's a minimal example.

## Codegen

https://the-guild.dev/graphql/codegen is used to generate TypeScript types and more from the GraphQL schema.

Usually you provide the graphql schema file, but in this demo, the schema is designed for neo4j and not recognized by the codegen tool.

You need to let `Neo4jGraphQL` generate the schema and deploy it to a server first, then provide the server's endpoint to the codegen tool.
Then the codegen tool will introspect the schema from the server and generate the types.

> Make sure the server is running before running codegen

```bash
cd packages/codegen
pnpm codegen
```

The generated files are in the `packages/codegen/src/gql` folder.

Sample operations can be added to `packages/codegen/operations`. Types and caller for operations will also be generated.

Read the documentation of codegen for more details.

Examples is always provided in the `packages/codegen` folder.

This is roughly how the generated code it works:

You get full type safety when calling the operations. The operations documents are predefined in a central place rather than in the code. This is useful when you have a large project with many operations. Modifying one operation will update all the callers. And if the type is no longer valid, the compiler will tell you.

The input variables are also protected by TypeScript. You won't need to guess what the input variables are. The compiler will tell you.

```ts
import { CreateMoviesDocument } from "./src/gql/graphql";

async function main() {
  const client = new ApolloClient({
    uri: "http://localhost:3000/graphql",
    cache: new InMemoryCache(),
  });
  client
    .mutate({
      mutation: CreateMoviesDocument,
      variables: {
        input: [
          {
            actors: {
              create: [
                {
                  node: {
                    name: "jacky",
                  },
                },
              ],
            },
            title: "fallout",
          },
        ],
      },
    })
    .then((res) => {
      console.log(res);
    });
}
```
