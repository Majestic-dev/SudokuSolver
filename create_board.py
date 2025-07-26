def create_board() -> dict:

    board = {
        "rows": {},
        "columns": {},
        "squares": {}
    }

    # create the rows

    i = 1

    while i <= 9:
        try:
            board["rows"][i] = [int(char) for char in input(f"Enter row {i} numbers: ")]
            if len(board["rows"][i]) != 9:
                quit("Exiting code, row must contain 9 numbers")
        except ValueError:
            quit("Exiting code, non-numerical string inserted")
        i += 1

    # create columns

    i = 0

    while i <= 8:
        column = []

        for row in board["rows"]:
            column.append(board["rows"][row][i])

        board["columns"][i+1] = column

        i +=1

    # create squares

    for i in range(1, 10):
        board["squares"][i] = []
    for r in board["rows"]:
        for num in board["rows"][r]:
            c = board["rows"][r].index(num) + 1
            if num == 0:
                board["rows"][r][c-1] = 10

            square_num = (3 * ((r-1) // 3) + ((c-1) // 3) + 1)
            board["squares"][square_num].append(board["rows"][r][c-1])

    for i in board["columns"]:
        for num in board["columns"][i]:
            if num == 0:
                index = board["columns"][i].index(0)
                board["columns"][i][index] = 10

    return board