- [etops](#etops)
- [synopsis](#synopsis)
- [SCP HELP](#scp-help)
- [Docker Cheats](#docker-cheats)


# etops
ET DevOps Repo - packaging and deploying cloud based veget

## Synopsis

1. on your local computer - in a folder called myconfig
	- edit the run, path and model _param yaml files to your satisfaction
2. push your configs from your local computer to the cloud
	- use scp and the destination directory is the docker ship - ubuntu@10.12.x.y:./dropbox
3. ssh to the docker ship 10.12....
4. cd /opt/etops
	- **make cloud_et_for_dummys**
5. **cd runs**/YOUR_RUN_NAME_HERE
	- **make model_prepare**
6. **tmux** -- # you likely want to leverage tmux for long running things over the VPN
7. **bash cmd_...YOUR_RUN_NAME_HERE.sh**
8. Monitoring the running cloud docker container ensamble SEE:
	- [Docker Cheats](#docker-cheats)
9. Tail the log files one for each container
	- There in the ./log directory
	- Example:
		- cd runs/gabes_dog_try1
		- cd ./log
		- tail -f run_gabes_dog_try1_chip44N-78E.log
		- man tail
		- man head
		- man grep
		- man cat
		- man more
		- man man


## scp help

### example

- scp -r -i c:\myhome\mypems\CHS-Butzer-Credentials-KeyPair.pem .\myconfig ubuntu@10.12.68.246:./dropbox


DESCRIPTION         top

     scp copies files between hosts on a network.  It uses ssh(1) for data
     transfer, and uses the same authentication and provides the same secu‐
     rity as ssh(1).  scp will ask for passwords or passphrases if they are
     needed for authentication.

     The source and target may be specified as a local pathname, a remote
     host with optional path in the form [user@]host:[path], or a URI in the
     form scp://[user@]host[:port][/path].  Local file names can be made
     explicit using absolute or relative pathnames to avoid scp treating
     file names containing ‘:’ as host specifiers.

```
ubuntu@ip-10-12-68-246:/opt/etops$ scp --help
unknown option -- -
usage: scp [-346BCpqrv] [-c cipher] [-F ssh_config] [-i identity_file]
           [-l limit] [-o ssh_option] [-P port] [-S program]
           [[user@]host1:]file1 ... [[user@]host2:]file2
```

## Docker Cheats

1. listing docker running containers
	- docker ps
2. listing built or downloaded docker images
	- docker image ls
3. KILL all docker running containers
	- docker kill $(docker ps -q)


# Old Section for curious Engineers Only Section
## References

https://kevcodez.de/posts/2019-08-10-fluent-bit-docker-logging-driver-elasticsearch/


## Concepts 

1. docker applications should just log to stdout

2. docker logging driver catches those log-events

3. logging events are processed and forwarded


## Fluentbit - takes 1/10 the resources of fluentd

- Fluent Bit can be configured by file or command line.

There are different sections of configuration:

    Service

- defines the global behavior of the Fluent Bit engine
Input
- defines the source from where Fluent Bit can collect data
Parser
- take unstructured log entries and give them structure
Filter
- allows to alter the incoming data generated by the input plugins
Output
- defines where Fluent Bit should flush the information it gathers from the input

```

[SERVICE]
	log_level debug

# The stdin plugin allows to retrieve valid JSON text messages over the standard input interface (stdin)
[INPUT]
	Name stdin

# The Record Modifier Filter plugin allows to append fields or to exclude specific fields.
[FILTER]
	Name record_modifier
	Match *
	Record hostname ${HOSTNAME}

# The stdout output plugin allows to print to the standard output the data received through the input plugin.
[OUTPUT]
	Name stdout
```


