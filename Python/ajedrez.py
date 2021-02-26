import chess

board = chess.Board()

print(board.legal_moves)

board.push_san("e4")
board.push_san("e5")
board.push_san("Bc4")
board.push_san("Nc6")
board.push_san("Qf3")
board.push_san("d6")
board.push_san("Qxf7")

print(board)

mate = board.is_checkmate()

mensaje = "Tome pal pinto, MATE CON TOMATE Y AGUACATE" if mate else "Aún no es mate"

print(mensaje)