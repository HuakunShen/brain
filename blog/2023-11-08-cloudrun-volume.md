---
title: Cloud Run Mount Volume Secret
authors: huakun
tags: [gcp, cloud-run, secret-manager]
---

Cloud Run is a good serverless solution for deploying docker containers. It's easy to deploy and scale.
Normally, if you can run a docker container in local dev environment, you can deploy it to cloud run directly without too much extra configuration. 

However, in my experience, there is one thing that is easy to waste lots of time on, that is mounting a secret file to the container.

## Volumes

Cloud run allows you to add environment variables, but one by one. It's not convenient if you have a lot of environment variables, and if you need to change them often. 

My solution is to add the content of `.env` file to Secret Manager in GCP and mount the secret file to the container, then load the `.env` file in the source code. This way I can update all env vars at once by creating a new version of the secret.

With docker volum, we can mount a single file easily like this `docker run -v ./secret.env:/app/.env image-name`.

However in cloud run, it's not that easy. If you try to configure the volume the same way docker does, your container will fail to start.

Here is the process to mount a secret file to cloud run;

- Under volumes tab, you can add a secret volume type, choose a secret from Secret Manager.
- The mount path can be a filename, such as `.env`.
- Then go to the `Container(s)` tab. Under `VOLUME MOUNTS` you can add **Volume Mount**.

The mount path points to the folder where the secret file is mounted, but the folder has to be empty/non-existent in your source code. Cloud Run doesn't allow mounting a single file, the mounted folder will replace the folder in your source code, because the folder is a protected folder by GCP.

If your source code is in `/xc-server`, and the mount path is set to `/xc-server` with the mounted file at `/xc-server/.env`, then the `/xc-server` folder will be completely removed and contain only the `.env` file.

What I do is mount the folder to `/xc-server/env/.env`, then in the source code load the `.env` file from `/xc-server/env/.env`.
