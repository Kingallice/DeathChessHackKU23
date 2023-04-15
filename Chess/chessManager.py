import chess

class ChessManager:
    def __init__(self) -> None:
        """Initialized the ChessManager."""
        self.board = chess.Board()

    def getFen(self):
        """Returns the fen of the board."""
        return self.board.board_fen()

    def getTurn(self):
        """Get current player turn of the board."""
        if (self.board.fullmove_number % 2 == 0):
            return chess.BLACK
        return chess.WHITE

    def get_board(self):
        """get the board state of all pieces"""
        return self.board
    
    def getPieces(self, color=None):
        pieceArr = []
        if color == chess.WHITE:
            for x in self.board.board_fen():
                if x.isupper():
                    pieceArr.append(x)
        elif color == chess.BLACK:
            for x in self.board.board_fen():
                if x.islower():
                    pieceArr.append(x)
        return pieceArr

    def getPieceType(self, pieceChar):
        pieceChar = pieceChar.lower()
        if pieceChar == "k":
            return chess.KING
        elif pieceChar == "q":
            return chess.QUEEN
        elif pieceChar == "r":
            return chess.ROOK
        elif pieceChar == "b":
            return chess.BISHOP
        elif pieceChar == "n":
            return chess.KNIGHT
        elif pieceChar == "p":
            return chess.PAWN
        
    def getCastleRights(self, color=None):
        if color == chess.WHITE or color == chess.BLACK:
            return self.board.has_castling_rights(color)
    
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