# Bring up the service

```
$ docker network create application-network
$ set -a
$ source .env
$ docker-compose build
$ docker-compose up
```