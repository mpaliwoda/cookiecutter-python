from {{cookiecutter.package_name}}.{{cookiecutter.package_name}} import hello


def test_prints_hello_world(capsys):
    hello()

    captured = capsys.readouterr()
    assert captured.out == "hello world\n"
