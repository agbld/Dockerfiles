# flutter
Including latest environment:
- Flutter SDK
- Dart SDK
- Android SDK

To build a docker image, use the following command:
`cd ./general/flutter`
`docker build -t agbld/flutter-dev:latest .`

Or pull the image from Docker Hub:
`docker pull agbld/flutter-dev:latest`

To run a container with a shared folder and GPU support, use the following command:
`docker run -d --name flutter -v E:\:/mnt/e -p [external_port]:22 flutter`