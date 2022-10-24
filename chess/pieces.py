class Piece:
    """Represents a Chess piece."""
    color: str

    def __init__(self, *args, **kwargs):
        self.color = kwargs["color"]


class Pawn(Piece):
    def __repr__(self):
        return f"{self.color[0]}P"


class Knight(Piece):
    def __repr__(self):
        return f"{self.color[0]}N"


class Bishop(Piece):
    def __repr__(self):
        return f"{self.color[0]}B"


class Rook(Piece):
    def __repr__(self):
        return f"{self.color[0]}R"


class Queen(Piece):
    def __repr__(self):
        return f"{self.color[0]}Q"


class King(Piece):
    def __repr__(self):
        return f"{self.color[0]}K"
