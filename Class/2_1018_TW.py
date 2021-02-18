#입력은 이중 리스트 생성
#체스판은 검은색과 흰색이 번갈아 칠해져 있어야함
#시작 정사각형의 크기와 관계없이, Output은 8*8 크기의 체스판으로 잘라냄
#Input을 2번 조건을 만족하는 체스판으로 만들라면 몇개의 정사각형을 칠해야 하나?(최소)
import sys

a,b = input().split()

complete_version_1 = ['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW']
complete_version_2 = ['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']

chess_board = []

for i in range(0,int(a)):
    chess_board_column = input()
    if len(chess_board_column) != int(b):
        sys.exit()
    else:
        chess_board.append(chess_board_column)


max_i = len(chess_board[0]) - 7
result_num = []

for i in range(0,max_i):
    cut_chess_board = []
    for col in chess_board:
        cut_column = col[i:i+8]
        cut_chess_board.append(cut_column)
    
    max_col = len(cut_chess_board) - 8
    
    for n ,col in enumerate(cut_chess_board):
        
        if max_col >= n:
            two_cut_chess_board = cut_chess_board[n:n +8]
            num_ver_1 = 0
            num_ver_2 = 0
            for n, col in enumerate(two_cut_chess_board):
                print(n,col)
                for num in range(0,7):
                    if complete_version_1[n][num] != col[num]:
                        num_ver_1 +=1
                    if complete_version_2[n][num] != col[num]:
                        num_ver_2 +=1
            if num_ver_1<num_ver_2:
                result_num.append(num_ver_1)
                num_ver_1 = 0
                num_ver_2 = 0
            else:
                result_num.append(num_ver_2)
                num_ver_1 = 0
                num_ver_2 = 0

print(result_num)