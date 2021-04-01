To run it on Docker Desktop for Windows:

- install X11 server
- Launch a Display client
- Set the Display Env Variable in docker-compose yml to your IPV4 address of your host and the client number
- Run docker-compose up

To run it on Docker in Ubuntu System:
-Set DISPLAY as $DISPLAY
-Uncomment the following lines in the docker-compose yml:
    #volumes:
    #      - $HOME/.Xauthority:/root/.Xauthority:rw