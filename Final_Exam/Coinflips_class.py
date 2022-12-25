
import random

class Coinflips:

    def __init__(self):
        self.wins = 0
        self.games = 0
        self.history = []

    def play(self, guess):
        possible = ["heads", "tails"]
        if guess not in possible:
            raise Warning

        flip = random.choice(possible)
        self.history.append(flip)
        self.games += 1
        if guess == flip:
            self.wins += 1
        return flip

    def winner(self):
        return True if self.wins > self.games / 2 else False

    def __str__(self):
        your_history = ', '.join(self.history)
        return your_history




t = Coinflips()
try:
    t.play("arms")
except Warning:
    print("invalid choice")
# Your play results may be different from this example due to randomness
print(t.play("heads"))
print(t.play("tails"))
print(t.play("heads"))
print(t)
print(t.winner())
