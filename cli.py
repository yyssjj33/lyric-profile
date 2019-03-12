import click
from api.lyrics import get_lyrics_and_analyse


@click.command()
@click.option('--name', required=True, help='the name of the singer')
def run(name):
    res = get_lyrics_and_analyse(name)
    print("{}'s song is more {}".format(name, res))


if __name__ == '__main__':
    run()
