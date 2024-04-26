Although JavaScript is single threaded, it comes with asynchronous operations as JS needs to deal with async web requests all the time. 
JS achieves this with event loop and Promise.
In Python we have multi-threading, multi-processing and async to achieve similar result.

https://realpython.com/python-concurrency/
| Concurrency Type                       | Switching Decision                                           | Number of Processors |
| -------------------------------------- | ------------------------------------------------------------ | -------------------- |
| Pre-emptive multitasking (`threading`) | The operating system decides when to switch tasks external to Python. | 1                    |
| Cooperative multitasking (`asyncio`)   | The tasks decide when to give up control.                    | 1                    |
| Multiprocessing (`multiprocessing`)    | The processes all run at the same time on different processors. | Many                 |

