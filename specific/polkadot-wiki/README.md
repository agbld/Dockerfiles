# my_dockerfiles - polkadot-wiki
To build a Docker image, use the following command:
```bash
cd [dockerfile_folder]
docker build -t polkadot-wiki .
```

To run a container, use the following command:
```bash
docker run -dt --rm --name polkadot-wiki -p 3000:3000 polkadot-wiki
```

To run a container for devepolment, use the following command:
```bash
docker run -dt --name polkadot-wiki-dev -p 2222:22 -p 3001:3000 polkadot-wiki
```

<!--
`docker run -d --name polkadot-wiki -v E:\docker_shared_folders\agbld\polkadot-wiki:/mnt/docker_shared_folders -p 2222:22 -p 3000:3000 polkadot-wiki`
-->

After starting the polkadot-wiki container, you should be able to visit a locally hosted Polkadot Wiki website by navigating to http://localhost:3000 in your browser.

Please note that due to security concerns, some browsers (like Edge) might **not allow you to visit a non-HTTPS address**. If you encounter any issues, remember to **check your browser settings** or consider switching to a different browser (such as Chrome).