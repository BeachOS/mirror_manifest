# BeachOS Mirror Manifest

## Using the mirror to sync

Usage: `repo init -u https://gitlab.com/beachos/mirror_manifest --mirror`

Once the mirror is synced, you can then run `repo init -u /path/to/mirror/beachos/manifest.git -b $BRANCHNAME` and sync normally.

If you want to sync the source quickly but want it to be up-to-date without syncing the mirror every time, then run `repo init -u https://gitlab.com/beachos/manifest -b $BRANCHNAME --reference=/path/to/mirror/`. This will init the new repo and fetch all the (available) data from the mirror, but will fallback to GitLab if something is missing in the mirror.

## Updating the mirror manifest

To update the mirror, use the `mirror-regen.py` script.  
Please make sure you set the environment variable before using the script:

`GITLAB_TOKEN` contains a GitLab Personal Access Token  
  
To set these environment variables, run these commands in your terminal window:  

```
export GITLAB_TOKEN="<Your Token>"
```

(You can obtain a GitLab Personal Access Token [here](https://gitlab.com/profile/personal_access_tokens))
