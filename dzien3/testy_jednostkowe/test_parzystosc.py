from parzystosc import parzystosc_sprawdz
import pytest

def test_parzystosc():
    assert parzystosc_sprawdz(2) == True
    assert parzystosc_sprawdz(3) == False

def test_parzystosc_string():
    with pytest.raises(ValueError, match='nie jest liczba'):
        assert parzystosc_sprawdz('blabla')