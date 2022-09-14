
#
# TIC TAC TOE PYTHON GAME
# Developed by Yuon Flemming
#
from ast import For
from cgitb import reset
from shutil import move
import sys
from tabnanny import check
from webbrowser import get
import numpy as np
# x = np.random.random((3,3,3))

class TicTacToe():

    def __init__(self, BoardSize=3):
        self._defaultGameBoard = [['--' for i in range(BoardSize)] for j in range(BoardSize)]
        
        self._winCondition = False
        self._drawState = False
        self._roundCount= 1
        self._playerDirectory={"player1": {
                                            "name": "Player1",
                                            "avatar": "X",
                                            "moves": [],
                                            "gameHistory": {},
                                            },
                                "player2": {
                                            "name": "Player2",
                                            "avatar": "O",
                                            "moves": [],
                                            "gameHistory": {},
                                            }
                                }
        
    
    
    # def assignPlayerAvatar(player="Player1"):        
    #     # Taking input from the user
    #     name = input("Enter your avatar (default is X or O) "+player)

    def validateGameRow(self, rowNum:int)->bool:
        if rowNum>0 and rowNum<= len(self._defaultGameBoard[0]):
            return True
        else:
            return False

    def validateGameCol(self, colNum:int)->bool:
        if colNum>0 and colNum<= len(self._defaultGameBoard):
            return True
        else:
            return False

    # Get Player Display Name
    def getPlayerDisplayName(self, player):
 
        return self._playerDirectory[player]["name"]

    # Get Player Avatar
    def getPlayerAvatar(self, player):

        return self._playerDirectory[player]["avatar"]

    # Get the specified move of selected player
    def getPlayerMove(self, player, index=-1):

        return self._playerDirectory[player]["moves"][index]

    # Add most recent player move to the game board
    def updateGameBoard(self, player):
        
        playerMove = self.getPlayerMove(player)
        rowMove= playerMove[0]-1
        colMove= playerMove[1]-1
        playerAvatar = self.getPlayerAvatar(player)
        
        print("\n" + self.getPlayerDisplayName(player).upper() + " has selected.")
        print("ROW: " + str(playerMove[0]))
        print("COL: " + str(playerMove[1]) + "\n")

        if self._defaultGameBoard[rowMove][colMove] == "--":
            
            self._defaultGameBoard[rowMove][colMove] = playerAvatar
        else:
            raise ValueError("Invalid Row or Column selected. Space take is taken.")

    # Get user input to configure Game Board
    def setBoardSettings(self):

        rowNum = int(input("Enter Your Row Selection: "))
        colNum = int(input("Enter You Column Selection: "))

        if self.validateGameRow(rowNum) and self.validateGameCol(colNum):
            return (rowNum, colNum)
        else:
            raise ValueError("Invalid Row or Column selected. Please select again.")

    # Get user input to make next move
    def setPlayerMoveInput(self, player, rowNum=1, colNum=1):
        
        print("\n")
        print(player + ": "+ self._playerDirectory[player]["name"] + "'s MOVE")
        # rowNum = int(input("Enter Your Row Selection: "))
        # colNum = int(input("Enter You Column Selection: "))

        if self.validateGameRow(rowNum) and self.validateGameCol(colNum):
            self._playerDirectory[player]["moves"].append((rowNum, colNum))
        else:
            raise IndexError("Invalid Row or Column selected. Please select again.")    
    
    # Take input from player to set desired avatar and displayname
    def setPlayerInfo(self, inputPlayer="player1"):
        
        print("\n")
        playerName = input("Enter Your Display Name "+ inputPlayer + ": ")
        playerAvatar = input("Enter Your Display Avatar "+ playerName+ ": ")[0]

        if(len(playerName)>0):
            self._playerDirectory[inputPlayer]["name"] = playerName
        if(len(playerAvatar)>0):
            self._playerDirectory[inputPlayer]["avatar"] = playerAvatar
        
    # Print player info to screen
    def printPlayerInfo(self):
        for player in self._playerDirectory.keys():
            print("\n")
            print("-------------------------------------------------------------------")
            print(player + " Display Name: " + self._playerDirectory[player]["name"])
            print(player + " Avatar: " + self._playerDirectory[player]["avatar"])
            print("-------------------------------------------------------------------")
            print("\n")
            
    # print current state of the gameboard
    def drawGameBoard(self):
        for row in self._defaultGameBoard:
            print(row)
    
    # Check is player has won game
    def checkWinState(self, player="player1")->bool:
        playerMove=self.getPlayerMove(player)
        rowMove= playerMove[0]-1
        colMove= playerMove[1]-1
        playerAvatar = self.getPlayerAvatar(player)

        # Print which way the user won
        if(self.checkVertical(colMove, playerAvatar)):
            self.printWinMessage(player)
            self._winCondition=True
            return True
        if(self.checkHorizontal(rowMove, playerAvatar)):
            self.printWinMessage(player)
            self._winCondition=True
            return True
        if(self.checkDiagonal(playerAvatar)):
            self.printWinMessage(player)
            self._winCondition=True
            return True
        if(self.checkReverseDiagonal(playerAvatar)):
            self.printWinMessage(player)
            self._winCondition=True
            return True
        return False

    # Check if the game is in a draw state
    def checkDrawState(self):
        totalMoves = len(self._playerDirectory["player1"]["moves"]) + len(self._playerDirectory["player2"]["moves"])
        if(totalMoves>=9 and not self._winCondition):
            self.printDrawMessage()
            self._drawState=True
            return True
        else:
            return False

    # Check for win from top to bottom
    def checkVertical(self, col, playerAvatar):

        for boardRow in self._defaultGameBoard:
            if(boardRow[col]==playerAvatar):
                continue
            else:
                return False
        return True

    # Check for win from left to right
    def checkHorizontal(self, row, playerAvatar):
        for boardCol in self._defaultGameBoard[row]:
            if(boardCol==playerAvatar):
                continue
            else:
                return False
        return True

    # Check for win from Right to Left diagonal
    def checkDiagonal(self, playerAvatar):
        col=0
        for boardRow in self._defaultGameBoard:
            if(boardRow[col]==playerAvatar):
                col+=1
                continue
            else:
                return False
        return True

    # Check for win from right to left diagonal
    def checkReverseDiagonal(self, playerAvatar):
        col=-1
        for boardRow in self._defaultGameBoard:
            if(boardRow[col]==playerAvatar):
                col-=1
                continue
            else:
                return False
        return True

    def printWinMessage(self, player="player1"):
        print("\n")
        print("----------------------------------------------------------------------------------------")
        print("CONGRATULATIONS! "+player + " " + self._playerDirectory[player]["name"] + ", YOU'VE WON!")
        print("----------------------------------------------------------------------------------------")
        print("\n")

    def printDrawMessage(self):
        print("\n")
        print("----------------------------------------------------------------------------------------")
        print("GOOD MATCH! Players "+ self._playerDirectory["player1"]["name"] + " and " + self._playerDirectory["player2"]["name"] + ", YOU'VE REACHED A DRAW!")
        print("----------------------------------------------------------------------------------------")
        print("\n")

    def clearPlayerMoves(self):
        # Create round label
        roundLabel = "round_" + str(self._roundCount)

        # Add moves from last round to game history
        self._playerDirectory["player1"]["gameHistory"][roundLabel]=self._playerDirectory["player1"]["moves"]
        self._playerDirectory["player2"]["gameHistory"][roundLabel]=self._playerDirectory["player2"]["moves"]

        # Reset move list for round
        self._playerDirectory["player1"]["moves"]=[]
        self._playerDirectory["player2"]["moves"]=[]
        
    # Reset game state
    def resetGame(self, BoardSize=3):
        self._defaultGameBoard = [['--' for i in range(BoardSize)] for j in range(BoardSize)]
        self._winCondition = False
        self._drawState = False
        self.clearPlayerMoves()

        print("\nSETTING UP NEW GAMEBOARD...\n")
        self._roundCount+=1
        self.drawGameBoard()

    def playAgain(self):
        userInput=input("Would you like to play again (Y|N)? ")[0]
        if(userInput.upper()=="Y"):
            self.resetGame()       
            
            # self.playAgain=True
        # else:
        #     self.playAgain=False

    def SETUP(self, defaultBoard=True):
        
        if(not defaultBoard):
            self.setBoardSettings()

        self.setPlayerInfo("player1")
        self.setPlayerInfo("player2")

        self.printPlayerInfo()
        self.drawGameBoard()
    
    def gameRound(self, player="player1"):
        self.setPlayerMoveInput(player)
        self.updateGameBoard(player)
        self.drawGameBoard()
        self._winCondition = self.checkWinState(player)
        self._drawState = self.checkDrawState()
        

# # Main Game loop that will control the flow of the game
# # The game opbject holds all necessary functions to play the game
# def GameLoop():
    
#     # Instantiate Game Object and win state
#     gameInstance = TicTacToe()
#     gameInstance.SETUP()
#     gameInstance.printPlayerInfo()

#     # BEGIN GAME LOOP
#     while not gameInstance._winCondition and not gameInstance._drawState:
#         try:
#             gameInstance.gameRound("player1")

#             if(not gameInstance._winCondition and not gameInstance._drawState):
#                 gameInstance.gameRound("player2")
                    
#             if(gameInstance._winCondition or gameInstance._drawState):
#                 gameInstance.playAgain()
                
#         except ValueError:
#             print("\n")
#             print("Invalid move. The board position you've selected is already taken.")
#             print("\n")
#         except IndexError:
#             print("\n")
#             print("Invalid move. The board position you've selected is out of bounds.")
#             print("\n")
        


# def main() -> int:
#     print("STARTING GAME LOOP ... ")
    
#     GameLoop()
#     return 0

# if __name__ == '__main__':
#     sys.exit(main())  # next section explains the use of sys.exit