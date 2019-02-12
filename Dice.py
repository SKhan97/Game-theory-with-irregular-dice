import random

dice1_values = [3, 5/6, 6, 1/6, 'Transparent'] #Transparent die
dice2_values = [2, 1/2, 5, 1/2, 'Grey'] #Grey die
dice3_values = [1, 1/6, 4, 5/6, 'Blue'] #Blue die


class Dice():
    "Class to generate a die which can only return 2 values"
    def __init__(self, dice_array):
        self.value1 = dice_array[0]
        self.prob1 = dice_array[1]
        self.value2 = dice_array[2]
        self.prob2 = dice_array[3]
        self.name = dice_array[4]

    def roll(self):
        x=random.random()
        if x <= self.prob1:
            return self.value1
        elif self.prob1 < x <= 1:
            return self.value2


    def compare(self, dice2):
        value1=self.roll()
        value2=dice2.roll()

        if value1>value2:
            return self.name
            #print("%s won with a value of %i compared to %i"% (self.name, value1,value2))
        elif value2>value1:
            return dice2.name
            #print("%s won with a value of %i compared to %i"% (dice2.name, value2, value1))
        else:
            print('WTF')

    def calculate(self, dice2, n):
       dice1_wins = 0
       dice2_wins = 0

       for i in range(n): #Need to incorparate the i somehow
           if self.compare(dice2) == self.name:
               dice1_wins +=1
               print(self.compare(dice2))
           elif self.compare(dice2) == dice2.name:
               dice2_wins += 1
           else:
               print(i)

       print(dice1_wins, dice2_wins)








Dice1 = Dice(dice1_values)
Dice2 = Dice(dice2_values)
Dice3 = Dice(dice3_values)

Dice1.calculate(Dice2, 10)


