def pid_find(log: str) -> str:
    log = log.casefold()  # lowercasing and remove all case distinctions in the logs.
    start = log.index("pid") + 4
    end = start + 4
    pid = log[start:end]
    return pid
