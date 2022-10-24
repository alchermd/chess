import pprint


class GameRenderer:
    def render(self, *, board=[]):
        raise NotImplementedError("Must be implemented by a subclass.")


class ConsoleRenderer(GameRenderer):
    """
    Renders the game via console.
    """

    def render(self, *, board=[]):
        pprint.pprint(board)
