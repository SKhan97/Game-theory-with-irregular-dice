# Game-theory-with-irregular-dice

There are 3 Dice:

Dice 1 - Five sides are 3 and one side is 6  
Dice 2 - Five sides are 4 and one side is 1  
Dice 3 - Three sides are 5 and three sides are 2  

The game is simple. Player 1 picks a die and then Player 2 selects one of the remaining two. Whoever rolls the highest wins. 

You can't simply take the expectation of each die because the actual value you're trying to compute is the long-term probability of winning rather than the long-term value you're going to average out to. To illustrate through an exaggerated example:

    Die A only ever rolls 1 with a probability of 100%
    Die B rolls 1 with a probability of 98% or 100 with a probability of 2%

    <Die A> = 1 & <Die B> = 2.98 so Die B has an expectation ~3x greater but a winrate of only 2%! The expectation of value is weighted too much towards values and is not the ideal metric for determining which die is better for the game.


Puzzle to figure out:



Questions Answered:
Which player would you want to be and which die you would want to select for each player?
How does this change if the game is the sum of two rolls rather than a single roll? How does it generalise to N rolls? 

