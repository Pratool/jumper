# How To
Useful commands.

```bash
# Make a python3 virtual environment
python3 -m venv env

# Activate that environment
source env/bin/activate

# Install pygame into that environment
pip install pygame
```

## Version Control
### Get the status
```bash
# This gets the local branch status
git status

# This gets the names of the remote branches you would sync to
git remote -v
```

### Make a branch
```bash
git checkout -b new_branch_name
```

### Commit a change
```bash
# This brings up an editor to add a commit message
git commit

# This allows you to add a commit message inline
git commit -m "Commit message here"
```

### Push changes upstream
```bash
# Usually <remote_name> is origin and the branch name is the local one you are on
git push <remote_name> <branch_name>
```
