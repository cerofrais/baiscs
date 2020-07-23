# Basic guide to have a dockerzie a flask app 

Flask : https://flask-doc.readthedocs.io/en/latest/

Docker: https://docs.docker.com/

Fastapi: https://fastapi.tiangolo.com/

## CMD to build docker image :
1. Any build arguments, tags needed should be added here.
2. By default . points to Dockerfile and u can give filename by -f argument.

    ```$ sudo docker build -t imagename .```

## CMD to run docker image
1. Any environment variables needed to run the docker container goes here with -e argument
2. port mapping is hostport:exposeddockerport
3. -d is for detach, if you need the the logs you can do -it
    
    ```$ sudo docker run -d -p 1111:1111 --name containername imagename```

## To See current running images and containers
1. Images
```$ sudo docker images```
2. Containers
```$ sudo docker ps -a```
3. Stats of a running container
```$ sudo docker stats containername```


## CMD to ssh into a running docker container
1. Container should be running

    ```$ sudo docker exec -it containername /bin/bash```



## Clean up
1. To delete all unused(not attached to any container) images.

    ```$ sudo docker system prune -a```
2. To stop a running container.

    ```$ sudo docker stop containername```
3. To delete an image., -f can be used to force

    ```$ sudo docker rmi image name```


### Things to check : 
1. If the port being used in the flask app and the port exposed in Dockerfile are same.
2. As we do in git to ignore files we add the path to `.gitignore`, same can be done with `.dockerignore`

### Other things to checkout:
1. Attaching volumes to a container
2. Adding in newrelic for logging.
3. instead of docker `run` one can try docker `compose`,`start`,`stop`

