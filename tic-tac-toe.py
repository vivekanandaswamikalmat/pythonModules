board = { '7':' ','8':' ', '9':' ' ,
	'4':' ','5': ' ','6':' ',
	'1':' ','2':' ', '3':' '}

def win(board):
	if board['7']+board['8']+board['9']=='xxx'  or board['9']+board['6']+board['3']=='xxx' or board['3']+board['2']+board['1']=='xxx' or board['1']+board['4']+board['7']=='xxx' or board['7']+board['5']+board['3']=='xxx' or board['9']+board['5']+board['1']=='xxx' or board['8']+board['5']+board['2']=='xxx' or board['6']+board['5']+board['4']=='xxx':
		print('X has won the match')
		return 1
	if board['7']+board['8']+board['9']=='000'  or board['9']+board['6']+board['3']=='000' or board['3']+board['2']+board['1']=='000' or board['1']+board['4']+board['7']=='000' or board['7']+board['5']+board['3']=='000' or board['9']+board['5']+board['1']=='000' or board['8']+board['5']+board['2']=='000' or board['6']+board['5']+board['4']=='000':
		print('O has won the match')
		return 1
	return 0

print('TIC TAC TOE')
print()
print('positions:')
print()
print('7'+'|'+ '8' + '|' + '9')
print('-+-+-')
print('4'+'|'+ '5' + '|' + '6')
print('-+-+-')
print('1'+'|'+ '2' + '|' + '3')
print()


def printboard(board):
	print()
	print(board['7']+'|'+ board['8'] + '|' + board['9'])
	print('-+-+-')
	print(board['4']+'|'+ board['5'] + '|' + board['6'])
	print('-+-+-')
	print(board['1']+'|'+ board['2'] + '|' + board['3'])
	print()

printboard(board)

turn = 'x'
count=0
w=0

while count<9:
	pos = input(turn+"'s"+' turn, Enter the position :')
	if board[pos] == ' ':
		board[pos] = turn
	printboard(board)
	if win(board):
		w=1
		break
	if pos in ['1','2','3','4','5','6','7','8','9']:
		count+=1
		if turn=='x':
			turn='0'
		else:
			turn='x'
	else:
		print('Invalid key')


if not w:
	print('The match has been tied')	

input()