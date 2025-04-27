import time
from game import TicTacToeGame
from ai import basic_minimax, minimax_with_pruning

def display_position_guide():
    print("Position Guide:")
    print("| 0 | 1 | 2 |")
    print("| 3 | 4 | 5 |")
    print("| 6 | 7 | 8 |")
    print("\nFor Clarification this is how the board positions are numbered.")

def test_speeds():
    game_basic = TicTacToeGame()
    game_optimized = TicTacToeGame()

    print("\nTesting Basic Minimax full game with move analysis...")
    start = time.time()
    current_player = 'X'
    while game_basic.has_empty_tiles() and not game_basic.winner:
        possible_moves = {}
        for move in game_basic.available_positions():
            game_basic.place_move(move, current_player)
            eval_result = basic_minimax(game_basic, 'O' if current_player == 'X' else 'X')
            game_basic.tiles[move] = ' '
            game_basic.winner = None
            possible_moves[move] = eval_result['score']

        print(f"\n{current_player}'s turn. Evaluating moves:")
        for move, score in possible_moves.items():
            print(f"Tile {move}: {score}")

        if current_player == 'X':
            chosen_move = max(possible_moves, key=possible_moves.get)
        else:
            chosen_move = min(possible_moves, key=possible_moves.get)

        game_basic.place_move(chosen_move, current_player)
        print(f"\n{current_player} moves to {chosen_move}")
        game_basic.display_board()
        print()

        current_player = 'O' if current_player == 'X' else 'X'

    elapsed = time.time() - start
    print(f"Game Over! Winner: {game_basic.winner if game_basic.winner else 'Draw'} | Time: {elapsed:.6f} seconds")

    print("\nTesting Minimax with Alpha-Beta Pruning full game with move analysis...")
    start = time.time()
    current_player = 'X'
    while game_optimized.has_empty_tiles() and not game_optimized.winner:
        possible_moves = {}
        for move in game_optimized.available_positions():
            game_optimized.place_move(move, current_player)
            eval_result = minimax_with_pruning(game_optimized, 'O' if current_player == 'X' else 'X')
            game_optimized.tiles[move] = ' '
            game_optimized.winner = None
            possible_moves[move] = eval_result['score']

        print(f"\n{current_player}'s turn. Evaluating moves:")
        for move, score in possible_moves.items():
            print(f"Tile {move}: {score}")

        if current_player == 'X':
            chosen_move = max(possible_moves, key=possible_moves.get)
        else:
            chosen_move = min(possible_moves, key=possible_moves.get)

        game_optimized.place_move(chosen_move, current_player)
        print(f"\n{current_player} moves to {chosen_move}")
        game_optimized.display_board()
        print()

        current_player = 'O' if current_player == 'X' else 'X'

    elapsed = time.time() - start
    print(f"Game Over! Winner: {game_optimized.winner if game_optimized.winner else 'Draw'} | Time: {elapsed:.6f} seconds")

def play_vs_ai():
    game = TicTacToeGame()
    player_symbol = input("Choose your symbol (X goes first, O goes second): ").upper()
    ai_symbol = 'O' if player_symbol == 'X' else 'X'
    current_player = 'X'

    while game.has_empty_tiles() and not game.winner:
        game.display_board()
        if current_player == player_symbol:
            move = None
            while move not in game.available_positions():
                try:
                    move = int(input(f"Your move (0-8): "))
                    if move not in game.available_positions():
                        print("Tile occupied or invalid! Try again.")
                except ValueError:
                    print("Invalid input! Enter a number between 0 and 8.")
            game.place_move(move, player_symbol)
        else:
            print(f"\nAI ({ai_symbol}) is thinking...")
            move_info = minimax_with_pruning(game, ai_symbol)
            game.place_move(move_info['choice'], ai_symbol)
            print(f"AI moved to {move_info['choice']}")

        current_player = 'O' if current_player == 'X' else 'X'

    game.display_board()
    if game.winner == player_symbol:
        print("Congratulations! You win!")
    elif game.winner == ai_symbol:
        print("You lost! AI wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    display_position_guide()

    test_speeds()

    play_choice = input("\nWould you like to play against AI? (y/n): ").lower()
    if play_choice == 'y':
        play_vs_ai()
    else:
        print("Goodbye!")
