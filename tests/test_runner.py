from kaxi import Runner


def test_file_exists_pipeline():
    runner = Runner.from_yaml("tests/resources/exists.yaml")
    assert isinstance(runner, Runner)
    runner.execute()
