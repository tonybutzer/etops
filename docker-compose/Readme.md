# ElasticSearch and Kibana via compose

## Objectives

- Manage and SCan logs from docker containers at scale
- alert on error conditions
- improve the VegET code by improving error handling and retries
- keep it simple as possible

## TODO

1. get elastic and kibana running in docker-compose
2. understand fluentd - replace with lighter fluentbit
3. test run this with a log tester or with veget container

## Architecture

https://www.fluentd.org/guides/recipes/elasticsearch-and-s3

![](https://www.fluentd.org/assets/img/recipes/elasticsearch-s3-fluentd.png)

## Doc

- the ./etc dir contains configs for elastic, kibana, fleuntd

### How to source docker into fluetd?
https://www.fluentd.org/guides/recipes/docker-logging

> The old fashion way is to write these messages to a log file, but that inherits certain problems specifically when we try to perform some analysis over the registers, or in the other side, if the application have multiple instances running, the scenario becomes even more complex.


### Testing the log handling pipeline

```
docker run --log-driver=fluentd --log-opt tag="docker.{.ID}}" ubuntu echo 'Hello Fluentd!'
Hello Fluentd!
```

### Running fluentd in a container exposed to the host on 24224

https://github.com/kzk/docker-compose-efk/tree/master/fluentd





## References

https://medium.com/better-programming/elasticsearch-cluster-and-kibana-using-docker-compose-4f9c4d6c5470

https://github.com/maxyermayank/docker-compose-elasticsearch-kibana/blob/master/README.md


## Memory Issues Complicate Things - BUMMER!

https://hostadvice.com/how-to/how-to-limit-a-docker-containers-resources-on-ubuntu-18-04/

```
