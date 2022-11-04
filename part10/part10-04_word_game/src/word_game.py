# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        # your code for determining the winner goes here
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2
        else:
            return 0

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        vowel = 'aeiou'
        player1 = 0
        player2 = 0
        for i in player1_word:
            if i in vowel:
                player1 +=1
        for i in player2_word:
            if i in vowel:
                player2 +=1
        if player1 > player2:
            return 1
        elif player1 < player2:
            return 2
        else:
            return 0

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        tool = ['rock','paper','scissors']
        if player1_word not in tool:
            if player2_word not in tool:
                return 0
            return 2
        elif player2_word not in tool:
            if player1_word not in tool:
                return 0
            return 1

        for i in range(len(tool)):
            if player1_word == tool[i]:
                player1 = i
            if player2_word == tool[i]:
                player2 = i
        
        result = player1-player2
        if result in [-1,2]:
            return 2
        elif result in [1,-2]:
            return 1
        else:
            return 0

