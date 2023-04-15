import chess

class ChessManager:
    def __init__(self) -> None:
        """Initialized the ChessManager."""
        self.board = chess.Board()

    def getFen(self):
        """Returns the fen of the board."""
        return self.board.fen

    def getTurn(self):
        """Get current player turn of the board."""
        if (self.board.fullmove_number % 2 == 0):
            return "BLACK"
        return "WHITE"
    
    def isLegalMove(self, uciMove=None):
        """Return True if passed move is legal."""
        if uciMove in self.board.generate_legal_moves:
            return True
        return False
    
    def pushMove(self, uciMove=None):
        """Pushes the passed move to the board."""
        if uciMove:
            self.board.push_uci(uciMove)
            return True
        return False
    
    def revertMove(self):
        """Removes the last move from the board."""
        return self.board.move_stack.pop()