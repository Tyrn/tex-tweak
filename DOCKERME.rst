Using this application with Docker
**********************************

Raw
===

Build
-----

::

    $ docker build -t tweaker --rm .

Run
---

::

    $ docker run -it --name twk --rm --mount type=bind,source="$HOME"/,target=/home/mnt tweaker

Docker Compose
==============

Configuration
-------------

`.env`:

::

    HOST=$HOME

`docker-compose.yml`:

::

    version: "3.9"
    services:
      tweaker:
        image: tweaker:latest
        volumes:
          - type: bind
            source: $HOME
            target: /home/mnt

Run
---

::

    $ docker-compose run --rm tweaker