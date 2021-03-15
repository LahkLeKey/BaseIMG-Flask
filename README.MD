# Basic Starter Image

Ports Used : **_5000_**

## Flask w/ Docker compose

### Written by Kyle Halek

LahkLeKey@gmail.com <br>

Kyle@LahkLeKey.com

## Dockerhub Image

`lahklekey/baseimgflask:latest`

> This works well with app containers on digital ocean.
> Just make an app select docker application and then point to the dockerhub and it is deployed.

https://hub.docker.com/repository/docker/lahklekey/baseimgflask

## Fresh Install

1. `ssh USERNAME@IP`

2. `git clone https://github.com/LahkLeKey/BaseIMG-Flask.git`

3. `cd BaseIMG-Flask`

4. `docker-compose up -d`

5. Visit IP:5000 and application should be deployed.
