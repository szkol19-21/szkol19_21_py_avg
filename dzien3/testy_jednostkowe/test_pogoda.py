from unittest.mock import patch
from pogoda import aktualna_temperatura, aktualna_temp
import requests 

def test_temperatura():
    with patch('pogoda.requests.get') as mock_get:
        mock_get.return_value.json.return_value = {"temp": 20}
        wynik = aktualna_temperatura("warszawa")
        assert wynik == 20
        mock_get.assert_called_once() # sprawdza, czy zostalo wywolane raz 

# Po co sa mocki -> Testy maja byc szybkie, powtarzalne, niezalezne. 

def test_timeout():
    with patch('pogoda.requests.get',side_effect=requests.Timeout):
        assert aktualna_temp("warszawa") is None 