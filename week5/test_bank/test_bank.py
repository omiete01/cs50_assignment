from bank import value

def test_valuehello():
    assert value(" hello") == 0

def test_valueh():
    assert value("hot") == 20

def test_valueother():
    assert value("Finito") == 100

def test_case():
    assert value("hEllo") == 0

def test_phrase():
    assert value("WHat's up?") == 100