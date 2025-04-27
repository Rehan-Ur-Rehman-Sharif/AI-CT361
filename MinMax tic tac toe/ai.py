def basic_minimax(board, player):
    opponent = 'O' if player == 'X' else 'X'

    if board.winner == opponent:
        return {'score': 1 if opponent == 'X' else -1}
    elif not board.has_empty_tiles():
        return {'score': 0}

    moves = []
    for move in board.available_positions():
        board.place_move(move, player)
        result = basic_minimax(board, opponent)
        board.tiles[move] = ' '
        board.winner = None
        moves.append({'choice': move, 'score': result['score']})

    if player == 'X':
        best = max(moves, key=lambda x: x['score'])
    else:
        best = min(moves, key=lambda x: x['score'])

    return best

def minimax_with_pruning(board, player, alpha=float('-inf'), beta=float('inf')):
    opponent = 'O' if player == 'X' else 'X'

    if board.winner == opponent:
        return {'score': 1 if opponent == 'X' else -1}
    elif not board.has_empty_tiles():
        return {'score': 0}

    best_move = None
    if player == 'X':
        max_eval = float('-inf')
        for move in board.available_positions():
            board.place_move(move, player)
            result = minimax_with_pruning(board, opponent, alpha, beta)
            board.tiles[move] = ' '
            board.winner = None
            if result['score'] > max_eval:
                max_eval = result['score']
                best_move = move
            alpha = max(alpha, result['score'])
            if beta <= alpha:
                break
        return {'choice': best_move, 'score': max_eval}
    else:
        min_eval = float('inf')
        for move in board.available_positions():
            board.place_move(move, player)
            result = minimax_with_pruning(board, opponent, alpha, beta)
            board.tiles[move] = ' '
            board.winner = None
            if result['score'] < min_eval:
                min_eval = result['score']
                best_move = move
            beta = min(beta, result['score'])
            if beta <= alpha:
                break
        return {'choice': best_move, 'score': min_eval}
