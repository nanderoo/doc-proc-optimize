# Notes:

This repo contains notes on a [sample Azure Function](initial.py) that processes document data, and what considerations we might take to make it more scalable and maintainable.

## Initial Recommendations:

* Avoid locking via async
* Handle input/payload errors
* Ensure all responses have status codes
* Make processed values configurable vs hard-coded
* Row iteration vs lambda call - PD Vectors
* Add Logging/Metrics

- These are all quick & easy fixes where AI tools can help.

## Thinking Bigger:

* Request Data Input Limitations
* Separate Business Logic from Request Processing
* Larger Documents & Memory Limits for AZ Funcs
* Split Request/Response, Parsing, Processing, Etc
* Queues / Kafka / Flink / Etc
* Cloud-provider Agnostic 
