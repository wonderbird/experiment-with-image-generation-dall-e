from dall_e.main import hello


def test_main():
    assert hello() == "Hello, world!"
