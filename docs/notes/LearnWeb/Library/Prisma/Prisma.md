---
keyword:
  - ORM
  - Node.js
  - TypeScript
---

# Prisma

> Next-generation Node.js and TypeScript **ORM**

> Prisma helps app developers **build faster** and **make fewer errors** with an open source database toolkit for PostgreSQL, MySQL, SQL Server, SQLite and MongoDB (Preview).

[Prisma Website](https://www.prisma.io/)

## Supported Databases (Mar. 2022)

- PostgreSQL
- MySQL
- SQLite
- SQL Server
- [MongoDB](./MongoDB.md)
- CockroachDB

## Supported Languages

- JavaScript
- TypeScript

## Other Features

- [GraphQL](https://www.prisma.io/graphql)

# Migration

[Prisma Migrate](https://www.prisma.io/docs/concepts/components/prisma-migrate)

> Prisma Migrate is an imperative database schema migration tool that enables you to:
>
> - Keep your database schema in sync with your Prisma schema as it evolves and
> - Maintain existing data in your database

> Prisma Migrate generates a history of .sql migration files, and plays a role in both development and deployment.

# CLI

[Prisma CLI reference](https://www.prisma.io/docs/reference/api-reference/command-reference)

## db pull

`prisma db pull`

[db pull](https://www.prisma.io/docs/reference/api-reference/command-reference#db-pull)

> The db pull command connects to your database and adds Prisma models to your Prisma schema that reflect the current database schema.

See [Introspection](#introspection) section.

## db push

`prisma db push`

[db push](https://www.prisma.io/docs/reference/api-reference/command-reference#db-push)

> The db push command pushes the state of your Prisma schema file to the database without using migrations. It creates the database if the database does not exist.

If you made some changes to your Prisma schema, you need to run `prisma generate` first and `prisma db push` to update the database. Otherwise changes like `@unique` property will not be updated to DB. Note, you may also want to use Migration if it's an update but not an initialization.

<h2 className="text-red-400">Be Very Careful with this Command, You could lose Data</h2>

Read [Choosing db push or Prisma Migrate](https://www.prisma.io/docs/concepts/components/prisma-migrate/db-push#choosing-db-push-or-prisma-migrate).

**Short answer: don't use it in production.**

## Migration

`prisma migrate dev`

Similar to also different from `db push`.

> The migrate dev command updates your database using migrations during development and creates the database if it does not exist.

MongoDB not supported.

Read [Choosing db push or Prisma Migrate](https://www.prisma.io/docs/concepts/components/prisma-migrate/db-push#choosing-db-push-or-prisma-migrate).

# Introspection

[Introspection](https://www.prisma.io/docs/getting-started/setup-prisma/add-to-existing-project/mongodb/introspection-typescript-mongodb)

# Transactions and Batch Queries

Read [Docs: Transactions and Batch Queries](https://www.prisma.io/docs/concepts/components/prisma-client/transactions)

## Sequential Prisma Client Operations

```js
const [posts, totalPosts] = await prisma.$transaction([
  prisma.post.findMany({ where: { title: { contains: "prisma" } } }),
  prisma.post.count(),
]);
```
