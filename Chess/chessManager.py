import chess

class ChessManager:
    def __init__(self, fen=None) -> None:
        """Initialized the ChessManager."""
        if fen:
            self.board = chess.Board(fen)
        else:
            self.board = chess.Board()

    def getFen(self):
        """Returns the fen of the board."""
        return self.board.board_fen()

    def getTurn(self):
        """Get current player turn of the board."""
        if (self.board.fullmove_number % 2 == 0):
            return chess.BLACK
        return chess.WHITE
    
    def skipTurn(self):
        """Skips the current players turn."""
        if self.board.turn == chess.WHITE:
            self.board.turn = chess.BLACK
        else:
            self.board.turn = chess.WHITE

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
        if uciMove in (move.uci() for move in self.board.generate_legal_moves()):
            return True
        return False
    
    def isCheck(self):
        """"""
    
    def pushMove(self, uciMove=None):
        """Pushes the passed move to the board."""
        if uciMove:
            self.board.push_uci(uciMove)
            return True
        return False
    
    def revertMove(self):
        """Removes the last move from the board."""
        return self.board.move_stack.pop()
    
    def isOccupied(self, location):
        """Return True if a piece is at location, else False"""
        if self.board.piece_at(chess.parse_square(location)):
            return True
        return False

    def isWhitePawn(self,location):
        if self.board.piece_at(chess.parse_square(location)) == 'P':
            return True
        else:
            return False

    def isBlackPawn(self, location):
        if self.board.piece_at(chess.parse_square(location)) == 'p':
            return True
        else:
            return False

    def removePiece(self, location):
        """Removes and returns piece at uci location passed"""
        return self.board.remove_piece_at(chess.parse_square(location))
    
    def setPiece(self, location, pieceChar, color):
        """Places a piece of pieceType for the passed char at uci location for passed color"""
        self.board.set_piece_at(chess.parse_square(location), chess.Piece(self.getPieceType(pieceChar), color))