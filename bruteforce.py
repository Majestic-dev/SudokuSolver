def find_square_index(row: int, col: int) -> int:
    return 3 * ((row - 1) // 3) + ((col - 1) // 3) + 1

def bruteforce(board: dict) -> dict:

    # see which cells we have to edit
    empty_cells = []

    for r in range(1, 10):
        for c, num in enumerate(board["rows"][r]):
            if num == 10:
                empty_cells.append((r, c+1))
    
    # See how many cells we have edited
    cell_index = 0

    # Create a dict which will store all edited cells
    tried_cells = {}

    while cell_index < len(empty_cells):
        row, col = empty_cells[cell_index]
        square = find_square_index(row = row, col = col)
        
        # Set all the cells which need to be edited to 1
        if (row, col) not in tried_cells:
            tried_cells[(row, col)] = 1

        # Get the number of the cell we're going to edit
        num = tried_cells[(row, col)]

        # Have we found the cell? Will be set to True if yes, otherwise we backtrack
        found = False

        while num <= 9:
            if (num not in board["rows"][row]
                and num not in board["columns"][col]
                and num not in board["squares"][square]):

                board["rows"][row][col - 1] = num
                board["columns"][col][row - 1] = num

                square_index = board["squares"][square].index(10)
                board["squares"][square][square_index] = num

                # In case we come back to this cell, we won't try the same number again
                tried_cells[(row, col)] = num + 1

                cell_index += 1
                found = True
                break
            else:
                num += 1
        
        if not found:

            # Reset the number for this cell, because when coming back we'll have to try all numbers again
            tried_cells[(row, col)] = 1

            
            cell_index -= 1

            # If the cell index goes to negative, it means we backtracked too far, sudoku is just not solvable
            if cell_index < 0:
                quit("No solution exists")


            # Next cell we have to edit is the previous one, because the cell we tried editing won't fit any number between 1-9
            prev_row, prev_col = empty_cells[cell_index]
            prev_square = find_square_index(row = prev_row, col = prev_col)


            # Find which number we tried for the previous cell
            prev_num = board["rows"][prev_row][prev_col - 1]

            board["rows"][prev_row][prev_col - 1] = 10
            board["columns"][prev_col][prev_row - 1] = 10

            square_index = board["squares"][prev_square].index(prev_num)
            board["squares"][prev_square][square_index] = 10

    return board