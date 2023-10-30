In a distributed system, logging gets harder.
In a regular application, the program could simply log to a file, e.g. one day one file.
It gets complicated in a distributed system as there could be multiple instances of the same microservice. One client could potentially be using multiple instances, thus we must combine the logs while debugging. If instances are always on, we could collect the log files and merge them, but there are scenarios where this is not possible.
If you are using K8S, cloud run or any auto-scalable distributed system, the instance gets destroyed when it's no longer needed, and log could be lost.
The simpliest solution to this is probably using a database instead of log files for logging. A log database can be always online while microservice instances all log to this log database.
However database is far more expensive than storing plain files.
How can we make multiple instances log to a single file.

## Message Queue
One solution is message queue. Usually, when a message queue is used, the messages produced by one producer are consumed by multiple consumers. Consumers may consume the messages differently or they are simply workers for extra computation power. 
In the logging scenario, there would be multiple producer and one consumer. 
Multiple Instances of a server microservice could publish logs to the same topic, "log:server". One single consumer will pick up all logs and store them into a file.
There could be bottleneck with this method. If there are too many server instances and so much log, a single logger consumer may not be enough. In this case, multiple logger consumers and log merging may be necessary. It's still better than losing the logs produced by destroyed instances.

