#!/bin/bash
docker run -d -p 1000:80 -p 5000:5000 --name shadow_fighters captain0pool/hint:latest "/home/startup.sh"
