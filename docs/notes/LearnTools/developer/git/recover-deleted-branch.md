# Recover Deleted Branch in Git
```bash
git reflog --no-abbrev    # find SHA1 for the commit at the tip of deleted branch
git checkout -b <your-branch> <sha>
```

## Reference
- https://stackoverflow.com/questions/3640764/can-i-recover-a-branch-after-its-deletion-in-git

