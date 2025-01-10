---
title: Svelte FAQ
---

This is a collection of my common questions and solutions with svelte/sveltekit.

## Data Passing

### How to access data and type in `+page.svelte` for data loaded from `+page.server.ts` and `+layout.server.ts`?

If you return some data from `+page.ts`, in `+page.svelte` you can access it with `$props().data`.
There is type auto-completion for the data you return from `+page.ts` in `+page.svelte`.
Sveltekit compiler updates the type in the background.

```ts title="+page.ts"
export const load = () => {
  return {
    hello: "world",
  };
};
```

But if you return some data from `+layout.server.ts` or `+page.server.ts`, you can't access it directly in `+page.svelte`.
The data is also accessible in `$props().data`, but no type auto-completion.

The solution is simple, you have to manually import it from the correct location.

For example, if the data is returned from a `+layout.server.ts` 2 levels up, you can import it from `../../$types`.

```ts title="dashboard/+layout.server.ts"
import type { LayoutServerLoad } from "./$types";

export const load: LayoutServerLoad = async ({
  locals: { supabase, session },
}) => {
  const { data: myExtensions } = await supabase
    .from("extensions")
    .select("identifier, icon, name, downloads, api_version, version")
    .filter("author_id", "eq", session?.user.id)
    .order("downloads");
  return { myExtensions: myExtensions ?? [] };
};
```

```ts title="dashboard/register-extension/jsr/+page.svelte"
import type { PageData } from "./$types";
import type { LayoutServerData } from "../../$types";

const { data }: { data: PageData & LayoutServerData } = $props();
```
