# my_dockerfiles
To build a docker image, use the following command:
`cd [dockerfile_folder]`
`docker build -t [image_name] .`
To run a container with a shared folder and GPU support, use the following command:
`docker run -d --name [container_name] -v C:\Users\agibl\docker_shared_folders\[container_folder_name]:/mnt/docker_shared_folders -p [external_port]:22 --gpus all [image_name]`