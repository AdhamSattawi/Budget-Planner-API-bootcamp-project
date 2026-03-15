from solution.ex1_parsing_logs import pid_find

def test_logs_pid_finder():
    logs = "2024-04-29 15:45:00,089 INFO [name:starwars_engine.spaceship_manager.tasks][pid:2995][uuid:20ebf460-dcdf-4b1f-abf1-7517ef3f63c2][process:run_services_if_needed_wrapper][function:run_services_if_needed][account:519][GamePlay:400004380] GamePlay's version is at least 'new' (5.2.0)."
    expected_pid = "2995"
    assert pid_find(logs) == expected_pid