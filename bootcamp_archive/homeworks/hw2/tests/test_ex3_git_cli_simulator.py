import pytest
from solution.ex3_git_cli_simulator import git_command_simulator


@pytest.mark.parametrize("command, expected", 
    [("git add python.py", "Stage all changes or specific file python.py for the next commit."),
    ("git commit -m my message is here", "Commit changes to the repository with a descriptive message my message is here."),
    ("git rm --cached python.py", "Unstage file python.py while retaining the changes in the working directory."),
    ("git push", "Upload your commits to the remote repository."),
    ("git stash", "Temporarily shelves changes in your working directory so you can work on a different task."),
    ("git stash push -m my message for you", "Stashes changes with a custom message my message for you for easy identification."),
    ("git stash apply", "Applies the most recently stashed changes."),
    ("git stash apply mypython", "Applies the stashed changes with the specified name mypython."),
    ]                     
)

def test_git_command_simulator(command, expected):
    assert git_command_simulator(command) == expected

def test_invalid_input():
    invalid_command = 'git'
    with pytest.raises(ValueError):
        git_command_simulator(invalid_command)

def test_empty_input():
    invalid_command = ''
    with pytest.raises(ValueError):
        git_command_simulator(invalid_command)