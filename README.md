# deploy flask app in docker

use [gunicorn](http://gunicorn.org/) as web server,  [nginx](https://nginx.org/)  as proxy server.then deploy this in [docker](https://www.docker.com/) by [docker-compose](https://docs.docker.com/compose/)

**start:**

```shell
docker-compose build
docker-compose up
```

**restart:**

```shell
docker-compose up -d
```
