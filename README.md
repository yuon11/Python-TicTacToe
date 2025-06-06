# Python-TicTacToe
## Overview  
<p>
    This project is an excercise in game programming and python GUIs. The program allows 2 players to play Tic-Tac-Toe, with customizable usernames and the ability to play with Avatars other than "X" and "O". (WIP) Computer Opponent
</p>

## Setup/Installation
<p>
    Running this program requires Python3. To install Python, you can download it from <a href="https://www.python.org/downloads/">Python.org</a> and istall directly from source. For an indepth walkthrough on installation <a href="https://www.geeksforgeeks.org/download-and-install-python-3-latest-version/">GeeksforGeeks.org</a> provides step by step instructions to install and verify your version of Python3. Once python is installed the game can be run with the following commands:

    Python3 main.py

![Starting Window Example](imgs/StartingWindow.PNG?raw=true "Tic-Tac-Toe Starting Window Example")
</p>

## Usage 
<p>
    Once you are able to run the main executable, the program will execute its startup loop and ask a series of questions that will take user input to determine the name and avatars for the players. The first question after the startup window is the following:

![Starting Confirmation Example](imgs/StartupConfirmation.PNG?raw=true "Tic-Tac-Toe Starting Confirmation Example")

At the Player Info screen you can customize what your display name will be, as well as your game avatar. There are some limitations on allowed length. If left blank the player will be set to a default avatar. Both players can select the same avatar without affecting the game.

![Player Info Example](imgs/PlayerInfoWindow.PNG?raw=true "Tic-Tac-Toe Starting Confirmation Example")

Once Player Name and Avatar are selected, the game begins.

![Game Window Example](imgs/GameWindow.PNG?raw=true "Tic-Tac-Toe Game Window Example")

On the game window the Game Board is shown in the center over a Game Log of automated messages that recount the events of the game. Each player has their own action log that will display each move they have made as well as their desired Avatar. To make a move, the player whose turn it is should click the button under their log that cooresponds with the position on the Game Board.
</p>