import chess
import random
from EvalFunction import *




def main():
    official_board = chess.Board()
    color = input("What color do you want to play as? (white/black): ")
    if(color == "white"):
        game = Game(UserAgent(), EngineAgent())
        game.play_random_game()
    elif(color == "black"):
        game = Game(EngineAgent(), UserAgent())
        game.play_random_game()



if __name__ == '__main__':
    main()
