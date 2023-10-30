# GraphQL

[Official Website](https://graphql.org/)

> GraphQL is a query language for APIs and a runtime for fulfilling those queries with your existing data. GraphQL provides a complete and understandable description of the data in your API, gives clients the power to ask for exactly what they need and nothing more, makes it easier to evolve APIs over time, and enables powerful developer tools.

## Tools

- [Apollo](./Apollo.md)
  - The most popular GraphQL framework that supports both frontend and backend.
- [Codegen](./Codegen.md)
  - Generate all kinds of code based on GraphQL schema, such as TypeScript, MongoDB Schema, introspection, and shortcuts for React, Vue, etc. with combinations of plugins.
  - This largely facilitates the development process, avoid rewriting code when GraphQL schema changes.
- [GraphQL-Shield](./GraphQL-Shield.md)
## Testing

- [Apollo](./Apollo.md) has notes for testing Apollo Server
- [Postman](../../../LearnTools/developer/full-stack/Postman.md) also supports developing and testing GraphQL
  - It's a good choice if you want to integrate other tests with GraphQL tests.
  - See [Postman Notes](../../../LearnTools/developer/full-stack/Postman.md) for more details.


## Common Problems

- Always get `INTERNAL_SERVER_ERROR` when using `shield` no matter what Error you are throwing
  - This is because all catched thrown errors are caught by shield and translated to `INTERNAL_SERVER_ERROR` to avoid exposing internal code
  - See [Custom Errors](https://www.graphql-shield.com/docs/errors).
  - **Short Answer: Return Error instead of throwing it**

## Common Usage

- [Apollo Authentication and Authorization](https://www.apollographql.com/docs/apollo-server/security/authentication/)