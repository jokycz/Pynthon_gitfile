def is_valid_move(x, y, board, N):
    """
    Zkontroluj, zda je tah koně platný (v rámci hranic šachovnice a neprošlé).
    """
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1


def print_board(board, N):
    """
    Vytiskni aktuální stav šachovnice.
    """

    print("    A    B    C    D    E    F    G    H")
    print("  -----------------------------------------")
    radek = 1
    for i in range(N):
        print(i+1, end=" ")
        for j in range(N):
            print(f"| {board[i][j]:2}", end=" ")
        print("|")
        print("  -----------------------------------------")
    print()


def solve_knight_tour(x, y, move_count, board, N, moves):
    """
    Použij backtracking k nalezení cesty koně.
    """
    # Pokud je move_count rovno N*N, všechny políčka byla navštívena
    if move_count == N * N:
        return True

    # Vyzkoušej všechny možné tahy koně
    for move in moves:
        next_x = x + move[0]
        next_y = y + move[1]
        if is_valid_move(next_x, next_y, board, N):
            board[next_x][next_y] = move_count
            if solve_knight_tour(next_x, next_y, move_count + 1, board, N, moves):
                return True
            # Backtracking: pokud tah nevede k řešení, resetuj pozici
            board[next_x][next_y] = -1

    return False


def knight_tour(start_x, start_y, N=8):
    """
    Vyřeš problém koně na šachovnici o rozměru N x N začínající z (start_x, start_y).
    """
    # Inicializuj šachovnici hodnotou -1
    board = [[-1 for _ in range(N)] for _ in range(N)]

    # Všechny možné tahy pro koně
    moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]

    # Začni z dané počáteční pozice
    board[start_x][start_y] = 0

    # Vyřeš problém pomocí rekurze
    if solve_knight_tour(start_x, start_y, 1, board, N, moves):
        print_board(board, N)
    else:
        print("Řešení nebylo nalezeno")


if __name__ == "__main__":
    # Požádej uživatele o souřadnice
    start_x_letter = input("Zadejte počáteční x-souřadnici (a až h): ").lower()
    start_y = int(input("Zadejte počáteční y-souřadnici (1 až 8): ")) - 1

    # Převod písmen na čísla pro osu x
    start_x = ord(start_x_letter) - ord('a')

    # Zahaj tah koně z daných souřadnic
    knight_tour(start_x, start_y)