# etops
ET DevOps Repo - packaging and deploying cloud based veget

## References

https://kevcodez.de/posts/2019-08-10-fluent-bit-docker-logging-driver-elasticsearch/


## Concepts 

1. docker applications should just log to stdout

2. docker logging driver catches those log-events

3. logging events are processed and forwarded


## Fluentbit - takes 1/10 the resources of fluentd

- Fluent Bit can be configured by file or command line.
