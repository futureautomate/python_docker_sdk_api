# python_docker_sdk_api
#This project was created for a demo in DevTools 2.0 meetup held at cashfree payments in bangalore. The code is a api end point used to using python docker sdk to control basic functtionalities of Docker.


# How to run the app

### install fastapi and uvicorn server and docker sdk
#### pip install docker
#### pip install fastapi


## Command to run the code 
### uvicorn main:app --host 0.0.0.0 --port 8000 --reload



## Sample Api Calls

### Base URL - http://127.0.0.1:8000/containers/   user same as a get call for getting list of conatiners

## Create Continer
### Post - baseurl    body - {"name": "somenew3"} 

## Stop Continer
### Post - baseurl/{conatinername}/stop

## Delete Continer
### Delete - baseurl/{conatinername}






