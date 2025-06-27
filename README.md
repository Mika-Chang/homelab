# Homelab Repo
Respository built to track changes to my homelab (technically just my VPS instance right now).

Currently supported services
- Nginx reverse proxy
- Personal portfolio website

## Run Services
To run the services, clone my github pages repo into the `portfolio` directory and run `update-containers.sh` from the parent directory of the repo.

## Dependencies
- docker
- git

## TODO
- Set up logging
- Set up program to update and reload compose files without downtime depending on desired services
