# LMS's monorepo

test addition

## Release Notes

### LMS version 1.1

_New Features_

- Ability to deploy locally with `docker` and in production with `docker-compose`.

_Bug Fixes_

- Issues with CORS are fixed.

### LMS version 1.0

_New Features_

- Comment toggling has been added.

_Bug Fixes_

- Tagging is persistent on lettersminglesouls.lmc.gatech.edu.

_Known Bugs_

- Stylistic bugs
  - About page does not "hug" the right side of the screen.
  - Mobile view is not rendered nicely.
  - Sorting dropdown that is selected is blue rather than maroon.

## Install Guide

### Generic Install Information

_Pre-requisites_

- `docker`
- Docker for Mac (if on macOS)

_Dependencies_
The dependencies for each project should be installed in
each docker container before the container is up and running.

Therefore, there should be no need to install any other dependencies.

## Running the Project

To run the project locally, make sure your terminal is in
the `/jif0359` folder and run `docker-compose up --build`.

This should start docker and set up the project using the `docker-compose.yml` file.

The client will be available at `localhost:3000` in your browser.

The back-end api can be tested via the command line at `localhost:5000`. When running this command, the client application makes requests to the back-end app running in the `api_1` container.

The database is also running in the `db_1` container, which the back-end communicates with.

If you change any files, stop the project (directions below) and then run the `docker-compose up --build` command to see the changes take effect.

## Stopping the project

Open another terminal window, go to the main project folder and then run `docker-compose down`.

## Deploying to the server

_PLEASE AVOID DOING THIS UNLESS ABSOLUTELY NEEDED_

If you are looking to deploy, we have a server setup in DigitalOcean. You need the ssh key on your machine in your `/.ssh/` folder. Shelby has the `digital_ocean` ssh key.

Then, run `ssh-add ~/.ssh/digital_ocean` to set the key in your system.

Once that is set, run `export DOCKER_HOST="ssh://root@159.89.87.236` and then `docker-compose up -f docker-compose.production.yml -d`. This will take a while, but will deploy containers to the remote server. The complete application should be working at `http://lettersminglesouls.live/`. If not, there's an issue.

Re-run the last `docker-compose up` command, removing the `-d` to see what issues have occurred.

Once you are done deploying, you want to run `unset DOCKER_HOST`.
