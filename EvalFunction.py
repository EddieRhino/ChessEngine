import random
import chess
import csv
import time
import chess.polyglot
import chess.syzygy


board = chess.Board()

pawnEvalWhite = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5,
0.5, -0.5, 1.0, 0.0, 0.0, -1.0, -0.5, 0.5,
0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0,
0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5,
1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0,
5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

pawnEvalBlack = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0,
0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5,
0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0,
0.5, -0.5, 1.0, 0.0, 0.0, -1.0, -0.5, 0.5,
0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5,
0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

bishopEvalWhite = [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0,
-1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0,
-1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0,
-1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0,
-1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0,
-1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0,
-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]

bishopEvalBlack = [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0,
-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
-1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0,
-1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0,
-1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0,
-1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0,
-1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0,
-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]

knightEval = [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0,
-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0,
-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0,
-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0,
-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0,
-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0,
-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0,
-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]

queenEval = [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,
-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
-1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
-0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,
0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,
-1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
-1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0,
-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]

rookEvalBlack = [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5,
-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]

rookEvalWhite = [0.0, 0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0,
-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5,
0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]

kingEvalBlack = [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0,
-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0,
2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0,
2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0]

kingEvalWhite = [2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0,
2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0,
-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0,
-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0,
-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
 -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0]

def MoveToString(move):
    return str(move)

def StringToMove(string_in):
    return Move.from_uci(string_in)


class ChessAgent:
    def move(self, board, color):
        pass

class RandomAgent(ChessAgent):
    def __init__(self):
        pass
    def move(self, board, color):
        legal_moves = list(board.legal_moves)
        rand = random.randint(0,len(legal_moves)-1)
        move = str(legal_moves[rand])
        board.push_san(move)
        return board

class UserAgent(ChessAgent):
    def __init__(self):
        pass
    def move(self, board, color):
        legal_moves = list(board.legal_moves)
        print("Please enter your move:")
        move = None
        try:
            san = input()
            move = chess.Move.from_uci(san)
        except:
            move = None
        while(not move in legal_moves):
            print("Illegal move, please enter a legal move")
            print("Legal moves: ", legal_moves)
            try:
                san = input()
                move = chess.Move.from_uci(san)
            except:
                print("Illegal move, please enter a legal move")
                move = None

        board.push(move)
        return board

class EngineAgent(ChessAgent):
    def __init__(self):
        pass


    def move(self, board, color):
        def make_opening_move():
            with chess.polyglot.open_reader("data/baron30.bin") as reader:
                for entry in reader.find_all(board):
                    if(entry == None):
                        return None
                    return entry.move

        def make_endgame_move():
            with chess.syzygy.open_tablebase("data/syzygy/regular") as tablebase:
                for move in list(board.legal_moves):
                    board_cpy = board.copy()
                    board_cpy.push_san(str(move))
                    if((tablebase.probe_dtz(board_cpy) == 0) and (tablebase.probe_dtz(board) == 0)):
                        return str(move)
                    elif(((tablebase.probe_dtz(board_cpy)*(-1)) <= tablebase.probe_dtz(board)) and (tablebase.probe_dtz(board_cpy) != 0)):
                        return str(move)
                return str(list(board.legal_moves)[0])


        def position_evaluation(board,color):
            total_ev = 0
            king_safety = 0
            space_controlled = 0
            piece_points = 0
            curr_board2 = board.piece_map()

            def piece_eval(piece_points,color):
                piece_points = 0.0
                def is_passed_pawn(location):
                    return False



                def rook_on_open_file(location,pp):
                    while(location >= 0 and location <= 63):
                        if(color == "black"):
                            if(((curr_board2).get(location) == "P") and (is_passed_pawn(location) == True)):
                                pp += 1
                                return False
                            elif((curr_board2).get(location) != "p"):
                                pp += 0.1
                                return False
                            elif(((curr_board2).get(location) != "P")):
                                location += 8
                                continue
                            else:
                                return False
                        else:
                            if(((curr_board2).get(location) == "p") and (is_passed_pawn(location) == True)):
                                pp += 1
                                return False
                            elif((curr_board2).get(location) != "P"):
                                pp += 0.1
                                return False
                            elif(((curr_board2).get(location) != "p")):
                                location -= 8
                                continue
                            else:
                                return False

                    return True

                def is_protected_passed_pawn(location):
                    pass
                if(color == "black"):
                    for x in range(0,64):
                        if(str(curr_board2.get(x)) == "P"):
                            piece_points += 1
                            piece_points += pawnEvalWhite[x]/10.0
                        elif(str(curr_board2.get(x)) == "R"):
                            piece_points += 5
                            if(rook_on_open_file(x,piece_points) == True):
                                piece_points += 0.4
                            piece_points += rookEvalWhite[x]/10.0
                        elif(str(curr_board2.get(x)) == "N"):
                            piece_points += 3
                            piece_points += knightEval[x]/10.0
                        elif(str(curr_board2.get(x)) == "B"):
                            piece_points += 3
                            piece_points += bishopEvalWhite[x]/10.0
                        elif(str(curr_board2.get(x)) == "Q"):
                            piece_points += 9
                            piece_points += queenEval[x]/10.0
                        elif(str(curr_board2.get(x)) == "K"):
                            piece_points += kingEvalWhite[x]/10.0
                            if(x == 6):
                                piece_points += 0.2
                            elif(x == 2):
                                piece_points += 0.1
                        elif(str(curr_board2.get(x)) == "p"):
                            piece_points -= 1
                            piece_points -= pawnEvalBlack[x]/10.0
                        elif(str(curr_board2.get(x)) == "r"):
                            piece_points -= 5
                            piece_points -= rookEvalBlack[x]/10.0
                            if(rook_on_open_file(x,piece_points) == True):
                                piece_points -= 0.4
                        elif(str(curr_board2.get(x)) == "n"):
                            piece_points -= 3
                            piece_points -= knightEval[x]/10.0

                        elif(str(curr_board2.get(x)) == "b"):
                            piece_points -= 3
                            piece_points -= bishopEvalBlack[x]/10.0
                        elif(str(curr_board2.get(x)) == "q"):
                            piece_points -= 9
                            piece_points -= queenEval[x]/10.0
                        elif(str(curr_board2.get(x)) == "k"):
                            piece_points -= kingEvalBlack[x]/10.0
                        else:
                            continue
                else:
                    for x in range(0,64):
                        if(str(curr_board2.get(x)) == "p"):
                            piece_points += 1
                            piece_points += pawnEvalBlack[x]/10.0
                        elif(str(curr_board2.get(x)) == "r"):
                            piece_points += 5
                            if(rook_on_open_file(x,piece_points) == True):
                                piece_points += 0.4
                            piece_points += rookEvalBlack[x]/10.0
                        elif(str(curr_board2.get(x)) == "n"):
                            piece_points += 3
                            piece_points += knightEval[x]/10.0
                        elif(str(curr_board2.get(x)) == "b"):
                            piece_points += 3
                            piece_points += bishopEvalBlack[x]/10.0
                        elif(str(curr_board2.get(x)) == "q"):
                            piece_points += 9
                            piece_points += queenEval[x]/10.0
                        elif(str(curr_board2.get(x)) == "k"):
                            piece_points += kingEvalBlack[x]/10.0
                            if(x == 62):
                                piece_points += 0.2
                            elif(x == 58):
                                piece_points += 0.1
                        elif(str(curr_board2.get(x)) == "P"):
                            piece_points -= 1
                            piece_points -= pawnEvalWhite[x]/10.0
                        elif(str(curr_board2.get(x)) == "R"):
                            piece_points -= 5
                            piece_points -= rookEvalWhite[x]/10.0
                            if(rook_on_open_file(x,piece_points) == True):
                                piece_points -= 0.4
                        elif(str(curr_board2.get(x)) == "N"):
                            piece_points -= 3
                            piece_points -= knightEval[x]/10.0

                        elif(str(curr_board2.get(x)) == "B"):
                            piece_points -= 3
                            piece_points -= bishopEvalWhite[x]/10.0
                        elif(str(curr_board2.get(x)) == "Q"):
                            piece_points -= 9
                            piece_points -= queenEval[x]/10.0
                        elif(str(curr_board2.get(x)) == "K"):
                            piece_points -= kingEvalWhite[x]/10.0
                        else:
                            continue
                return piece_points


            def our_king_safety():
                pass
            def opp_king_safety():
                pass
            def space():
                # squares = 0
                # if(color == "black"):
                pass



            if((board.is_checkmate() == True) and (color == "black") and (board.result() == "1-0")):
                return 10000000
            elif((board.is_checkmate() == True) and (color == "black") and (board.result() == "0-1")):
                return -10000000
            elif((board.is_checkmate() == True) and (color == "white") and (board.result() == "1-0")):
                return -10000000
            elif((board.is_checkmate() == True) and (color == "white") and (board.result() == "0-1")):
                return 10000000
            elif(board.is_stalemate() == True):
                return 0
            return piece_eval(0.0,color)





        legal_moves = list(board.legal_moves)
        curr_board = board.piece_map()
        board_cpy = board.copy()
        opening_move = make_opening_move()
        if(opening_move != None):
            #print("in opening")
            board_cpy.push_san(str(opening_move))
            print(str(opening_move))
            return board_cpy
        elif(len(curr_board) <= 5):
            #print("in low piece endgame")
            endgame_move = make_endgame_move()
            board_cpy.push_san(endgame_move)
            print(endgame_move)
            return board_cpy
        else:
            print("Thinking...")
            minimax_dict = {}
            minimax_dict1 = {}
            minimax_dict2 = {}
            minimax_dict3 = {}
            #minimax_dict4 = {}
            # minimax_dict5 = {}
            board_cpy2 = board_cpy.copy()
            # legal_moves = list(board_cpy.legal_moves)
            # rand = random.randint(0,len(legal_moves)-1)
            # move = str(legal_moves[rand])
            # board_cpy.push_san(move)
            for move1 in list(board_cpy2.legal_moves):
                board_cpy3 = board_cpy2.copy()
                minimax_dict.update({str(move1):0})
                board_cpy3.push_san(str(move1))
                pos_eval1 = position_evaluation(board_cpy3,color)
                if(pos_eval1 < -10):
                    minimax_dict.update({str(move1):pos_eval1})
                    continue
                for move2 in list(board_cpy3.legal_moves):
                    board_cpy4 = board_cpy3.copy()
                    minimax_dict1.update({str(move2):0})
                    board_cpy4.push_san(str(move2))
                    pos_eval2 = position_evaluation(board_cpy4,color)
                    if(pos_eval2 < -5):
                        minimax_dict1.update({str(move2):pos_eval2})
                        continue
                    for move3 in list(board_cpy4.legal_moves):
                        board_cpy5 = board_cpy4.copy()
                        minimax_dict2.update({str(move3):0})
                        board_cpy5.push_san(str(move3))
                        pos_eval3 = position_evaluation(board_cpy5,color)
                        if(pos_eval3 < -3):
                            minimax_dict2.update({str(move3):pos_eval3})
                            continue
                        # else:
                        #     minimax_dict2.update({str(move3):pos_eval3})
                        for move4 in list(board_cpy5.legal_moves):
                            board_cpy6 = board_cpy5.copy()
                            minimax_dict3.update({str(move4):0})
                            board_cpy6.push_san(str(move4))
                            pos_eval4 = position_evaluation(board_cpy6,color)
                            if(pos_eval4 < -3):
                                minimax_dict3.update({str(move4):pos_eval4})
                                continue
                            else:
                                minimax_dict3.update({str(move4):pos_eval4})
                            # for move5 in list(board_cpy6.legal_moves):
                            #     board_cpy7 = board_cpy6.copy()
                            #     minimax_dict4.update({str(move5):0})
                            #     board_cpy7.push_san(str(move5))
                            #     pos_eval5 = position_evaluation(board_cpy7,color)
                            #     if(pos_eval5 < -3):
                            #         minimax_dict4.update({str(move5):pos_eval5})
                            #         continue
                            #     else:
                            #         minimax_dict4.update({str(move5):pos_eval5})
                            # if(minimax_dict4 == {}):
                            #      break
                            # minimax_dict3.update({str(move4):max(minimax_dict4.values())})
                            # minimax_dict4.clear()
                        if(minimax_dict3 == {}):
                             break
                        minimax_dict2.update({str(move3):min(minimax_dict3.values())})
                        minimax_dict3.clear()
                    #print(minimax_dict2)
                    if(minimax_dict2 == {}):
                        break

                    minimax_dict1.update({str(move2):max(minimax_dict2.values())})
                    minimax_dict2.clear()
                #print(minimax_dict1)
                if(minimax_dict1 == {}):
                    break
                minimax_dict.update({str(move1):min(minimax_dict1.values())})
                minimax_dict1.clear()
            # move_to_make = max(minimax_dict, key=minimax_dict.get)
            #print(minimax_dict)
            max_val = max(minimax_dict.values())
            for x,y in minimax_dict.items():
                if (y == max_val):
                    move_to_make = x
                    break
            print(str(move_to_make))
            print(round(max_val,2))
            board_cpy2.push_san(str(move_to_make))
            return board_cpy2













class Game:
    white_agent = None
    black_agent = None
    color = None

    def __init__(self, white = RandomAgent(), black = RandomAgent()):
        self.black_agent = black
        self.white_agent = white


    def get_board(self):
        return board

    def play_random_game(self):
        board = chess.Board()
        print(board)
        print("\n")
        if(self.black_agent == EngineAgent()):
            self.color = "black"
        else:
            self.color = "white"
        color = self.color
        while(not board.is_checkmate() and not board.is_stalemate() and not board.is_insufficient_material() and
        not board.can_claim_draw() and not board.is_fifty_moves()):
            if(board.turn):
                board = self.white_agent.move(board,color)
            else:
                board = self.black_agent.move(board,color)
            print(board)
            print("\n")
        print(board.outcome())


#board
# 56 57 58 59 60 61 62 63
# 48 49 50 51 52 53 54 55
# 40 41 42 43 44 45 46 47
# 32 33 34 35 36 37 38 39
# 24 25 26 27 28 29 30 31
# 16 17 18 19 20 21 22 23
# 08 09 10 11 12 13 14 15
# 00 01 02 03 04 05 06 07
