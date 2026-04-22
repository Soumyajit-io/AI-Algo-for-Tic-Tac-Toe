import random
import os
import time

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
            os.system('cls')
            print_board(X,O)
            print("X Won the match")
            return 1
        if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            os.system('cls')
            print_board(X,O)
            print("O Won the match")
            return 0
    return -1

def ai_algo_X(X,O,moves):
   
   available_moves = {0,1,2,3,4,5,6,7,8}-moves
   corner = [0,2,6,8]
   edge = [1,3,5,7]
   center = 4
   if any(X)==0 : # first move
      return random.choice(corner)
   
   def win_move(a_moves):
      wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
      for m in a_moves:
         for w in wins:
            if (sum(X[w[0]],X[w[1]], X[w[2]]) == 2) :
               if m in w:
                  print("ai: ",m)
                  return m

   
   
   
   mov = win_move(available_moves) 
   if mov : return mov 
   else: return 4

def gameloop():
   X =[0,0,0,0,0,0,0,0,0]
   O =[0,0,0,0,0,0,0,0,0]
   turn = 1
   delay = 2
   moves =set()
   print("Welcome to AI powered tic tak toe ")
   time.sleep(2)
   while(True):
      os.system('cls')
      print("Welcome to AI powered tic tak toe ")
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
            time.sleep(delay)
            continue
         if (player_inp<0 or player_inp>8): 
            print("Invalid input")
            time.sleep(delay)
            continue
         if player_inp not in moves :
            moves.add(player_inp)
            X[player_inp] =1
         else:
            print("Enter valid move")
            time.sleep(delay)
            continue
      else:
         print("O's turn: ")
         try:
            player_inp = int(input("Enter your move: "))
         except ValueError :
            print("Enter a valid move")
            time.sleep(delay)
            continue

         if (player_inp<0 or player_inp>8): 
            time.sleep(delay)
            print("Invalid input")

         if player_inp not in moves :
            moves.add(player_inp)
            O[player_inp] =1
         else:
            print("Enter valid move")
            time.sleep(delay)
            continue
      cwin = checkWin(X,O)
      if(cwin != -1):
         print("Match over")
         break
      turn = not(turn)
gameloop()