# GraphQL Shield

> GraphQL Permissions Framework For Complex Authorisation Systems

> Implement your server permissions in a clear and deterministic way and let it guard access to your schema.

https://www.graphql-shield.com/

Define rule functions, each query/mutation can be authorized by one or multiple rules.

## Example

```js
import { shield, rule, and, or } from 'graphql-shield'

const isAdmin = rule()(async (parent, args, ctx, info) => {
  return ctx.user.role === 'admin'
})

const isEditor = rule()(async (parent, args, ctx, info) => {
  return ctx.user.role === 'editor'
})

const isOwner = rule()(async (parent, args, ctx, info) => {
  return ctx.user.items.some((id) => id === parent.id)
})

const permissions = shield({
  Query: {
    users: or(isAdmin, isEditor),
  },
  Mutation: {
    createBlogPost: or(isAdmin, and(isOwner, isEditor)),
  },
  User: {
    secret: isOwner,
  },
})
```


## Custom Errors

This is important and often an easy to ignore point.

When I throw errors (even if the mutation has nothing to do with shield), the server always return `INTERNAL_SERVER_ERROR`, no matter what type of error I throw. Everything back to normal if I stop using shield.

https://www.graphql-shield.com/docs/errors#custom-errors

> Shield, by default, catches all errors thrown during resolver execution. This way we can be 100% sure none of your internal logic can be exposed to the client if it was not meant to be.

> To return custom error messages to your client, you can **return error instead of throwing it**. This way, Shield knows it's not a bug but rather a design decision under control. Besides returning an error you can also return a string representing a custom error message.

> You can return custom error from resolver or from rule itself. Rules that return error are treated as failing, therefore not processing any further resolvers.