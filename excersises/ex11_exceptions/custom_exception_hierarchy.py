class ConfigError(Exception):
    pass

class ConfigFileNotFoundError(ConfigError):
    pass

class ConfigParseError(ConfigError):
    pass

class ConfigValidationError(ConfigError):
    pass

def parse_config(filename: str, required_keys: list[str]) -> dict[str, str]:
    if not filename:
        raise ConfigFileNotFoundError(f"The config file '{filename}' was not found.")
    
    
    