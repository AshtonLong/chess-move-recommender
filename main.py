import chess
import chess.engine

def main():
    engine = chess.engine.SimpleEngine.popen_uci("stockfish-windows-2022-x86-64-avx2.exe")
    color = input("Enter your color (white/black): ").lower()

    if color not in ["white", "black"]:
        print("Invalid color. Choose either 'white' or 'black'.")
        return

    board = chess.Board()

    while not board.is_game_over():
        if color == "white":
            result = engine.play(board, chess.engine.Limit(time=5))
            recommended_move = result.move
            print("Stockfish recommends playing:", recommended_move.uci())
            board.push(recommended_move)

            opponent_move = input("Enter opponent's move in UCI notation: ")
            if not opponent_move:
                print("Invalid move.")
                continue
            opponent_move = chess.Move.from_uci(opponent_move)
            board.push(opponent_move)
        else:
            opponent_move = input("Enter opponent's move in UCI notation: ")
            if not opponent_move:
                print("Invalid move.")
                continue
            opponent_move = chess.Move.from_uci(opponent_move)
            board.push(opponent_move)

            result = engine.play(board, chess.engine.Limit(time=5))
            recommended_move = result.move
            print("Stockfish recommends playing:", recommended_move.uci())
            board.push(recommended_move)

    engine.quit()

if __name__ == "__main__":
    main()
