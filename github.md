# Git Commands Reference

This document describes the use cases for essential Git commands used when working with GitHub repositories.

## Core Git Commands

### `git clone`
**Use Case:** Download a complete copy of a remote repository to your local machine.

- **When to use:** First time working with a repository, or getting a fresh copy
- **What it does:** Creates a local copy with all history, branches, and files
- **Example:** `git clone https://github.com/username/repository.git folder-name`
- **Result:** Creates a new directory with the folder name provided

### `git pull`
**Use Case:** Get the latest changes from the current branch

- **When to use:** Before starting work on a feature to get the latest changes
- **Example:** `git pull`
- **Best practice:** Always pull before pushing to avoid conflicts

### `git commit`
**Use Case:** Save your staged changes as a permanent snapshot in Git history.

- **When to use:** After making changes to send your changes to the current branch
- **What it does:** Creates a commit with your changes and a descriptive message
- **Example:** `git commit -a -m "Add user authentication feature"`
- **Best practice:** Make commits atomic (one logical change per commit)

### `git push`
**Use Case:** Upload your local commits to a remote repository (like GitHub).

- **When to use:** After committing changes that you want to share or backup
- **What it does:** Sends your local branch commits to the remote repository
- **Example:** `git push`
- **Note:** Creates the branch on remote if it doesn't exist (with `-u` flag)

### `git checkout`
**Use Case:** Switch between branches or restore files to a previous state.

- **Switch branches:** `git checkout main` or `git checkout feature-branch`
- **Create new branch:** `git checkout -b new-feature-branch`
- **Restore file:** `git checkout -- filename.txt`
- **When to use:** Navigating between different versions/features of your code



### `git fetch`
**Use Case:** Download changes from remote repository without merging them.

- **When to use:** Check what changes exist remotely before merging
- **What it does:** Updates your local repository's knowledge of remote changes
- **Example:** `git fetch origin`
- **Difference from pull:** Doesn't automatically merge changes into your working branch

## Common Workflows

### Starting Work on New Feature
1. `git pull` - Get latest changes
2. `git checkout -b new-feature` - Create feature branch
3. Make your changes
4. `git commit -a -m "Description"` - Stage changed files and commit changes
5. `git push` - Push to GitHub

### Getting Someone Else's Repository
1. `git clone <repository-url> <folder-name>` - Download repository
2. `cd folder-name` - Enter directory
3. `git checkout -b my-branch` - Create your working branch

### Staying Up to Date
1. `git fetch` - Check for remote changes
2. `git checkout main` - Switch to main branch
3. `git pull` - Get latest main branch changes
4. `git checkout your-branch` - Switch back to your branch

## Tips

- **Always commit before switching branches** to avoid losing work
- **Use descriptive commit messages** for better project history
- **Pull before push** to avoid conflicts
- **Use `git status`** frequently to see what's staged/unstaged
- **Create branches for features** to keep main branch stable