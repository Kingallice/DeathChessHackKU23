import chess

class ChessManager:
    def __init__(self) -> None:
        self.board = chess.Board()

    def getFen(self):
        return self.board.fen

    def getTurn(self):
        if (self.board.fullmove_number % 2 == 0):
            return "BLACK"
        return "WHITE"
    
    def isLegalMove(self, uciMove=None):
        if uciMove in self.board.generate_legal_moves:
            return True
        return False
    
    def pushMove(self, uciMove=None):
        if uciMove:
            self.board.push_uci(uciMove)
            return True
        return False

print(ChessManager().getTurn())