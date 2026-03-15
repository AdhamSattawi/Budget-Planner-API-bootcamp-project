# This code processes log content provided as a string, counting the number of error, warning, and info messages.


def analyze_log_content(log_content: str) -> dict:
    log_lines = log_content.strip().splitlines()
    error_count = 0
    warning_count = 0
    info_count = 0
    for line in log_lines:
        parts = line.split()
        log_level = parts[2]
        match log_level:
            case "ERROR":
                error_count += 1
            case "WARNING":
                warning_count += 1
            case "INFO":
                info_count += 1
    return log_levels_dic(error_count, warning_count, info_count)


def log_levels_dic(error: int, warning: int, info: int) -> dict:
    log_levels = {"Error": error, "Warning": warning, "Info": info}
    return log_levels


log_content = """
2024-04-29 15:45:00,089 INFO [name:starwars_engine][pid:2995] Message one
2024-04-29 15:45:05,123 WARNING [name:starwars_engine][pid:2996] Check disk space
2024-04-29 15:45:08,111 /var/log/apache2/server.access.log 172.18.0.12 - - "POST /api/command/?201dfd68-e48d-587b-e715-3ff83ef3af19 HTTP/1.1" 200
2024-04-29 15:45:10,456 ERROR [name:starwars_engine][pid:2997] Failed to start engine
2024-04-29 15:46:00,789 INFO [name:starwars_engine][pid:2998] All systems go
"""
print(analyze_log_content(log_content))
