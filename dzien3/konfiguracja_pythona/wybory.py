import click
# instalowac biblioteke click

@click.command()
@click.option("--rozmiar", type=click.Choice(['S','M','L']),default="M")
def koszulka(rozmiar):
    click.echo(f'Rozmiar {rozmiar}')

if __name__=="__main__":
    koszulka()