# This Module Extract Key-Value Pairs from Logs


def key_value_extract(log: str, key: str) -> str:
    length_of_key = len(key)
    key_index = log.find(f"[{key}:")
    value_start = key_index + length_of_key + 1  # 1 is the ":" in key-vale pairs
    value_end = log.find("]", key_index)  # every key-value pair sorunded by "[]"
    value = log[value_start:value_end].strip()
    return value
