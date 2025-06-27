#!/usr/bin/bash
cd portfolio/Mika-Chang.github.io && git pull
cd ../..
docker compose build
docker compose up -d
