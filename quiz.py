from collections import defaultdict


def reverse_list(l: list):

    """
    Reverse a list without using any built in functions

    The function should return a sorted list.

    Input l is a list which can contain any type of data.

    Time Complexity: O(n)
    
    Space Complexity: O(n)
    """

    reversed_list: list = []

    for item in l:
        # Basically: reversed_list.insert(0, item)
        reversed_list = [item] + reversed_list
    
    return reversed_list


def solve_sudoku(matrix: list[list[int]]):

    """
    Write a programme to solve 9x9 Sudoku board.

    Sudoku is one of the most popular puzzle games of all time. The goal of Sudoku is to fill a 9x9 grid with numbers so that each row, column and 3x3 section contain all of the digits between 1 and 9. As a logic puzzle, Sudoku is also an excellent brain game.

    The input matrix is a 9x9 matrix. You need to write a program to solve it.

    Time Complexity: O(9^m) where m is # of empty cell

    Space Complexity: O(n^2) where n is the size of the Sudoku board
    """

    w: int = len(matrix)
    square_w: int = w // 3
    rows: dict[int, set] = defaultdict(set)
    cols: dict[int, set] = defaultdict(set)
    squares: dict[tuple, set] = defaultdict(set) # Key: (x // square_w, y // square_w)


    def is_valid(x: int, y: int, num: int):
        # Check num is valid in its row, col and 3x3 square
        if (
            num in rows[x] or 
            num in cols[y] or 
            num in squares[(x // square_w, y // square_w)]
        ):
            return False
        return True
    

    def backtrack():
        for x in range(w):
            for y in range(w):
                if matrix[x][y] == 0:
                    # Try 1 - 9 in an empty cell
                    for i in range(1, 10):
                        if is_valid(x, y, i):
                            # Put the valid num in the cell
                            rows[x].add(i)
                            cols[y].add(i)
                            squares[(x // square_w, y // square_w)].add(i)
                            matrix[x][y] = i

                            # Move to next cell
                            if backtrack():
                                return True
                            else:
                                # Backtrack to previous cell
                                rows[x].remove(i)
                                cols[y].remove(i)
                                squares[(x // square_w, y // square_w)].remove(i)
                                matrix[x][y] = 0
                    
                    # No num is valid
                    return False
        return True


    for x in range(w):
        for y in range(w):

            if matrix[x][y] == 0:
                continue

            num = matrix[x][y]

            if not is_valid(x, y, num):
                raise ValueError("Invalid Sudoku board")
            
            rows[x].add(num)
            cols[y].add(num)
            squares[(x // square_w, y // square_w)].add(num)
    
    backtrack()

