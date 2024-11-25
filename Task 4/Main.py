import random

def create_puzzle():
    tiles = list(range(1, 16)) + [None]
    random.shuffle(tiles)
    puzzle = [tiles[i:i + 4] for i in range(0, 16, 4)]
    return puzzle

def display_puzzle(puzzle):
    print("---------------------")
    for row in puzzle:
        print("|", (" ".join([str(tile).rjust(2, ' ') + " |" if tile is not None else "   |" for tile in row])))
        print("---------------------")
    print()

def find_empty(puzzle):
    for row in range(4):
        for col in range(4):
            if puzzle[row][col] is None:
                return row, col

def is_solvable(puzzle):
    tiles = [tile for row in puzzle for tile in row if tile is not None]
    inversions = 0
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            if tiles[i] > tiles[j]:
                inversions += 1
    empty_row = find_empty(puzzle)[0]
    return (inversions % 2 == 0) == (empty_row % 2 != 0)

def is_solved(puzzle):
    expected = list(range(1, 16)) + [None]
    return [tile for row in puzzle for tile in row] == expected

def move_tile(puzzle, row, col):
    empty_row, empty_col = find_empty(puzzle)
    if abs(empty_row - row) + abs(empty_col - col) == 1:
        puzzle[empty_row][empty_col], puzzle[row][col] = puzzle[row][col], None

def main():
    puzzle = create_puzzle()
    while not is_solvable(puzzle):
        puzzle = create_puzzle()

    while not is_solved(puzzle):
        display_puzzle(puzzle)
        try:
            move = int(input("Zadejte číslo dlaždice k přesunutí (nebo 0 pro ukončení): "))
            if move == 0:
                print("Hra ukončena. Děkujeme za hraní!")
                break
            row, col = [(r, c) for r in range(4) for c in range(4) if puzzle[r][c] == move][0]
            move_tile(puzzle, row, col)
        except (ValueError, IndexError):
            print("Neplatný tah. Zkuste to prosím znovu.")

    if is_solved(puzzle):
        display_puzzle(puzzle)
        print("Gratulujeme! Vyřešili jste hlavolam!")

if __name__ == "__main__":
    main()