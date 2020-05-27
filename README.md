# flask_demo

Demonstrates running Flask web server in Docker.

#### Requirements
-  [Docker Desktop](https://www.docker.com/products/docker-desktop)

#### Notes

- docker-compose is optional but simplifies steps to build & run container
- By default, Flask starts on port 5000
- `volumes` setting should allow hot-reload of web server when files are changed. But doesn't seem to work yet