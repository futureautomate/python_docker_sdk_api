# main.py

from fastapi import FastAPI, HTTPException
import docker
from pydantic import BaseModel

app = FastAPI()
client = docker.from_env()

# Predefined Docker image
DOCKER_IMAGE = "bfirsh/reticulate-splines"

class ContainerConfig(BaseModel):
    name: str

@app.post("/containers/")
async def create_container(config: ContainerConfig):
    try:
        container = client.containers.run(DOCKER_IMAGE, name=config.name, detach=True)
        return {"id": container.id, "name": container.name, "status": container.status}
    except docker.errors.DockerException as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/containers/{container_name}/stop")
async def stop_container(container_name: str):
    try:
        container = client.containers.get(container_name)
        container.stop()
        return {"name": container_name, "status": "stopped"}
    except docker.errors.NotFound:
        raise HTTPException(status_code=404, detail="Container not found")
    except docker.errors.DockerException as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/containers/")
async def list_containers():
    containers = client.containers.list()
    running_containers = [container for container in containers if container.status == "running"]
    return [{"id": container.id, "name": container.name, "status": container.status} for container in running_containers]


@app.delete("/containers/{container_name}")
async def delete_container(container_name: str):
    try:
        container = client.containers.get(container_name)
        container.remove(force=True)
        return {"name": container_name, "detail": "Container deleted"}
    except docker.errors.NotFound:
        raise HTTPException(status_code=404, detail="Container not found")
    except docker.errors.DockerException as e:
        raise HTTPException(status_code=400, detail=str(e))

