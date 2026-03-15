# This moudle interprets and responds to various Git command strings using structural pattern matching introduced in Python 3.10.


def git_command_simulator(git_command: str) -> str:
    command_validation(git_command)
    command_parts = command_split(
        git_command
    )  # ['git', 'add'/'rm'/'commit'/'push'/'stash', "--cached"/"-m"/"filename"/"push"/"apply", "filename"]
    command = command_parts[1]
    match command:
        case "add":
            return add_command(command_parts)
        case "rm":
            return rm_command(command_parts)
        case "commit":
            return commit_command(command_parts)
        case "push":
            return push_command(command_parts)
        case "stash":
            return stash_command(command_parts)
    raise ValueError()

MESSAGE_INCLUDED = '-m' # -m in git command indicates that there is a message.

def command_split(git_command: str) -> list:
    # command structure ['git', 'add'/'rm'/'commit'/'push'/'stash'...]
    if MESSAGE_INCLUDED in git_command and "commit" in git_command:
        command_parts = git_command.split(maxsplit=3)
    elif MESSAGE_INCLUDED in git_command and "stash" in git_command:
        command_parts = git_command.split(maxsplit=4)
    else:
        command_parts = git_command.split()
    return command_parts


def command_validation(git_command: str) -> None:
    command_list = [
        "git stash push -m",
        "git stash apply",
        "git rm --cached",
        "git commit -m ",
        "git stash",
        "git push",
        "git add",
    ]
    git_command_list = git_command.split()
    if (
        not git_command_list
        or git_command_list[0] != "git"
        or len(git_command_list) <= 1
    ):
        raise ValueError("All commands must start with 'git' and a command after.")
    for command in command_list:
        if git_command.startswith(command):
            break
    else:
        raise ValueError("Unknown command")


def add_command(command_parts: list) -> str:
    length_of_command_parts = len(command_parts)
    if length_of_command_parts > 3 or length_of_command_parts == 2:  # 3 parts
        raise ValueError("please use the proper format: [git add <filename>]")
    else:
        filename = command_parts[2]
        return f"Stage all changes or specific file {filename} for the next commit."


def rm_command(command_parts: list) -> str:
    length_of_command_parts = len(command_parts)
    if length_of_command_parts > 4 or length_of_command_parts == 3:
        raise ValueError("please use the proper format: [git rm --cached <filename>]")
    if command_parts[2] != "--cached":
        raise ValueError("please use the proper format: [git rm --cached <filename>]")
    filename = command_parts[3]
    return f"Unstage file {filename} while retaining the changes in the working directory."


def commit_command(command_parts: list) -> str:
    length_of_command_parts = len(command_parts)
    if length_of_command_parts > 4 or length_of_command_parts == 3:
        raise ValueError(
            "please use the proper format: [git commit -m <commit message>]"
        )
    if command_parts[2] != MESSAGE_INCLUDED:
        raise ValueError(
            "please use the proper format: [git commit -m <commit message>]"
        )
    commit_message = command_parts[3]
    return f"Commit changes to the repository with a descriptive message {commit_message}."


def push_command(command_parts: list) -> str:
    length_of_command_parts = len(command_parts)
    if length_of_command_parts > 2:
        raise ValueError("please use the proper format: [git push]")
    else:
        return "Upload your commits to the remote repository."


def stash_command(command_parts: list) -> str:
    length_of_command_parts = len(command_parts)
    if length_of_command_parts == 2:
        return "Temporarily shelves changes in your working directory so you can work on a different task."
    stash_valid(command_parts)
    command = command_parts[2]  # git stash [command]
    match command:
        case "push":
            stash_message = command_parts[4]  # git stash [command] -m [message]
            return f"Stashes changes with a custom message {stash_message} for easy identification."
        case "apply":
            if length_of_command_parts == 3:
                return "Applies the most recently stashed changes."
            else:
                stash_name = command_parts[3]
                return (
                    f"Applies the stashed changes with the specified name {stash_name}."
                )
    raise ValueError()


def stash_valid(command_parts: list) -> None:
    length_of_command_parts = len(command_parts)
    if length_of_command_parts > 5:
        raise ValueError("please use the proper format!")
    command = command_parts[2]
    if command == "push" and command_parts[3] != MESSAGE_INCLUDED:
        raise ValueError(
            "please use the proper format: git stash push -m <stash message>"
        )
    if command == "apply" and length_of_command_parts > 4:
        raise ValueError("please use the proper format: git stash apply <stash-name>")
