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

## Logging
All services logging all their activity.
In each api there is a logs directory, where logs are stored. We set the logging level in the api.env file of each application. 
Three logging levels are available:
- DEBUG
- INFO
- ERROR

## Service Discovery and Load Balancer
The Service Discovery and Load Balancer are handled by Consul. 
All services are logged automatically via the service_registrar script run automatically at startup with docker compose.
All services are available at address:
```http://localhost:8500/```

## Class Diagram

### Auth service

### Product service

### Cart service

### Review service

## API's Documentation

### Auth service API

```http://localhost:8001/api/schema/swagger-ui/#/```

### Product service API

```http://localhost:8002/api/schema/swagger-ui/#/```
### Cart service API

```http://localhost:8003/api/schema/swagger-ui/#/```

### Reviews

```http://localhost:8004/api/schema/swagger-ui/#/```


## How to run

1. Clone projekt:

```bash
git@github.com:BlazejBielski/ip_management.git
```
2. Przechodzimy do katalogu z projektem.
3. Kopiujemy pliki z katalogu envs nadając im odpowiednio nazwy:
- backend.env
- postgres.env
4. Przykładowe uzupełnienie plików env:
```
DJ_SECRET_KEY="django-insecure-ih$-8kb2(_49%8t=+o^s$n=0rvpqci0d-8hgui&-phzslfi4y5"
DJ_DEBUG=1
DJ_ALLOWED_HOSTS=localhost 0.0.0.0 127.0.0.1
DJANGO_LOGLEVEL='info'
```
```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

DB_CONNECTION_STRING=postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}
```
5. Uruchamiamy projekt.

```bash
docker compose up
```
Uwaga — serwis przy starcie zasila bazę danych z bazy wiedzy, może to potrwać do kilku minut.
envs
docker