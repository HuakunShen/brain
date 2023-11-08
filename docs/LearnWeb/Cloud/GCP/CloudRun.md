# Cloud Run

## Volumes

It's easy to mess up the volume mount path in cloud run production.

Under volumes tab, you can add a secret volume type, choose a secret from Secret Manager.

The mount path can be a filename, such as `.env`.

Then go to the `Container(s)` tab. Under `VOLUME MOUNTS` you can add **Volume Mount**.

The mount path points to the folder where the secret file is mounted, but the folder has to be empty in your source code. Cloud Run doesn't allow mounting a single file, the mounted folder will replace the folder in your source code. 

If your source code is in `/xc-server`, and the mount path is set to `/xc-server` with the mounted file at `/xc-server/.env`, then the `/xc-server` folder will be completely removed and contain only the `.env` file.

What I do is mount the folder to `/xc-server/env/.env`, then in the source code load the `.env` file from `/xc-server/env/.env`.

