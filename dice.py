import random
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

class Dice():
    "Class to generate a die which can only return 2 values"
    def __init__(self, name, value1, prob1, value2, prob2):
        self.name = name
        self.value1 = value1
        self.prob1 = prob1
        self.value2 = value2
        self.prob2 = prob2
        

    def roll(self):
        x=random.random()

        if x <= self.prob1:
            return self.value1

        return self.value2


    def compare(self, dice2, n_rolls = 1):
        
        value1, value2 = 0, 0

        for roll in range(n_rolls):
            value1+=self.roll()
            value2+=dice2.roll()

        if value1>value2:
            return self.name
        elif value2>value1:
            return dice2.name
        else:
            pass 
            # raise Exception('Error with values')

    def calculate(self, dice2, n, n_rolls = 1):
       dice1_wins, dice2_wins, draws = 0, 0, 0

       for i in range(n):
           winner = self.compare(dice2, n_rolls = n_rolls)
           if winner == self.name:
               dice1_wins +=1
           elif winner == dice2.name:
               dice2_wins += 1
           else:
               draws += 1

       return(dice1_wins, dice2_wins, draws)


    def compete(self, other_dice, n, individual = False, n_rolls = 1):
        dice_win, dice_lost= {}, {}
        winrate = 0
        for die in other_dice:
            self_wins, other_wins, draws = self.calculate(die,n, n_rolls = n_rolls)
            win_percentage = 100 * self_wins / n

            if self_wins > other_wins:
                dice_win[die.name] = win_percentage
            elif self_wins < other_wins:
                dice_lost[die.name] = win_percentage

            elif self_wins == other_wins:
                raise Exception('Winrate is equal!')
            else:
                raise Exception('Either the dice are the same or unseen error')

        for key in dice_win:
            winrate += dice_win[key]
            if individual:
                print(f"{self.name} beats {key} with an average of {dice_win[key]} win rate")

        for key in dice_lost:
            winrate += dice_lost[key]
            if individual:
                print(f"{self.name} loses to {key} with an average of only {dice_lost[key]} win rate")

        # average_winrate = winrate/len(other_dice)
        # print(f"{self.name} has an average winrate of {average_winrate} winrate against the other dice")






dice1 = Dice('Transparent', 3, 5/6, 6, 1/6)
dice2 = Dice('Grey', 2, 1/2, 5, 1/2)
dice3 = Dice('Blue', 1, 1/6, 4, 5/6)


dice1.compete([dice2, dice3], 10000, individual=True, n_rolls = 2)
dice2.compete([dice1, dice3], 10000, individual=True, n_rolls=2)
dice3.compete([dice1, dice2], 10000, individual=True, n_rolls=2)

def prob_win(wins):
    return wins[0]/(wins[0]+wins[1]+wins[2])

def plot_probabilities(max_rolls):

    x = [i for i in range(1,max_rolls+1)]
    y1 = np.zeros(max_rolls)
    y2 = np.zeros(max_rolls)
    y3 = np.zeros(max_rolls)

    for i in tqdm(x):
        y1[i-1] = prob_win(dice1.calculate(dice2, 10000, n_rolls=i))
        y2[i-1] = prob_win(dice1.calculate(dice3, 10000, n_rolls=i))
        y3[i-1] = prob_win(dice2.calculate(dice3, 10000, n_rolls=i))

    plt.scatter(x, y1, label = dice1.name, s=0.5)
    plt.scatter(x, y2, label = dice2.name, s=0.5)
    plt.scatter(x, y3, label = dice3.name, s=0.5)
    plt.legend()
    plt.show()
    plt.savefig('dice.png')

# plot_probabilities(1000)
