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

## References

https://medium.com/better-programming/elasticsearch-cluster-and-kibana-using-docker-compose-4f9c4d6c5470

https://github.com/maxyermayank/docker-compose-elasticsearch-kibana/blob/master/README.md


## Memory Issues Complicate Things - BUMMER!

https://hostadvice.com/how-to/how-to-limit-a-docker-containers-resources-on-ubuntu-18-04/

```
