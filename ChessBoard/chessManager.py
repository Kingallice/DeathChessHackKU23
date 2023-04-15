import chess

class ChessManager:
    __slots__ = "board"

    def __init__(self) -> None:
        self.board = chess.Board()

    def getFen(self):
        return self.board.fen

    def getTurn(self):
        if (self.board.fullmove_number % 2 == 0):
            return "BLACK"
        return "WHITE"

    def getWhite(self):
        print("white")

print(ChessManager().getTurn())