from rabat import cena_po_rabacie
import pytest


@pytest.mark.parametrize('a, b, oczekiwany', [
    (50, 5, 47.50),
    (100, 10, 90),
    (40,25,30),
    (100, 25, 75),
    (200,50,100),
    (400,25,300)
])
def test_cena_po_rabacie(a, b, oczekiwany):
    assert cena_po_rabacie(a, b) == oczekiwany