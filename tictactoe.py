def display(board):
  
  print(" "+board[0]+" | "+board[1]+" | "+board[2])
  
  print("-----------")
 
  print(" "+board[3]+" | "+board[4]+" | "+board[5])
  
  print("-----------")
  print(" "+board[6]+" | "+board[7]+" | "+board[8])
  

def check_win(board,pmark):
  return(
      (board[0]==board[1]==board[2]==pmark)or
      (board[3]==board[4]==board[5]==pmark)or
      (board[6]==board[7]==board[8]==pmark)or
      (board[0]==board[3]==board[6]==pmark)or
      (board[1]==board[4]==board[7]==pmark)or
      (board[2]==board[5]==board[8]==pmark)or
      (board[0]==board[4]==board[8]==pmark)or
      (board[2]==board[4]==board[6]==pmark)
  )

def draw(board):
    return ' ' not in board

def copy_board(board):
  copy=[]
  for i in board:
    copy.append(i)
  return copy
   
def test_win_move(board,pmark,move):
  bcopy=copy_board(board)
  bcopy[move]=pmark
  return check_win(bcopy,pmark)   

def win_stat(board):
  if(board[4]==' '):
    return 4

  for i in [0,2,6,8]:
    if(board[i]==' '):
      return i
  for i in [1,3,5,7]:
    if(board[i]==' '):
      return i
  
def fork_move(board,pmark,move):
  copy=copy_board(board)
  winning_moves=0
  for i in range(0,9):
    if test_win_move(copy,pmark,i) and copy[i]==' ':
      winning_moves +=1
  return winning_moves >=2


def comp_analyse(board):
  #agent move for winning 
  for i in range(0,9):
    if board[i]==' ' and test_win_move(board,'O',i):
      return i
  
  #prevent player from winning 
  for i in range(0,9):
    if board[i]==' ' and test_win_move(board,'X',i):
      return i
  
  #fork move 
  for i in range(0,9):
    if board[i]==' ' and fork_move(board,'O',i):
      return i
  
  for i in range(0,9):
    if board[i]==' ' and fork_move(board,'X',i):
      return i
  return win_stat(board)
  


def tictactoe():
  playing=True
  while playing:
    board=[' ']*9
    display(board)
    print("Positions are as follow:")
    print("0, 1, 2 ")
    print("3, 4, 5 ")
    print("6, 7, 8 ")
    print("\n")
    in_game=True
    print ("You want to play first y/n?")
    ch=input()
    sym=''
    if(ch=='y' or ch=='Y'):
      print ("Player symbol is X \n Computer is O")
      sym='X'
    else:
      print ("Player symbol is O \n Computer is X")
      sym='O'
    while in_game:
      if(sym=='X'):
        print("choose a position")
        pos=int(input())
        if board[pos]!=' ':
          print("Invalid position.")
          continue
      else:
        pos=comp_analyse(board)
      
      board[pos]=sym

      if check_win(board,sym):
        in_game=False
        display(board)
        if sym== 'X':
          print ("------------You Won The Game!------------")
        else:
          print ("-------------Computer Won!---------------")
        continue
      if draw(board):
        in_game=False
        display(board)
        print ("--------------It is a Draw!--------------")
        continue

      display(board)
      print("\n --------------------------- \n")
      if sym=='X':
        sym='O'
      else:
        sym='X'
    
    print("Play again? y/n")
    xx=input()

    if xx=='y' or xx=='Y':
      continue
    else:
      break
 

tictactoe()