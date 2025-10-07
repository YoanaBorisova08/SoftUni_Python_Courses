import tkinter as tk
from tkinter import messagebox

class InvalidColumnError(Exception):
    pass

class FullColumnError(Exception):
    pass

def create_matrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def place_player_choice(ma, c, player_n):
    for r in range(len(ma)-1, -1, -1):
        if ma[r][c] == 0:
            ma[r][c] = player_n
            return r, c
    raise FullColumnError

def is_player_num(ma, r, c, player_n):
    try:
        return ma[r][c] == player_n
    except IndexError:
        return False

def is_vertical_winner(ma, r, c, player_n, slots):
    return all([is_player_num(ma, r+idx, c, player_n) for idx in range(slots)])

def is_horizontal_win(ma, r, c, player_n, slots):
    filled = 1
    for idx in range(1, slots):
        if is_player_num(ma, r, c+idx, player_n):
            filled+=1
        else:
            break

    for idx in range(1, slots):
        if is_player_num(ma, r, c-idx, player_n):
            filled+=1
        else:
            break

    return filled >= slots


def is_right_diagonal_win(ma, r, c, player_n, slots):
    filled = 1
    for idx in range(1, slots):
        if is_player_num(ma, r - idx, c + idx, player_n):
            filled+=1
        else:
            break

    for idx in range(1, slots):
        if is_player_num(ma, r + idx, c - idx, player_n):
            filled+=1
        else:
            break

    return filled >= slots

def is_left_diagonal_win(ma, r, c, player_n, slots):
    filled = 1
    for idx in range(1, slots):
        if is_player_num(ma, r + idx, c + idx, player_n):
            filled += 1
        else:
            break

    for idx in range(1, slots):
        if is_player_num(ma, r - idx, c - idx, player_n):
            filled += 1
        else:
            break

    return filled >= slots

def is_winner(ma, r, c, player_n, slots):
    return any([
        is_vertical_winner(ma, r, c, player_n, slots),
        is_horizontal_win(ma, r, c, player_n, slots),
        is_left_diagonal_win(ma, r, c, player_n, slots),
        is_right_diagonal_win(ma, r, c, player_n, slots)
    ])

def update_ui(labels, r, c, player_n):
    color = "red" if player_n == 1 else "beige"
    labels[r][c].config(bg=color)

def reset_game(ma, rows, cols, labels):
    for r in range(rows):
        for c in range(cols):
            ma[r][c] = 0
            labels[r][c].config(bg="white")

def handle_column_click(ma, labels, col_num, player_num, counter, rows, cols, slots_to_win):
    try:
        row, col = place_player_choice(ma, col_num, player_num)
        update_ui(labels, row, col, player_num)
        if is_winner(ma, row, col, player_num, slots_to_win):
            messagebox.showinfo("Game over", f"The winner is Player {player_num}!")
            reset_game(ma, rows, cols, labels)
            return 1, 0

        counter += 1
        if counter == rows * cols:
            messagebox.showinfo("Game over", "It's a draw!")
            reset_game(ma, rows, cols, labels)
            return 1, 0

        return 2 if player_num == 1 else 1, counter

    except FullColumnError:
        messagebox.showerror("Invalid move", "This column is full! Select another!")


    return player_num, counter

def create_ui(root, rows, cols, slots_to_win):
    matrix = create_matrix(rows, cols)
    labels = [[tk.Label(root, text=" ", width=4, height=2, bg="white", relief="solid") for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            labels[r][c].grid(row=r+1, column=c)

    game_state = {
        "player_num": 1,
        "counter": 0,
    }

    def on_click(col_num, state):
        state["player_num"], state["counter"] = handle_column_click(matrix,
                                                                    labels,
                                                                    col_num,
                                                                    state["player_num"],
                                                                    state["counter"],
                                                                    rows,
                                                                    cols,
                                                                    slots_to_win)

    buttons = [tk.Button(root,
                         text="↓",
                         width=4,
                         height=2,
                         bg = "pink",
                         command=lambda c_idx=c: on_click(c_idx, game_state))
               for c in range(cols)]
    for c, button in enumerate(buttons):
        button.grid(row=0, column=c)

    tk.Button(root,
              text="Reset",
              bg = "pink",
              command=lambda: reset_game(matrix, rows, cols, labels)).grid(row=rows+1, column=cols//2)

def start_game():
    root = tk.Tk()
    root.title("Connect Four")
    rows, cols, slots_to_win = 6, 7, 4
    create_ui(root, rows, cols, slots_to_win)
    root.mainloop()

if __name__ == '__main__':
    start_game()

