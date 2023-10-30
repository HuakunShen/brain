---
title: TypeScript Sample Usage
---

# Merge Types

> Reference: https://stackoverflow.com/questions/48215950/exclude-property-from-type

If 2 types have no conflict fields, use intersection operator directly

```ts
type A = { a: number };
type B = A & { b: string };
```

If 2 types have common fields, we need to `Omit` the conflict types first

```ts
type A = { a: number; b: number };
type B = Omit<A, "a" | "b"> & { a: string; b: string };
```
