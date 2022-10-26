class GameRenderer:
    def render(self, *, board: list):
        raise NotImplementedError("Must be implemented by a subclass.")


class ConsoleRenderer(GameRenderer):
    """
    Renders the game via console.
    """

    def render(self, *, board: list):
        """
        Renders the board as 17 rows of characters: 8 for the actual ranks, 9 for the enclosing borders.
        """

        def render_row(chars, end=""):
            for char in chars:
                print(char, end=end)

        horizontal_borders = [" --" for _ in range(8)]

        for x, row in enumerate(board):
            render_row([
                *horizontal_borders,
                "\n",
                *["|" + str(square) if square else "|  " for square in row],
                "|",
                "\n",
            ])

        render_row([*horizontal_borders, "\n"])
