## Hangman

Hangman is a game meant to be something to pass time with, guessing letters of a word without getting the man hung.
If you guess the word correct, you win. If you run out of guesses and haven't gotten the correct word - you lose and the game displays a hanging man.  
It's a Python terminal game, which runs on Heroku. 
The target for this game is someone that needs a few minutes break to pass time. 

## How to play

* Player gets displayed a view of the game, and gets information to choose a letter.
* Player gets information if the guess is correct or false
* The player is displayed with a presentation of previous guesses
* The player will have a display with lines, and correct words printed.
* The player will be see the previous guess if its wrong.
* For every wrong guess there's one more attachment for the hanging man.
* After 6 guesses if word is not guessed, the player will be displayed with the correct word.
* The player will be displayed with a choise to either play a new game or finish the game. 
* If the player writes yes, or y the game starts over.
* If the player writes no the game ends. 


## Created the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

## Inspiration and doc of text:

### Kite on youtube

[Kite on Youtube](https://www.youtube.com/watch?v=m4nEnsavl6w) - Kite's youtube channel, and the video of inspiration here. 

### Shaun Halverson on youtube

[Shaun on YouTube](https://www.youtube.com/watch?v=pFvSb7cb_Us&t=71s) - Shauns youtube channel, and the video of inspiration here.

## Hangman symbols

### Credit for the symbols for hanging man from Chris Horton on github

[Symbols](https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c) - I got the symbols for hangman from here.


## Testing and deploying

### Testing thru the Pep8 website 

[Pep8](http://pep8online.com/) - I tested my Python code here for validation, displayed no errors.
