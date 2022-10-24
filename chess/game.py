from datetime import datetime

from chess.pieces import Rook, Knight, Bishop, Queen, King, Pawn
from chess.renderers import ConsoleRenderer, GameRenderer


class Game:
    """
    Represents a game of chess.
    """

    BLACK = "Black"
    WHITE = "White"

    color_to_move: str
    current_move_count: int
    moves: list
    board: list
    renderer: GameRenderer

    def __init__(self, *, color_to_move=WHITE, current_move_count=1, moves=[], renderer=ConsoleRenderer()):
        self.color_to_move = color_to_move
        self.current_move_count = current_move_count
        self.moves = moves
        self.board = generate_starting_board()
        self.renderer = renderer

    def start(self):
        """
        Main game loop.
        """
        print(f"Starting game on {datetime.now()}")

        while True:
            try:
                self.display_board()
                self.poll_for_input()
            except (KeyboardInterrupt, EOFError):
                print("\nMove List:")
                print(self.moves)
                break

    def poll_for_input(self):
        """
        Waits and accepts the user's next move.
        """
        current_move = input(f"(Move #{self.current_move_count}) {self.color_to_move} to move: ")
        self.validate_move(move=current_move)
        self.setup_next_ply()
        self.moves.append(current_move)

    def display_board(self):
        """
        Display the current game state using the defined renderer.
        """
        self.renderer.render(board=self.board)

    def setup_next_ply(self):
        """
        Adjust internal variables to prepare for the next ply (half-move).
        """
        if self.color_to_move == self.WHITE:
            self.color_to_move = self.BLACK
        else:
            self.color_to_move = self.WHITE
            self.current_move_count += 1

    def validate_move(self, *, move: str):
        """
        Check's the given move's validity against the current game state.
        """
        print(f"Validating {self.current_move_count}.{move} (TODO: Implement me!)")


def generate_starting_board() -> list:
    return [
        [
            Rook(color=Game.BLACK),
            Knight(color=Game.BLACK),
            Bishop(color=Game.BLACK),
            Queen(color=Game.BLACK),
            King(color=Game.BLACK),
            Bishop(color=Game.BLACK),
            Knight(color=Game.BLACK),
            Rook(color=Game.BLACK),
        ],
        [Pawn(color=Game.BLACK) for _ in range(8)],
        [None for _ in range(8)],
        [None for _ in range(8)],
        [None for _ in range(8)],
        [None for _ in range(8)],
        [Pawn(color=Game.WHITE) for i in range(8)],
        [
            Rook(color=Game.WHITE),
            Knight(color=Game.WHITE),
            Bishop(color=Game.WHITE),
            Queen(color=Game.WHITE),
            King(color=Game.WHITE),
            Bishop(color=Game.WHITE),
            Knight(color=Game.WHITE),
            Rook(color=Game.WHITE),
        ],
    ]
