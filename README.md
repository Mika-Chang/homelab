# Microservices Repo
Respository built to run and track microservices run in docker containers.

Currently supported services
- Nginx reverse proxy
- Personal portfolio website

## Run Services
To run the services, run `docker compose up -d --build` from the parent directory of the repo.

## Dependencies
- docker
- git (optionally)

## TODO
- Set up logging
- Set up program to update and reload compose files without downtime depending on desired services
