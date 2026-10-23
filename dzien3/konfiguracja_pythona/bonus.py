import click

@click.command(params=[
    click.Option(["--imie"], prompt="Twoje imię"),        # click.Option z WIELKIEJ litery,
    click.Option(["--wiek"], type=int, prompt="Twój wiek"), # a nazwa opcji w liście
    click.Option(["--krzyk"], is_flag=True),
])
def profil(imie, wiek, krzyk):
    wiadomosc = f"{imie} ma {wiek} lat"
    click.echo(wiadomosc.upper() if krzyk else wiadomosc)

if __name__ == "__main__":
    profil()