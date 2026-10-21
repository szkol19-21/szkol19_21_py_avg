# # reczne
# 10. Konfiguracja Pythona: Reczne tworzenie wirtualnego srodowiska

# 1. Bierzemy folder w ktorym chcemy wirtualke
# 2. uzywamy komendy zeby sie dostac:
#  windows: cd C:\Users\labuser\Desktop\szkolenie\dzien3\pakiety
#  linux: cd /home/labuser/Pulpit/szkolenie/dzien3/pakiety
#  macos: cd /Users/labuser/Desktop/szkolenie/dzien3/pakiety
# 3. python -m venv venv
# 4. wejsc na srodowisko za pomoca komendy
# windows --> .\venv\Scripts\Activate
# linux/macos
# source ./venv/bin/activate
# 5. pip install click
# 6. Czy paczka znajduje sie w venvie
# pip freeze
# 7. Po skonczonej pracy z venvem zapisac sobie liste paczek
# pip freeze > requirements.txt
# 8. pip uninstall click
# 9. pip install -r requirements.txt
# Uninstall i install tylko pokazuja mechanizm. W praktyce requirements.txt sluzy do
# odtworzenia srodowiska: kasujemy venv albo przechodzimy na inny komputer,
# robimy nowy venv (krok 3), aktywujemy go (krok 4) i wtedy pip install -r requirements.txt

# 10. pip install pandas==2.1.1 konkretna wersja

# Folderu venv nie wrzucamy do gita, dopisujemy go do pliku .gitignore:
# venv/
# Do repo idzie tylko requirements.txt

# 11. jesli chcemy wyjsc z venva
# deactivate
