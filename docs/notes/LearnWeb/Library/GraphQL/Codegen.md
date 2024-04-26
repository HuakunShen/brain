# GraphQL Code Generator

https://www.graphql-code-generator.com/

[Plugin Hub](https://www.graphql-code-generator.com/plugins) contains all kinds of plugins that can be used to generate code.

The [main page of the official website](https://www.graphql-code-generator.com/) has some presets of plugin combinations.

[Installation](https://www.graphql-code-generator.com/docs/getting-started/installation) can be found here.

## Sample Configuration

```yaml
overwrite: true
schema: ./src/graphql/schema/**/*.g(raph)?ql
documents: ./src/graphql/schema/operation/clipboard/*.gql
generates:
  ./src/graphql/schema/index.ts:
    plugins:
      - 'typescript'
      - 'typescript-mongodb'
      - 'typescript-document-nodes'
  ./src/graphql/schema/resolvers.ts:
    plugins:
      - typescript
      - typescript-resolvers
  ./src/graphql/schema/ops.ts:
    plugins:
      - 'typescript'
      - 'typescript-operations'
  ./src/graphql/schema/graphql.schema.json:
    plugins:
      - 'introspection'
```

Execute with `graphql-codegen --config codegen.yml`.

4 files will be generated. `typescript` is usually the first plugin to use as basis of other plugins.

The generated `graphql.schema.json` from introspection can be loaded into postman.

Note: Postman supports auto fetching graphql schema when a graphql server is running.