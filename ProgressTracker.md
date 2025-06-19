# Progress Tracking
Some notes on what I did and my thoughts on the project

## 25/06/19
### Top Level Compose File
Added top level compose file for singe run of `docker compose up`
### Portfolio Added
Added a portfolio directory to the project to run a portfolio inside the repo instead of outside it. I also added a gitignore file to ignore the portfolio files (those are in a separate repo)
### Docker Networking
Added support for internal and external networks using docker compose to keep ports secure on the host machine. The `frontend` network is a bridge network acessible outside the containers for the reverse-proxy to communicate with clients. The `backend` network is an internal bridge network used for docker containers. More internal networks can be added in the future to keep services separate.
### Nginx Config Updated
Added a `conf` directory for different nginx configurations. Currently the config is set to proxy my svelte porfolio site running in a separate container, but this could be changed in the future.
- TODO: potentially add a bind mount to the conf directory to directly update the nginx container's `nginx/conf.d` directory
### Next Steps:
- Add a script that runs the services instead of running compose directly
- Add a script that can change and reload the nginx configuration depending on my desired services
- Add a script that clones my portfolio git repo when I run my portfolio container
