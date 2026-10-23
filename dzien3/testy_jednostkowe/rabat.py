# 11.1.2: Masz gotowy plik rabat.py z funkcją do przetestowania (skopiuj go do siebie)

def cena_po_rabacie(cena, procent):
    if not 0 <= procent <= 100:
        raise ValueError("Rabat musi być od 0 do 100")
    return round(cena * (1 - procent / 100), 2)

# W osobnym pliku test_rabat.py napisz testy, używając parametryzacji (@pytest.mark.parametrize):

#     jeden sparametryzowany test dla co najmniej 4 poprawnych przypadków: cenę, rabat i oczekiwany wynik wymyśl i policz sam (sprawdź też skrajne rabaty 0 i 100),
#     drugi sparametryzowany test, który sprawdza, że dla kilku niepoprawnych rabatów (spoza zakresu 0–100) leci ValueError wraz z komunikatem.

# Uruchom pytest -v i sprawdź, czy każdy przypadek pojawia się jako osobny test.


