# Contributing

Thanks for thinking of contributing to this project 🙌

This is a guide to help you get started, and an outline for the coding standards and processes to follow. PRs must be approved by at least one code owner before being merged.

## Prerequisites

Install [Git](https://git-scm.com/downloads)  
Install [Python](https://www.python.org/downloads/)

## Running the project

Run the following in your terminal or command line

1. `git clone https://github.com/JohnnyRottin/Gubber.git`
2. `cd Gubber`
3. `python Main.py`

## Performing feature or defect work

### Make sure you are where you think you are in your file system by running

1. `git status` or `pwd` or both.
2. Ensure you have the lastest changes with `git pull origin main`

Note: If you have existing changes in your work space, you may need to stash your changes with `git stash` before running `git pull origin main`. Later, you can unstash your changes with `git stash pop`. This may introduce merge conflicts that will need to be resolved before commiting new work

[Resolve merge conflicts on the command line](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line)  
[Resolve merge conflicts in vscode](https://code.visualstudio.com/docs/sourcecontrol/overview#_merge-conflicts)

### Checkout a new feature or defect branch

the `-b` flag is for creating a new branch

1. `git checkout -b <branch-name>`  
   e.g. `git checkout -b new-game` or `git checkout -b bug-fix`

Then make changes to the files... for example, the `Main.py` file.

### Stage changes for commit

1. `git status` - to see the files that can be staged
2. `git add <file>`  
   e.g `git add Main.py`

### Commit your changes

the `-m` flag is for setting the commit message in the command

1. `git commit -m <commit-message>`  
   e.g. `git commit -m "Add new game"`

Note: It's good practice to put commit messages in present tense and
keep them descriptive about what the commit actually changes.

Note: If you just run `git commit` without the `-m` flag and commit message, [vim](https://www.vim.org/) will open
and you'll need to type and save your commit message there. In this case

1. Type the commit
2. Press 'Esc' to exit 'Insert' mode.
3. Then type `:wq` to write your changes and quit the vim program.

### Push your changes up to a remote repository

To check what remote branches there are, run:  
`git remote -v`

Then, to push to a remote:
`git push -u origin <branch-name>`  
e.g. `git push -u origin new-game` or `git push -u origin bug-fix`

The name of the branch should be the branch you have commit work on.

Once your work has been commited and your branch is up on GitHub, you are ready to open a pull request! 🎉🎉🎉
