from create_board import create_board
from bruteforce import bruteforce

board = create_board()

board = bruteforce(board=board)

for i in board["rows"]:
    print(board["rows"][i])