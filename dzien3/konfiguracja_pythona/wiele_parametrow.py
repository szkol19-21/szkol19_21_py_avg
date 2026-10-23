import click
# instalowac biblioteke click

@click.command()
@click.option("--imie",prompt='Twoje imie',help='Imie uzytkownika')
@click.option("--wiek",type=int,prompt='Twoj wiek',help='Wiek uzytkownika')
@click.option('--krzyk', is_flag=True, help='Wypisz wielkimi literami')
def profil(imie, wiek, krzyk):
    """Wyswietla profil uzytkownika"""
    wiadomosc = f'{imie} ma {wiek} lat'
    if krzyk:
        wiadomosc = wiadomosc.upper()
    click.echo(wiadomosc)



if __name__=="__main__":
    profil()# 10.3.1: Napisz program pizza.py z opcją 
# --rozmiar (tylko big, bigXL lub Small, wymagana) i flagą 
# --na-wynos. Ma wypisać np. 
# Pizza L, na wynos albo Pizza M, na miejscu.