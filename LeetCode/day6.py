# **********************************************
# 1275. Find Winner on a Tic Tac Toe Game
# **********************************************

def tictactoe(moves: list[list[int]]) -> str:
    # game over? A win or B win
    # finish? draw
    # unfinish? pending
    board = [[0]*3 for i in range(3)]
    win_state = [[[0,0],[0,1],[0,2]],
    [[1,0],[1,1],[1,2]],
    [[2,0],[2,1],[2,2]],
    [[0,0],[1,0],[2,0]],
    [[0,1],[1,1],[2,1]],
    [[0,2],[1,2],[2,2]],
    [[0,0],[1,1],[2,2]],
    [[0,2],[1,1],[2,0]]]
    for index,move in enumerate(moves):
        i,j = move
        if index % 2 == 0:
            board[i][j] = 'A'
        else:
            board[i][j] = 'B'
    def checkWiner(s):
        # for i,j in board:
        #     if board[i][j] == s and 

        print(board)
        # if there's any combination in the all 'A' or all 'B'
        return any([all(board[i][j] == s for i,j in line) for line in win_state])
    if checkWiner('A'): return 'A'
    if checkWiner('B'): return 'B'
    elif len(moves) == 9: return 'Draw'
    else: return 'Pending'

    # A = []
    # B = []
    # for i,j in enumerate(moves):
    #     # if i //2 ==0:
    #     #     A.append(j)
    #     A.append(j) if i//2==0 else B.append(j)
    # while len(A)==3 or len(B) == 3:
    #     for i in range(len(A)-1):
    #         for j in range(len(A)-1):
    #             if A[i][j] == A[i+1][j+1] or A[i][0] == A[i][1] and :
    #                 return 'A'
    #     for i in range(len(B)-1):
    #         for j in range(len(B)-1):
    #             if B[i][j] == B[i+1][j+1]:
    #                 return 'B'
    # if len(A) > len(B):
    #     return 'A'
    # elif len(A) < len(B):
    #     return 'B'
    # else
    # return a
moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
# moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
# moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
print(tictactoe(moves))