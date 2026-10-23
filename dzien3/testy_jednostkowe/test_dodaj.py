# Testy jednostkowe
# 1. pobrac pytest biblioteke oraz pytest-cov
# 2. obok modulu(w tym przypadku najwygodniej utworzyc plik do testowania)
# 3. pytest szuka wszystkich plikow w lokalizacji ktore maja czlon test_
# 4. jak jest nazwa testy_ t*sty_ t3sty_ to sa zle wywolania i pytest je pominie

# Testy, ktore sprawdzaja automatycznie, czy dany fragment kodu dziala poprawnie.
# zwykle male funkcje


from dodaj import dodawanie, podziel, Konto
import pytest

def test_dodawanie():
    assert dodawanie(2, 3) == 5
    assert dodawanie(-1,1) == 0

# test celowo nie przechodzi --> pokazuje jak wyglada blad w pytest
def test_zly():
    assert dodawanie(2, 2) == 5

def test_dodawanie_stringi():
    assert dodawanie("a","b") == "ab"

def test_podziel():
    assert podziel(10, 2) == 5

def test_podziel_przez_zero():
    with pytest.raises(ValueError):
        podziel(10, 0)

def test_podziel_komunikat():
    with pytest.raises(ValueError, match='przez zero'):
        podziel(10, 0)

# Uruchomiony w terminalu w folderze z testami
# pytest --> wszystkie testy
# pytest -v --> to samo, ale z nazwa kazdego testu 
# pytest test_dodaj.py --> sprawdzenie tylko jednego modulu z testami
# pytest -k 'podziel' --> tylko testy z 'podziel' w nazwie
# pytest -x --> zatrzymuje sie po pierwszym bledzie 


# fixture --> Przygtowanie danych wspolnych dla wielu testow. Test
# dostaje fixture jako parametr staly do test


@pytest.fixture
def konto():
    return Konto(100)

def test_wplata(konto):
    konto.wplac(50)
    assert konto.saldo == 150

def test_saldo_startowe(konto):
    assert konto.saldo == 100 # swieze konto 

# Pulapka testow jednostkowych 


def test_float():
    assert dodawanie(0.2, 0.1) == 0.3

def test_float_ok():
    assert dodawanie(0.2, 0.1) == pytest.approx(0.3)


# Parametryzacja
@pytest.mark.parametrize('a, b, oczekiwany',[
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300)
])

def test_dodaj_wiele(a , b, oczekiwany):
    assert dodawanie(a, b) == oczekiwany


# Uruchom testy z raportem pokrycia
# pytest --cov=dodaj

# pytest --cov=dodaj --cov-report=html