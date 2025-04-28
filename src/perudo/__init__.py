from argparse import ArgumentParser
from collections import Counter
from rich.console import Console
from rich.progress import track
from rich.table import Table

from .sprites import main as game
from .perudo import Perudo, Player

__all__ = ["game", "Perudo", "Player"]


def sim():
    parser = ArgumentParser()
    parser.add_argument(
        "-n", "--num_games", help="Number of games, default: 10", type=int, default=10
    )
    parser.add_argument(
        "-p", "--num_players", help="Number of players, default: 5", type=int, default=5
    )
    parser.add_argument(
        "-d", "--num_dice", help="Number of dice, default: 5", type=int, default=5
    )
    config = parser.parse_args()

    winners = []

    for _ in track(range(config.num_games), description="Simulating..."):
        p = Perudo(players=config.num_players, dice=config.num_dice)
        state = []
        while isinstance(state, list):
            state = p()

        winners.append(state)

    table = Table(title=f"Perudo Winners, {config.num_games} Games")

    table.add_column("ID", justify="right", style="cyan")
    table.add_column("Wins", justify="right", style="magenta")
    table.add_column("Win Rate", justify="right", style="green")

    for player, wins in Counter(winners).items():
        table.add_row(str(player), str(wins), str(wins / config.num_games))

    console = Console()
    console.print(table)
