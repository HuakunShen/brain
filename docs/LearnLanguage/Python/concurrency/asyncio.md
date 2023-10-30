Python has a native asyncio package that supports `async` and `await` (similar to JS). 
We will be using the lastest Python version 3.11, some features may not be available in older Python versions.

## Task Group
In a task group context, tasks are executed concurrently. In the example below, 2 tasks should finish at around the same time.
```python
"""asyncio task group (python 3.11 only)"""

import asyncio

import time

  

async def say_after(delay, what):
	await asyncio.sleep(delay)
	print(what)


async def main():
	async with asyncio.TaskGroup() as tg:
		task1 = tg.create_task(say_after(2, 'hello'))
		task2 = tg.create_task(say_after(2, 'world'))

		print(f"started at {time.strftime('%X')}")
	# The await is implicit when the context manager exits.
	print(f"finished at {time.strftime('%X')}")
asyncio.run(main())
print("finished all")
```

## asyncio.gather()
The gather method also blocks the code from keep running

```python
import asyncio

async def say(msg: str):
    await asyncio.sleep(1)
    print(f"say: {msg}")


async def main():
    await say("a")

    # this is also valid:
    await asyncio.gather(
        say("b"),
        say("c")
    )
    print("finished")

asyncio.run(main())
```

## Queue
Not thread safe.
[Queues — Python 3.11.2 documentation](https://docs.python.org/3/library/asyncio-queue.html)
`asyncio.Queue` is similar to [Golang: WaitGroups](https://gobyexample.com/waitgroups)
Tasks are created, added to queue and executed concurrently. 
`task_done()` is called after each job is finished. `queue.join()` will wait for all tasks in queue to finish. 
```python
import asyncio
import random
import time


async def worker(name, queue):
    while True:
        # Get a "work item" out of the queue.
        sleep_for = await queue.get()

        # Sleep for the "sleep_for" seconds.
        await asyncio.sleep(sleep_for)

        # Notify the queue that the "work item" has been processed.
        queue.task_done()

        print(f'{name} has slept for {sleep_for:.2f} seconds')


async def main():
    # Create a queue that we will use to store our "workload".
    queue = asyncio.Queue()

    # Generate random timings and put them into the queue.
    total_sleep_time = 0
    for _ in range(20):
        sleep_for = random.uniform(0.05, 1.0)
        total_sleep_time += sleep_for
        queue.put_nowait(sleep_for)

    # Create three worker tasks to process the queue concurrently.
    tasks = []
    for i in range(3):
        task = asyncio.create_task(worker(f'worker-{i}', queue))
        tasks.append(task)

    # Wait until the queue is fully processed.
    started_at = time.monotonic()
    await queue.join()
    total_slept_for = time.monotonic() - started_at

    # Cancel our worker tasks.
    for task in tasks:
        task.cancel()
    # Wait until all worker tasks are cancelled.
    await asyncio.gather(*tasks, return_exceptions=True)

    print('====')
    print(f'3 workers slept in parallel for {total_slept_for:.2f} seconds')
    print(f'total expected sleep time: {total_sleep_time:.2f} seconds')


asyncio.run(main())
```

