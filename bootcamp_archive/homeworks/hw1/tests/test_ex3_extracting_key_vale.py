from solution.ex3_extracting_key_value import key_value_extract

def test_key_value():
    key = "account"
    log_line = "2024-04-29 15:45:00,089 INFO [name:starwars_engine.spaceship_manager.tasks][pid:2995][uuid:20ebf460-dcdf-4b1f-abf1-7517ef3f63c2][process:run_services_if_needed_wrapper][function:run_services_if_needed][account:519][GamePlay:400004380] GamePlay's version is at least 'new' (5.2.0)."
    assert key_value_extract(log_line, key) == "519"

def test_empty_value():
    key = "account"
    log_line = "2024-04-29 15:45:00,089 INFO [name:starwars_engine.spaceship_manager.tasks][pid:2995][uuid:20ebf460-dcdf-4b1f-abf1-7517ef3f63c2][process:run_services_if_needed_wrapper][function:run_services_if_needed][account:][GamePlay:400004380] GamePlay's version is at least 'new' (5.2.0)."
    assert key_value_extract(log_line, key) == ""

def test_value_with_spaces():
    key = "account"
    log_line = "2024-04-29 15:45:00,089 INFO [name:starwars_engine.spaceship_manager.tasks][pid:2995][uuid:20ebf460-dcdf-4b1f-abf1-7517ef3f63c2][process:run_services_if_needed_wrapper][function:run_services_if_needed][account:  520  ][GamePlay:400004380] GamePlay's version is at least 'new' (5.2.0)."
    assert key_value_extract(log_line, key) == "520"