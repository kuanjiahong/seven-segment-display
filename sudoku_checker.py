'''
https://stackoverflow.com/questions/13410733/python-sudoku-checker
'''

file_list = ['sudoku_test_1.txt', 'sudoku_test_2.txt']



def sudoku(board:list):
    for i in range(9):
        valid_row = []
        for j in range(9):
            if board[i][j] not in valid_row:
                valid_row.append(board[i][j])
            else:
                return False
    
    for i in range(9):
        valid_col = []
        for j in range(9):
            if board[j][i] not in valid_col:
                valid_col.append(board[j][i])
            else:
                return False
    valid = set(range(1,10))
    sum_valid = sum(valid)
    counter = 0
    while counter < 7:
        subgrid = board[counter: counter+3]

        result = set()
        for row in subgrid:
            for n in row[0:3]:
                result.add(int(n))
        
        if sum(result) != sum_valid:
            return False

        result = set()

        for row in subgrid:
            for n in row[3:6]:
                result.add(int(n))
        
        if sum(result) != sum_valid:
            return False

        
        result = set()

        for row in subgrid:
            for n in row[6:9]:
                result.add(int(n))
        
        if sum(result) != sum_valid:
            return False
        
        counter += 3
    
    return True

for file in file_list:
    board = []
    with open(file, 'r') as f:
        for line in f:
            row = list(line.strip())
            board.append(row)

    if sudoku(board):
        print("Yes, valid board")
    else:
        print("No, invalid board")