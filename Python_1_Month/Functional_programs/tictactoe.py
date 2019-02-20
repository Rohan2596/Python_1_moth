import random
board=[0,1,2,
        3,4,5,
        6,7,8]
print(board)
def show():
	print(board[0],'|',board[1],'|',board[2])
	print("--|---|--")
	print(board[3],'|',board[4],'|',board[5])
	print("--|---|--")
	print(board[6],'|',board[7],'|',board[8])
def checkline(char,spot1,spot2,spot3):
	if (board[spot1]==char and board[spot2]==char and board[spot3]==char):
		return True
def  checkall(char):
	if checkline(char,0,1,2):
		return True
	if checkline(char,3,4,5):
		return True
	if checkline(char,6,7,8):
		return True
	if checkline(char,0,3,6):
		return True
	if checkline(char,2,5,8):
		return True
	if checkline(char,1,4,7):
		return True
	if checkline(char,0,4,8):
		return True
	if checkline(char,2,4,6):
		return True

while True:
	ip=input("Select the spot:- ")
	ip=int(ip)
	if board[ip]!='x' and board[ip]!='o':
		board[ip]='x'
		if checkall('x')==True:
			print("-----XWins---------")
			break
		
		while True:
			random.seed()
			oppenent=random.randint(0,8)
			if board[oppenent]!='o' and board[oppenent]!='x':
				board[oppenent]='o'
				
				if checkall('o')==True:
					print("------Owins------")
					break
				break
	else:
		print("this spot is taken")
	show()

