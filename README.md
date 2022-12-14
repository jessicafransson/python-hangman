# About

## Hangman

Hangman is a game meant to be something to pass time with, guessing letters of a word without getting the man hung.
If you guess the word correct, you win. 
If you run out of guesses and haven't gotten the correct word - you lose and the game displays a hanging man.  
It's a Python terminal game, which runs on Heroku. 
The target for this game is someone that needs a few minutes break to pass time. 

## How to play

* Player gets displayed a view of the game, and gets information to choose a letter.
* Player gets information if the guess is correct or false
* The player is displayed with a presentation of previous guesses
* The player will have a display with lines, and correct words printed.
* The player will see the previous guess if its wrong.
* For every wrong guess there's one more attachment for the hanging man.
* After 6 guesses if word is not guessed, the player will be displayed with the correct word.
* The player will be displayed with a choise to either play a new game or finish the game. 
* If the player writes yes, or y the game starts over.
* If the player writes no the game ends. 

## Find the live game here

https://hangmanjf.herokuapp.com/

## Here's how the game is displayed:  


* You first get a welcome message, saying let's play!  

* You get the message with Guess a letter:  
![guess a letter](images/startgame.png "Guess the first letter")


* If you try guessing anything but a letter, you get asked to enter a valid option, and the suggestions of the letters valid,  
![invalid guess](images/invalidguess.png "Display if you guess anything but a letter")

* If you guess the wrong letter you get displayed the amount of guesses you have left, it also displays amount of correct guesses which here shows as 0.  
![wrong guess](images/wrongguess.png "If you guess a wrong letter")

* If you guess the correct word, the letter is displayed on the line for the word, and correct guesses starts counting with 1.     
![correct guess](images/correctguess.png "If you make a correct guess")

* If you win the game, you get this message.   
![game won](images/gamewon.png "Winning message")

* If you lose the game, you get this message.   
![game lost](images/gamelost.png "Lost game message")

### You can either press yes or no to either restart the game or end the loop.  

# Testing and deploying project

### Testing thru the Pep8 website 

[Pep8](http://pep8online.com/) - I tested my Python code here for validation, displayed no errors.  
![pep8 message no errors](images/pep8validator.png "Displaying Pep8 validator without errors"). 

## Created the Heroku app

* I started with creating a _Config Var_ called `PORT`, and set this to `8000` in my Heroku page.  

* I created the app using following steps:  
* I added two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

* The importance here is to first have the Python, and after it the nodejs for it to work properly.

# Technologies used

* This project was made using only Python.  
* Code is written in gitpod.  
* This project has been deployed to Heroku.  

# Future additions.   

* Due to loosing a week i decided to skip some features because of lack of time.  
(I got notification of extension only a day before deadline when my game was already completed).  
* I would have added a step before game start to enter user name.  
* I would have added a nicer way to display how to not guess numbers, symbols or empty space.  
* I would have added a cleaner way to display previous guesses.   

# Errors and issues. 

* I had an error with getting the user to not be able to guess empty letters, numbers or symbols. I fixed this by adding the def ask input.  
* I had issues with the indetation which was giving me errors in PEP8.  I fixed that by going over my code and sorting out indentations

# Credits and content

### Kite on youtube

[Kite on Youtube](https://www.youtube.com/watch?v=m4nEnsavl6w) - Kite's youtube channel, and the video of inspiration here. 

### Shaun Halverson on youtube

[Shaun on YouTube](https://www.youtube.com/watch?v=pFvSb7cb_Us&t=71s) - Shauns youtube channel, and the video of inspiration here.

## Hangman symbols

### Credit for the symbols for hanging man from Chris Horton on github

[Symbols](https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c) - I got the symbols for hangman from here.

# Acknowledgements

* This is a game for Project 3 for the Full Stack Software Developer program with Code Institute.  
## Jessica Fransson, 2022