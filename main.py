import random
import os
import time

def sum (a,b,c): return a+b+c

def clear_screen():
   os.system('cls')
   # pass

def print_board(X,O):
   zero = 'X' if X[0] else ('O' if O[0] else "1")
   one = 'X' if X[1] else ('O' if O[1] else "2")
   two = 'X' if X[2] else ('O' if O[2] else "3")
   three = 'X' if X[3] else ('O' if O[3] else "4")
   four = 'X' if X[4] else ('O' if O[4] else "5")
   five = 'X' if X[5] else ('O' if O[5] else "6")
   six = 'X' if X[6] else ('O' if O[6] else "7")
   seven = 'X' if X[7] else ('O' if O[7] else "8")
   eight = 'X' if X[8] else ('O' if O[8] else "9")

   print('\n')
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
            clear_screen()
            print_board(xState,zState)
            print("X Won the match")
            return 1
        if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            clear_screen()
            print_board(xState,zState)
            print("O Won the match")
            return 0
    return -1


def ai_algo_O(X,O,mov):
   # game variables
   moves = set(mov)
   total_moves= {0,1,2,3,4,5,6,7,8}
   available_moves = total_moves -moves
   corners = {0,2,6,8}
   edges = {1,3,5,7}
   center = 4
    #  cheack if the opponent will win in the next move
   def defence_move(a_moves):
      print("defence move called")
      wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
      for m in a_moves:
         for w in wins:
            if (sum(O[w[0]],O[w[1]], O[w[2]]) == 2) :
               if m in w:
                  print("defence move: ",m)
                  return m+1

   #  cheack if we can win in the next move
   def win_move(a_moves):
      print("win move called")
      wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
      for m in a_moves:
         for w in wins:
            if (sum(X[w[0]],X[w[1]], X[w[2]]) == 2) :
               if m in w:
                  print("win move: ",m)
                  return m+1
   
   
   ad_move =  win_move(available_moves) or defence_move(available_moves)
   if ad_move: return ad_move-1 

   if len(mov)==1:
      if 4 in available_moves :
         print("middle move")
         return 4 
      else :
         print("random move")
         return random.choice(list(available_moves))
   
   
   return random.choice(list(available_moves-corners))


def ai_algo_X(X,O,mov):

   # game variables
   moves = set(mov)
   total_moves= {0,1,2,3,4,5,6,7,8}
   available_moves = total_moves -moves
   corners = {0,2,6,8}
   edges = {1,3,5,7}
   center = 4
   
   #  cheack if the opponent will win in the next move
   def defence_move(a_moves):
      print("defence move called")
      wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
      for m in a_moves:
         for w in wins:
            if (sum(O[w[0]],O[w[1]], O[w[2]]) == 2) :
               if m in w:
                  print("defence move: ",m)
                  return m+1

   #  cheack if we can win in the next move
   def win_move(a_moves):
      print("win move called")
      wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
      for m in a_moves:
         for w in wins:
            if (sum(X[w[0]],X[w[1]], X[w[2]]) == 2) :
               if m in w:
                  print("win move: ",m)
                  return m+1
   
   
   
   ad_move =  win_move(available_moves) or defence_move(available_moves)
   if ad_move: return ad_move-1 

   # edge cases:

   # first move always corner
   if len(moves)==0 : 
      return random.choice(list(corners)) 
      # return 6 
   
   # second move if opponent choose center in the first move
   elif(len(moves)==2) and list(mov)[1]==center:
      print("second move (if opponent choose center)")
      pre_corner_mov:int = mov[0]
      mapping = {0: 8, 8: 0, 2: 6, 6:2}
      return mapping.get(pre_corner_mov)
   
   #second move if opponent choose edge in the first move
   elif (len(moves)==2) and list(mov)[1] in edges :

      print("second move (if opponent choose edge)")
      pre_egde_mov = list(mov)[1]
      pre_corner_mov = list(mov)[0]
   
      mapping_corners={
         0 : (2,6),
         2 : (0,8),
         6: (0,8),
         8: (2,6)
      }
      mapping_edges = {
         1: (6,8),
         3: (2,8),
         5: (0,6),
         7: (0,2)          
      }
      
      cor = mapping_corners.get(pre_corner_mov)
      print("corner: " ,cor)
      egd = mapping_edges.get(pre_egde_mov)
      print("edge: ", egd)

      return list(set(cor) & set(egd))[0] 
   

   # second move if opponent choose corner in the first move
   elif (len(moves)==2) and list(mov)[1] in corners : 
      print("second move (if opponent choose corner)")
      print(list(moves)[0])
      print(list(moves)[1])
      pre_corner_move = list(moves)[0]
      pre_corner_move2 = list(moves)[1]
      mapping_corners={
          0 : (2,6),
          2 : (0,8),
          6: (0,8),
          8: (2,6)
       }
      cor = mapping_corners.get(pre_corner_move)
      return cor[1] if cor[0] == pre_corner_move2 else cor[0]

   # forth move if opponent choose corner or edge in the first move 
   if (len(moves)==4) and not(4 in mov): 
      print("edge case third move")
      available_corner = list(available_moves & corners)
      fst = mov[0]
      mapping = {0: 8, 8: 0, 2: 6, 6:2}
      return mapping.get(fst)

   
   
   # if no edges cases choose random move
   print("random move")
   return random.choice(list(available_moves))

def gameloop():
   
   #  game variables
   X =[0,0,0,0,0,0,0,0,0]
   O =[0,0,0,0,0,0,0,0,0]
   turn = 1
   delay = 2
   moves =[]
   



   print("Welcome to AI powered tic tak toe ")
   time.sleep(2)


   #  game loop
   while(True):
      time.sleep(1)
      clear_screen()
      print("Welcome to AI powered tic tak toe ")
      print_board(X,O)


      # draw condition
      if len(moves)==9 :
         print("Draw\n")
         # if int(input("Do you want to continue (1/0)")):
         if 1 :
            X =[0,0,0,0,0,0,0,0,0]
            O =[0,0,0,0,0,0,0,0,0]
            turn = 1
            delay = 2
            moves =[]
            continue
         else: 
            break
         


      # =====player input =====
      if turn:
         print("X's turn: ")

         # safe input 
         try:
            player_inp_x = ai_algo_X(X,O,moves)
            # player_inp_x = int(input("Enter your move: "))-1
            print("ai:  ",player_inp_x)
         except ValueError  as e:
            print("Enter a valid move", e)
            time.sleep(delay)
            continue
         if (player_inp_x<0 or player_inp_x>8): 
            print("Invalid input")
            time.sleep(delay)
            continue

         # appending the move
         if player_inp_x not in moves :
            moves.append(player_inp_x)
            X[player_inp_x] =1
         else:
            print("Enter valid move")
            time.sleep(delay)
            continue
      else:

         print("O's turn: ")

         # save input
         try:
            # player_inp_o = int(input("Enter your move: "))-1
            player_inp_o = ai_algo_O(O,X,moves)
         except ValueError :
            print("Enter a valid move")
            time.sleep(delay)
            continue
         if (player_inp_o<0 or player_inp_o>8): 
            time.sleep(delay)
            print("Invalid input")



         if player_inp_o not in moves :
            moves.append(player_inp_o)
            O[player_inp_o] =1
         else:
            print("Enter valid move")
            time.sleep(delay)
            continue
      
      cwin = checkWin(X,O)


# =========== win checking ===============
      if(cwin != -1):
         print("Match over")
         # if int(input("Do you want to continue (1/0)")):
         if 1:
            X =[0,0,0,0,0,0,0,0,0]
            O =[0,0,0,0,0,0,0,0,0]
            turn = 0
            delay = 2
            moves =[]
         else: 
            break


      turn = not(turn)
gameloop()