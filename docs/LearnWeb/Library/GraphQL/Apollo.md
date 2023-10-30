# Apollo

https://www.apollographql.com/docs/

## Apollo Client

- [React](https://www.apollographql.com/docs/react)
- [IOS](https://www.apollographql.com/docs/ios)
- [Kotlin](https://www.apollographql.com/docs/kotlin)

## Backend

- [Apollo Server](https://www.apollographql.com/docs/apollo-server/)
  - > Configure a production-ready GraphQL server to fetch and combine data from multiple sources.
- [Federation](https://www.apollographql.com/docs/federation/)
  - > Implement a single unified supergraph across multiple subgraphs.
- [Router](https://www.apollographql.com/docs/router)
  - > A configurable, high-performance graph router for a federated supergraph.

## Cloud

- [Apollo Studio](https://www.apollographql.com/docs/studio/)
  - > Build your supergraph with your team, evolve it safely, and keep it running smoothly.
- [Rover CLI](https://www.apollographql.com/docs/rover)
  - > Manage your Studio graphs and schemas from the command line.

# Error Handling

> Making errors actionable on the client and server

> Whenever Apollo Server encounters errors while processing a GraphQL operation, its response to the client includes an errors array that contains each error that occurred. Each error in the array has an extensions field that provides additional useful information, including an error code and (while in development mode) an exception.stacktrace.

## `stacktrace`

[Stacktrace Doc](https://www.apollographql.com/docs/apollo-server/data/errors/#omitting-or-including-stacktrace)

By default, Apollo Server omits the `exception.stacktrace` field if the NODE_ENV environment variable is set to either `production` or `test`.

## Sample Error Output

```json
{
  "errors": [
    {
      "message": "Cannot query field \"__typenam\" on type \"Query\".",
      "locations": [
        {
          "line": 1,
          "column": 2
        }
      ],
      "extensions": {
        "code": "GRAPHQL_VALIDATION_FAILED",
        "exception": {
          "stacktrace": [
            "GraphQLError: Cannot query field \"__typenam\" on type \"Query\".",
            "    at Object.Field (/my_project/node_modules/graphql/validation/rules/FieldsOnCorrectTypeRule.js:48:31)",
            "    ...additional lines..."
          ]
        }
      }
    }
  ]
}
```

## Error Types

[Error Codes](https://www.apollographql.com/docs/apollo-server/data/errors/#error-codes)

The error codes are present in `errors.extensions.code`.

| Error Code                      | Error Class                       |
| ------------------------------- | --------------------------------- |
| `GRAPHQL_PARSE_FAILED`          | `SyntaxError`                     |
| `GRAPHQL_VALIDATION_FAILED`     | `ValidationError`                 |
| `BAD_USER_INPUT`                | `UserInputError`                  |
| `UNAUTHENTICATED`               | `AuthenticationError`             |
| `FORBIDDEN`                     | `ForbiddenError`                  |
| `PERSISTED_QUERY_NOT_FOUND`     | `PersistedQueryNotFoundError`     |
| `PERSISTED_QUERY_NOT_SUPPORTED` | `PersistedQueryNotSupportedError` |
| `INTERNAL_SERVER_ERROR`         | `None`                            |

For example:

- `UserInputError`: Invalid Input, extra info included in `errors.extensions`

```js
// ...
userWithID: (parent, args, context) => {
  if (args.id < 1) {
    throw new UserInputError("Invalid argument value");
  }
  // ...fetch correct user...
};
// ...

// Custom Error Info
throw new UserInputError("Invalid argument value", {
  argumentName: "id",
});
// ...
```

Sample Error Output for Customized Input

```json
{
  "errors": [
    {
      "message": "Invalid argument value",
      "locations": [
        {
          "line": 2,
          "column": 3
        }
      ],
      "path": ["userWithID"],
      "extensions": {
        "argumentName": "id",
        "code": "BAD_USER_INPUT",
        "exception": {
          "stacktrace": [
            "UserInputError: Invalid argument value",
            "    at userWithID (/my-project/index.js:25:13)",
            "    ...more lines..."
          ]
        }
      }
    }
  ]
}
```

## Custom Errors

[Custom Errors](https://www.apollographql.com/docs/apollo-server/data/errors/#custom-errors)

> You can create a custom error by defining your own subclass of ApolloError, or by initializing an ApolloError object directly

## Masking and Logging Errors (Error Interception)

> You can edit Apollo Server error details before they're passed to a client or reported to Apollo Studio. This enables you to omit sensitive or irrelevant data.

Add a `formatError` function when initializing server to inspect and modify error message before returning to client. See [Client Response Handling](https://www.apollographql.com/docs/apollo-server/data/errors/#for-client-responses).

```js
const server = new ApolloServer({
  typeDefs,
  resolvers,
  csrfPrevention: true,
  formatError: (err) => {
    // Don't give the specific errors to the client.
    if (err.message.startsWith('Database Error: ')) {
      return new Error('Internal server error');
    }

    // Otherwise return the original error. The error can also
    // be manipulated in other ways, as long as it's returned.
    return err;
  },
});


// Use `instanceof` of Error Class
formatError(err) {
	if (err.originalError instanceof AuthenticationError) {
		return new Error('Different authentication error message!');
	}
}
```

### For Apollo Studio Reporting

`formatError` doesn't modify errors sent to Apollo studio.

See [Docs](https://www.apollographql.com/docs/apollo-server/data/errors/#for-apollo-studio-reporting) for details.

For example, [Example: Ignoring common low-severity errors](https://www.apollographql.com/docs/apollo-server/data/errors/#example-ignoring-common-low-severity-errors).

## HTTP Status Code

By default, GraphQL doesn't use HTTP status codes. See [Docs](https://www.apollographql.com/docs/apollo-server/data/errors/#returning-http-status-codes) for how to do it using a plugin.

# Testing

- [Integration Testing](https://www.apollographql.com/docs/apollo-server/testing/testing/)
  - Utilities for testing Apollo Server
  - [Testing using `executeOperation`](https://www.apollographql.com/docs/apollo-server/testing/testing/#testing-using-executeoperation)
    - > Apollo Server's executeOperation method enables you to run operations through the request pipeline without sending an HTTP request.
  - [End-to-end testing](https://www.apollographql.com/docs/apollo-server/testing/testing/#end-to-end-testing)
    - No built-in support for now, just use any http or GraphQL client and testing framework like **Jest**.
