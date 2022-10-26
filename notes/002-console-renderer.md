## Initial implementation of `ConsoleRenderer`

I physically drew on a piece of paper what the chess board would look like, and how I could go about and render each
square individually. I came across the "each square's border overlaps with each other" problem, which you'll be familiar
with if you tried to draw an X by X grid of squares using HTML and JavaScript. I then realized that the issue is much
simpler in my intended implementation: instead of thinking of the board as an 8x8 grid, I could just implement it as
17 rows of characters (8 for the ranks themselves, 9 for the enclosing borders).

The code itself is nothing out of the ordinary, I decided to store ALL characters (including the newlines) in a single
list and just print them one by one. I refactored the printing logic into an inner function for readability.

```python
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
```