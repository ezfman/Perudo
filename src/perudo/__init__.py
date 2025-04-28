from .sprites import main as game
from .perudo import Perudo, Player

__all__ = ["game", "Perudo", "Player"]


def sim():
    p = Perudo()
    state = []
    while isinstance(state, list):
        state = p()
    print(f"Winner is {state[0]}")
