#!/usr/bin/bash
# assumes there is a local repo of Mika-Chang.github.io in the portfolio directory.
cd portfolio/Mika-Chang.github.io && git pull
cd ../..
docker compose build
docker compose up -d
