# E-commerce system with microservices

## Main technologies
* python
* django
* DRF
* postgresql
* JWT
* redis
* kong
* consul
* docker
* docker compose

## Description

The eCommerce with Microservices project tests the Django REST Framework for microservices-based projects. 
The project uses the following technologies:
1. For containerization, Docker was used.
2. Docker Compose was used to manage the process.
3. Consul was used to discover services and as a load balancer.
4. Docker Compose was used to manage the process.
5. Consul was used to find services and balance the workload.
6. Kong was used as an API gateway.
7. Postrgesql was used as a RDBMS
8. Redis was used as a Cache
9. JWT is the key to securing web applications
All microservices have they own instance of database

Consul service discovery and load balancer
http://localhost:8500/


## API's Documentation

Auth service API

http://localhost:8001/api/schema/swagger-ui/#/

Product service API

http://localhost:8002/api/schema/swagger-ui/#/

Cart service API

http://localhost:8003/api/schema/swagger-ui/#/

Reviews

http://localhost:8004/api/schema/swagger-ui/#/


## How to run
envs
docker