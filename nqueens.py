def p_board(board):
	for row in range(len(board)):
		for i in range(row):
			print(i,end=' ')
		print()
def print_board(board):
	for row in board:
		print(' '.join(['Q' if x == 1 else '.' for x in row]))

def isSafe(board,row,col,n):
	for i in range(row):
		if board[i][col]==1:
			return False
	for i ,j in zip(range(row,-1,-1),range(col,-1,-1)):
		if board[i][j]==1:
			return False
	for i ,j in zip(range(row,-1,-1),range(col,n)):
		if board[i][j]==1:
			return False
	return True
		      

def solve_nqueen(board,row,n):
	if row==n:
		print(print_board(board))
	for col in range(n):
		if isSafe(board,row,col,n):
			board[row][col]=1
			solve_nqueen(board,row+1,n)
			board[row][col]=0



def main():
	n=int(input("enter the size of the matrix:"))
	first_row_value=int(input("first_row_value:"))
	first_row_coln=int(input("first_row_coln:"))

	board = [[0 for _ in range(n)] for _ in range(n)]

	if 0<=first_row_value<n and 0<=first_row_coln<n:
		board[first_row_value][first_row_coln]=1
	else:
		print("invalid input")

	solve_nqueen(board,first_row_value+1,n)
	
	
if __name__=="__main__":
	main()