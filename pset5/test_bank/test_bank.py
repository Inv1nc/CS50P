from bank import value


def test_casesensitivity():
    assert value("hello") == 0
    assert value("Hello") == 0


def test_firstletter():
    assert value("hero") == 20
    assert value("Hai Friend") == 20


def test_failure():
    assert value("Nothing bro") == 100
    assert value("1 customer of the year") == 100