import chess

posiciones = {
    "peon" : "8/8/8/8/8/5p2/4P3/8 w - - 0 1",
    "alfil" : "8/8/8/3B4/8/8/8/8 w - - 0 1",
    "caballo" : "8/8/8/3N4/8/8/8/8 w - - 0 1",
    "torre" : "8/8/8/3R4/8/8/8/8 w - - 0 1",
    "dama" : "8/8/8/3Q4/8/8/8/8 w - - 0 1",
    "rey" : "8/8/8/3K4/8/8/8/8 w - - 0 1"
}

pieza = input("Cuál pieza quiere aprender?\n").lower()

tablero = chess.Board(posiciones[pieza])

print(tablero)

jugadas_validas = []

for m in tablero.legal_moves:
    m = str(m)[2:]
    jugadas_validas.append(m)

print("Su", pieza, "puede moverse a", jugadas_validas)
