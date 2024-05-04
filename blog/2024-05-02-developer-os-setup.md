---
title: Set up OS for developer to prevent data loss
authors: huakun
tags: [OS]
---

As a developer, I have hundreds of repos on my computer. I also need to reinstall the system every year or few months depending on the amount of garbage I added to the OS or if I broken the OS.

Data loss is a serous problem. My design goal is to prevent any possibility of losing important files even if the OS crashed, the computer is stolen, and I can reset it any time without worrying about backing up my data. (Reinstalling apps is fine for me).

The solution is simple, cloud.

My files include the following categories

1. Code
2. Videos
3. Regular documents (pdf, books, forms, notes, etc.)
4. Images

My code repos is always tracked with git and all changes must be backed up to GitHub immediately.

The code are stored in `~/Dev/`

All other files are saved in OneDrive or iCloud Drive.

There is nothing on my `~/Desktop`. I like to keep it clean.

This way I can reset my computer any time.

## Backup

Although I have all my files in the cloud, sometimes you may forgot to commit all changes to git. You may want to backup the entire projects folder to a drive, or cloud.

However, projects can take up a huge amount of space. My single rust project can easily take up 10-60GB due to large cache. This will take forever to upload to the cloud.

I wrote a small app called `devclean` (https://github.com/HuakunShen/devclean) with 2 simple feautres:

1. Scan a given directory recursively for all git repos that have uncommitted changes.
   1. You can commit the changes and push before resetting the computer.
2. Scan a given directory recursively for cache and dependency files (`node_modules`, `target`, etc.). These files can be deleted before backup. Then the project code is probably a few MB.
   1. Clearing cache and dependencies can save a lot of space and time during backup.
