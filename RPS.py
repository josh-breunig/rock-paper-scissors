"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.my_move = "None"
        self.their_move = "None"
        self.index = 0

    def move(self):
        return "rock"

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            move1 = input("Rock, paper, scissors? > ")
            if move1 in moves:
                return move1


class ReflectPlayer(Player):
    def move(self):
        if self.their_move == "None":
            return random.choice(moves)
        else:
            return self.their_move


class CyclePlayer(Player):
    def move(self):
        next_move = moves[self.index]
        self.index = (self.index + 1) % len(moves)
        return next_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.score = 0
        self.p2.score = 0

    def play_round(self):
        if self.p1.score < 5 or self.p2.score < 5:
            move1 = self.p1.move()
            move2 = self.p2.move()
            print(f"Player 1 played {move1}.\n"
                  f"Player 2 played {move2}.")
            if move1 == move2:
                print("** TIE - PLAY AGAIN**")
            else:
                if beats(move1, move2) is True:
                    print("** PLAYER ONE WINS THIS ROUND**")
                    self.p1.score += 1
                elif beats(move1, move2) is False:
                    print("** PLAYER TWO WINS THIS ROUND**")
                    self.p2.score += 1
            print(f"Player ONE score: {self.p1.score} \t"
                  f"Player TWO score: {self.p2.score}")
            self.p1.learn(move1, move2)
            self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(5):
            print(f"Round {round}:")
            self.play_round()
        Game.end_game(self)

    def end_game(self):
        print("GAME OVER")
        if self.p1.score == 5:
            print(f"Player One wins with a score of {self.p1.score} "
                  f"to {self.p2.score }")
        elif self.p2.score == 5:
            print(f"Player Two wins with a score of {self.p2.score } "
                  f"to {self.p1.score}")
        play_again = input("Play again?  y or n > ")
        if play_again == 'y':
            Game.play_game(self)
        else:
            quit()


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
