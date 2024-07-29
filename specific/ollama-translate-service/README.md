# my_dockerfiles - ollama-translate-service
This Dockerfile is designed to set up a service that adapts the Ollama LLM model into a REST API translation service, intended for use with the [沉浸式翻譯 (Immersive Translate)](https://immersivetranslate.com/) Chromium extension.

Before proceeding, ensure that an [Ollama](https://github.com/ollama/ollama) container is running on your local machine. For instructions on setting up the environment, please refer to: [Docker Setup Guide](https://github.com/ollama/ollama#docker).


## Setup
To build a docker image, use the following command:
```
docker build -t ollama-translate-service .
```

To run a container, use the following command:
```
docker run -d --name ollama-translate-service -p 5000:5000 --add-host=host.docker.internal:host-gateway ollama-translate-service --host host.docker.internal --port 11434 --model phi3:14b --post-prompts ""
```

Modify following parameters as needed:
- `-p [PORT]:5000`: the port of the Ollama Translate Service container (default: 5000)
- `--host`: the host of the Ollama container
- `--port`: the port of the Ollama container
- `--model`: the model of the Ollama container, e.g. `phi3:14b`, `llama3.1`
- `--post-prompts`: the post-prompts of the Ollama container (This is currently disabled)