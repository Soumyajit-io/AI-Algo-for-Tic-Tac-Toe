import random

def sum (a,b,c): return a+b+c

def print_board(X,O):
   zero = 'X' if X[0] else ('O' if O[0] else "0")
   one = 'X' if X[1] else ('O' if O[1] else "1")
   two = 'X' if X[2] else ('O' if O[2] else "2")
   three = 'X' if X[3] else ('O' if O[3] else "3")
   four = 'X' if X[4] else ('O' if O[4] else "4")
   five = 'X' if X[5] else ('O' if O[5] else "5")
   six = 'X' if X[6] else ('O' if O[6] else "6")
   seven = 'X' if X[7] else ('O' if O[7] else "7")
   eight = 'X' if X[8] else ('O' if O[8] else "8")

   print(f" {zero} | {one} | {two} ")
   print(f"---|---|---")
   print(f" {three} | {four} | {five} ")
   print(f"---|---|---")
   print(f" {six} | {seven} | {eight} ")
   print('\n')

def checkWin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print_board(X,O)
            print("X Won the match")
            return 1
        if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print_board(X,O)
            print("O Won the match")
            return 0
    return -1



if __name__ == "__main__":
   X =[0,0,0,0,0,0,0,0,0]
   O =[0,0,0,0,0,0,0,0,0]
   turn = 1
   moves =set()
   print("Welcome to AI powered tic tak toe ")
   while(True):
      print_board(X,O)
      if len(moves)==9 :
         print("Draw")
         break
      if turn:
         print("X's turn: ")
         try:
            # player_inp = int(ai_algo(X,O,moves))
            player_inp = int(input("Enter your move: "))
            print(player_inp)
         except ValueError  as e:
            print("Enter a valid move", e)
            continue
         if (player_inp<0 or player_inp>8): 
            print("Invalid input")
            continue
         if player_inp not in moves :
            moves.add(player_inp)
            X[player_inp] =1
         else:
            print("Enter valid move")
            continue
      else:
         print("O's turn: ")
         try:
            player_inp = int(input("Enter your move: "))
         except ValueError :
            print("Enter a valid move")
            continue

         if (player_inp<0 or player_inp>8): 
            print("Invalid input")

         if player_inp not in moves :
            moves.add(player_inp)
            O[player_inp] =1
         else:
            print("Enter valid move")
            continue
      cwin = checkWin(X,O)
      if(cwin != -1):
         print("Match over")
         break
      turn = not(turn)