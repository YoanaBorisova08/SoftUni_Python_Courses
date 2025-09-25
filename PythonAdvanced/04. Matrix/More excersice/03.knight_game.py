
def knight_to_remove(knights, moves, board):
    max_idx = 0
    max_count = 0
    for idx in range(len(knights)):
        k_row, k_col = knights[idx]
        count = 0
        for move in moves:
            n_row, n_col = move(k_row, k_col)
            if 0<=n_row<n and 0<=n_col<n:
                if board[n_row][n_col] == "K":
                    count+=1
        if count > max_count:
            max_count = count
            max_idx = idx

    return max_idx if max_count>0 else None


n = int(input())
chess_board = [[char for char in input()] for _ in range(n)]
knights_pos = [[r, c] for r, row in enumerate(chess_board)
               for c, col in enumerate(row)
               if chess_board[r][c] == "K"]
removed_knights = 0

knight_moves = [
    lambda r, c: [r-1, c-2],
    lambda r, c: [r+1, c-2],
    lambda r, c: [r-1, c+2],
    lambda r, c: [r+1, c+2],
    lambda r, c: [r-2, c-1],
    lambda r, c: [r-2, c+1],
    lambda r, c: [r+2, c-1],
    lambda r, c: [r+2, c+1],
]

while knights_pos:
    index = knight_to_remove(knights_pos, knight_moves, chess_board)
    if index is not None:
        chess_board[knights_pos[index][0]][knights_pos[index][1]] = "0"
        knights_pos.pop(index)
        removed_knights += 1
    else:
        break

print(removed_knights)

