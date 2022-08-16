## Hangman

Hangman is a game meant to be something to pass time with, guessing letters of a word. 
It's a Python terminal game, which runs on Heroku. 
The target for this game is someone that needs a few minutes break to pass time. 

## How to play

* Player gets displayed a view of the game, and gets information to choose a letter.
* Player gets information if the guess is correct or false
* The player is displayed with a presentation of previous guesses


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
