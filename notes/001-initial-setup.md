## Initial Setup

My initial thought is to abstract away the Chess functionality as an importable module. The goal is not to publish it
as a package, but rather work on it with a API/consumer mindset. The simplest way to do this is to have the game logic
sit in its own package and be called by a consumer -- the `main.py` file.

The `chess` module doesn't have any structural decisions made so far, everything is placed as I see fit. It started with
the `game.py` file containing the main `Game` class. I then write out its methods by thinking out loud how a game of
Chess would behave:

1. The board and pieces are set up
2. The game starts
3. A player makes a move
4. That move is checked for validity
5. The board and piece configuration (i.e. game state) is updated to reflect the move
6. Repeat until the game ends

The pseudocode above lead me to the basic skeleton below:

```python
class Game:
    """
    Represents a game of chess.
    """
    moves = []

    def __init__(self, *args, **kwargs):
        pass

    def start(self):
        """
        Main game loop.
        """
        while True:
            try:
                self.display_board()
                self.poll_for_input()
            except (KeyboardInterrupt, EOFError):
                break

    def poll_for_input(self):
        """
        Waits and accepts the user's next move.
        """
        current_move = input()
        self.validate_move(move=current_move)
        self.moves.append(current_move)

    def display_board(self):
        pass

    def validate_move(self, *, move: str):
        """
        Check's the given move's validity against the current game state.
        """
        pass
```

## Game State

A 2D list is the first thought that came to my mind when I'm considering how I'd track the game state. But how should I
represent a Chess piece? A dictionary could be the simplest solution, but a `Piece` class hierarchy looks appealing in
terms of mapping the mental model of a Chess game into code.

I decided to design the `Piece` parent class to accept a color in which it is to be associated with. It is then
subclassed by the actual pieces (pawns, rooks, knights, etc). Whether it is better to structure the pieces with
hardcoded colors (`Pawn(color="WHITE")` vs `WhitePawn()`) is yet to be determined.

## Displaying the board

I just want to see the game state graphically, so I opted to use `pprint`. I then made the decision to abstract
UI part of the code into _renderers_, in which I moved the `pprint` part to a `ConsoleRenderer`. This looks like a
classic case of premature optimization, but it felt right at the time. Perhaps it could be helpful when I try to write
tests for the game down the line?