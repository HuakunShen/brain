---
title: A JS Way of Hot Reloading Go Server (PocketBase)
authors: [huakun]
tags: [Go, PocketBase]
---

I was working on a Go project by writing PocketBase Go extension code. I wanted to have a hot reload feature for the Go server. I found that there are many ways to achieve this, such as using `air`, `fresh`, `realize`, etc. 

But I wanted to try a different way by using JavaScript/TypeScript.

This gives me more control over the reload process.

## Deno Dev Script

```ts title="deno-dev.ts"
let child: Deno.ChildProcess | null = null;

async function startGoServer() {
  if (child) {
    console.log("Killing previous Go server...");
    child.kill("SIGTERM"); // Send SIGTERM to the process
    await child.status; // Wait for the process to terminate
  }

  const buildCmd = new Deno.Command("go", {
    args: ["build", "-o", "pocketbase", "main.go"],
  });
  await buildCmd.output();
  const cmd = new Deno.Command("./pocketbase", { args: ["serve"] });
  child = cmd.spawn();
  console.log("Go server started.");
}

startGoServer();

for await (const _event of Deno.watchFs("main.go")) {
  console.log("File change detected, restarting server...");
  await startGoServer();
}
```

## Bun Dev Script

```ts title="bun-dev.ts"
import { $, type Subprocess } from "bun";
import { watch } from "fs";

let child: Subprocess | null = null;

async function startGoServer() {
  console.log("Starting Go server...");
  if (child) {
    console.log(`Killing previous Go server with PID: ${child.pid}`);
    await child.kill(9);
    // sleep 3 seconds
    // use setTimeout to iteratively wait until killed is true, check every 1 second
    while (child.killed === false) {
      await new Promise((resolve) => setTimeout(resolve, 1000));
    }
    console.log(`Killed ${child.pid}: ${child.killed}`);
  }
  await $`go build -o pocketbase main.go`;
  child = Bun.spawn(["./pocketbase", "serve"], {
    stdio: ["inherit", "inherit", "inherit"],
  });
  console.log(`Go server started with PID: ${child.pid}`);
}

startGoServer();
watch("./main.go", { recursive: true }, async (event, filename) => {
  await startGoServer();
});
```