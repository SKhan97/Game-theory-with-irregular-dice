import random
from tqdm import trange

dice1_dict = {
    'name': 'Transparent',
    'value1': 3,
    'prob1': 5/6,
    'value2': 6,
    'prob2': 1/6,
}

dice2_dict = {
    'name': 'Grey',
    'value1': 2,
    'prob1': 1/2,
    'value2': 5,
    'prob2': 1/2,
}

dice3_dict = {
    'name': 'Blue',
    'value1': 1,
    'prob1': 1/6,
    'value2': 4,
    'prob2': 5/6,
}

class Dice():
    "Class to generate a die which can only return 2 values"
    def __init__(self, dice):
        self.value1 = dice['value1']
        self.prob1 = dice['prob1']
        self.value2 = dice['value2']
        self.prob2 = dice['prob2']
        self.name = dice['name']

    def roll(self):
        x=random.random()

        if x <= self.prob1:
            return self.value1

        return self.value2


    def compare(self, dice2):
        value1=self.roll()
        value2=dice2.roll()

        if value1>value2:
            return self.name
        elif value2>value1:
            return dice2.name
        else:
            raise Exception('Error with values')

    def calculate(self, dice2, n):
       dice1_wins = 0
       dice2_wins = 0

       for i in trange(n):
           winner = self.compare(dice2)
           if winner == self.name:
               dice1_wins +=1
           elif winner == dice2.name:
               dice2_wins += 1
           else:
               print('#####')

       return(dice1_wins, dice2_wins)


    def compete(self, other_dice, n, individual = False):
        dice_beaten = {}
        dice_lost = {}
        winrate = 0
        for die in other_dice:
            self_wins, other_wins = self.calculate(die,n)
            win_percentage = 100 * self_wins / n

            if self_wins > other_wins:
                dice_beaten[die.name] = win_percentage
            elif self_wins < other_wins:
                dice_lost[die.name] = win_percentage
            else:
                raise Exception('Either the dice are the same or unseen error. Try rerunning script')

        for key in dice_beaten:
            winrate += dice_beaten[key]
            if individual:
                print("%s beats %s with an average of %.1f%% win rate" % (self.name, key, dice_beaten[key]))

        for key in dice_lost:
            winrate += dice_lost[key]
            if individual:
                print("%s loses to %s with an average of only %.1f%% win rate" % (self.name, key, dice_lost[key]))

        average_winrate = winrate/len(other_dice)
        print("%s has an average winrate of %.1f%% winrate against the other dice" % (self.name, average_winrate))










Dice1 = Dice(dice1_dict)
Dice2 = Dice(dice2_dict)
Dice3 = Dice(dice3_dict)

Dice1.compete([Dice2, Dice3], 1000000)
Dice2.compete([Dice1, Dice3], 1000000)
Dice3.compete([Dice1, Dice2], 1000000)


