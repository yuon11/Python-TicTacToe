from __future__ import division
from cgi import test
from email import message
from tkinter import *
from tkinter import messagebox
from collections import OrderedDict
from TicTacToe import *
from playsound import playsound
import tkinter.font as TkFont
import sys
import math
import json
import pygame
import winsound

GAMEINSTANCE = TicTacToe()

GAME_UI_ELEMENTS = {}

# Dictionary to track player ui elements state
PLAYER_UI_ELEMENTS={
    "player1": 
    {
        "Buttons": False
    },
    "player2": 
    {
        "Buttons": False
    }
}

# pygame.mixer.init()# initialise the pygame
def play():
    print("Testing music")
    playsound("C:\\Users\\Yuon\\PersonalProjects\\CodeProjects\\Python\\TicTacToeApp\\sounds\\Intense_mechanical_music.mp3", False)
    print("After playing music")
    # pygame.mixer.music.load(r"C:\Users\Yuon\PersonalProjects\CodeProjects\Python\TicTacToeApp\sounds\Intense_mechanical_music.mp3")
    # pygame.mixer.music.play(loops=-1)


# Check the state of the 
def checkButtonState(player):
    return PLAYER_UI_ELEMENTS[player]["Buttons"]

# Switch buttons to on
def activatePlayerElements(player):
    PLAYER_UI_ELEMENTS[player]["Buttons"]=True

# Switch buttons to off
def deactivatePlayerElements(player):
    PLAYER_UI_ELEMENTS[player]["Buttons"]=False

def printWinMessage(player="player1"):
    message=""
    message+="\n"
    message+="----------------------------------------------------------------------------------------"
    message+="CONGRATULATIONS! "+player + " " + GAMEINSTANCE._playerDirectory[player]["name"] + ", YOU'VE WON!"
    message+="----------------------------------------------------------------------------------------"
    message+="\n"
    
    return message

def printDrawMessage():
    message=""
    message+= "\n"
    message+="----------------------------------------------------------------------------------------"
    message+="GOOD MATCH! Players "+ GAMEINSTANCE._playerDirectory["player1"]["name"] + " and " + GAMEINSTANCE._playerDirectory["player2"]["name"] + ", YOU'VE REACHED A DRAW!"
    message+="----------------------------------------------------------------------------------------"
    message+="\n"
    
    return message
    
# Create The button layout for player 1
def setupP1Frame(top):

        player1Data = GAMEINSTANCE._playerDirectory["player1"]

        p1Frame=Frame(top, bd=3, relief=SUNKEN)
        p1YScrollBar = Scrollbar(p1Frame)
        p1YScrollBar.grid(row=0, rowspan=1, column=10, sticky=N+S+W)

        p1TxtField = Text(p1Frame, height=10,width=50, spacing3=8,
                    font=TkFont.Font(family="Helvetica", size=9, weight="bold"),
                    yscrollcommand=p1YScrollBar.set)
        p1TxtField.grid(row=0, rowspan=3, column=0, sticky=N+W+S+E, columnspan=10)
        p1TxtField.insert(END, player1Data["name"].upper()+' LOG\n')
        p1TxtField.insert(END, "Your Avatar is: "+player1Data["avatar"]+'\n')
        
        p1YScrollBar.config(command=p1TxtField.yview)
        p1TxtField['state']=DISABLED
        p1Frame.pack(side=LEFT)

        def submit_movep1(row, col):
            if checkButtonState("player1"):
                try:
                    GAMEINSTANCE.setPlayerMoveInput("player1", row, col)
                    GAMEINSTANCE.updateGameBoard("player1")
                    # GAMEINSTANCE.drawGameBoard()
                    
                    index = str(row) + ","+ str(col)
                    print("\nINDEX: "+ index + " GAME ELEMENTS: ")
                    print(GAME_UI_ELEMENTS)
        
                    # Enable UI elements
                    GAME_UI_ELEMENTS["scoreTextField"]["state"] = NORMAL
                    PLAYER_UI_ELEMENTS["player1"]["textField"]["state"] = NORMAL

                    #
                    GAME_UI_ELEMENTS[index].config(text= GAMEINSTANCE.getPlayerAvatar("player1"))
                    GAME_UI_ELEMENTS["scoreTextField"].insert(INSERT, "\n" + player1Data["name"].upper() + " has moved into ROW: " + str(row) +" COL: "+str(col))
                    PLAYER_UI_ELEMENTS["player1"]["textField"].insert(INSERT, "\n"+str(GAMEINSTANCE.getPlayerMove("player1")))

                    # DISABLE
                    GAME_UI_ELEMENTS["scoreTextField"]["state"] = DISABLED
                    PLAYER_UI_ELEMENTS["player1"]["textField"]["state"] = DISABLED
                    
                    deactivatePlayerElements("player1")

                    # Check game win state
                    GAMEINSTANCE.checkWinState("player1")
                    GAMEINSTANCE.checkDrawState()

                    GAMEINSTANCE.drawGameBoard()

                    if(not GAMEINSTANCE._winCondition and not GAMEINSTANCE._drawState):
                        GAME_UI_ELEMENTS["scoreTextField"].insert(INSERT, "\nPlayer2's Move.")
                        activatePlayerElements("player2")
                        # PROMPT P2 TO GO

                    elif(GAMEINSTANCE._winCondition):
                        deactivatePlayerElements("player1")
                        deactivatePlayerElements("player2")
                        GAME_UI_ELEMENTS["scoreTextField"].insert(INSERT, printWinMessage("player1"))
                        GAMEINSTANCE.resetGame()

                    elif(GAMEINSTANCE._drawState):
                        deactivatePlayerElements("player1")
                        deactivatePlayerElements("player2")
                        GAME_UI_ELEMENTS["scoreTextField"].insert(INSERT, printDrawMessage())
                        GAMEINSTANCE.resetGame()

                except ValueError:
                    print("\n")
                    print("Invalid move. The board position you've selected is already taken.")
                    print("\n")
                except IndexError:
                    print("\n")
                    print("Invalid move. The board position you've selected is out of bounds.")
                    print("\n")
            
    
        # ROW 1
        p1button_11 = Button(p1Frame,text="1,1",command=lambda: submit_movep1(1,1),height=2,width=5)
        p1button_11.grid(row=4, column=2, sticky=N+W+S+E)
        p1button_12 = Button(p1Frame,text="1,2",command=lambda: submit_movep1(1,2),height=2,width=5)
        p1button_12.grid(row=4, column=3, sticky=N+W+S+E)
        p1button_13 = Button(p1Frame,text="1,3",command=lambda: submit_movep1(1,3),height=2,width=5)
        p1button_13.grid(row=4, column=4, sticky=N+W+S+E)

        # ROW 2
        p1button_21 = Button(p1Frame,text="2,1",command=lambda: submit_movep1(2,1),height=2,width=5)
        p1button_21.grid(row=5, column=2, sticky=N+W+S+E)
        p1button_22 = Button(p1Frame,text="2,2",command=lambda: submit_movep1(2,2),height=2,width=5)
        p1button_22.grid(row=5, column=3, sticky=N+W+S+E)
        p1button_23 = Button(p1Frame,text="2,3",command=lambda: submit_movep1(2,3),height=2,width=5)
        p1button_23.grid(row=5, column=4, sticky=N+W+S+E)

        # ROW 3
        p1button_31 = Button(p1Frame,text="3,1",command=lambda: submit_movep1(3,1),height=2,width=5)
        p1button_31.grid(row=6, column=2, sticky=N+W+S+E)
        p1button_32 = Button(p1Frame,text="3,2",command=lambda: submit_movep1(3,2),height=2,width=5)
        p1button_32.grid(row=6, column=3, sticky=N+W+S+E)
        p1button_33 = Button(p1Frame,text="3,3",command=lambda: submit_movep1(3,3),height=2,width=5)
        p1button_33.grid(row=6, column=4, sticky=N+W+S+E)
        
        PLAYER_UI_ELEMENTS["player1"]["1,1"] = p1button_11
        PLAYER_UI_ELEMENTS["player1"]["1,2"] = p1button_12
        PLAYER_UI_ELEMENTS["player1"]["1,3"] = p1button_13
        
        PLAYER_UI_ELEMENTS["player1"]["2,1"] = p1button_21
        PLAYER_UI_ELEMENTS["player1"]["2,2"] = p1button_22
        PLAYER_UI_ELEMENTS["player1"]["2,3"] = p1button_23

        PLAYER_UI_ELEMENTS["player1"]["3,1"] = p1button_31
        PLAYER_UI_ELEMENTS["player1"]["3,2"] = p1button_32
        PLAYER_UI_ELEMENTS["player1"]["3,3"] = p1button_33
        PLAYER_UI_ELEMENTS["player1"]["textField"] = p1TxtField

        print("P1 FRAME SETUP")


# Create the button layout for player 2
def setupP2Frame(top):
    
        player2Data = GAMEINSTANCE._playerDirectory["player2"]

        p2Frame=Frame(top, bd=3, relief=SUNKEN)
        p2YScrollBar = Scrollbar(p2Frame)
        p2YScrollBar.grid(row=0, rowspan=1, column=62, sticky=N+S+E)

        p2TxtField=Text(p2Frame, height=10, width=50, spacing3=8,
                    font=TkFont.Font(family="Helvetica", size=9, weight="bold"),
                    yscrollcommand=p2YScrollBar.set)    
        p2TxtField.grid(row=0, rowspan=3, column=52, sticky=N+W+S+E, columnspan=10)
        p2TxtField.insert(END, player2Data["name"].upper() +' LOG\n')
        p2TxtField.insert(END, "Your Avatar is: "+player2Data["avatar"]+'\n')
        # p2TxtField.tag_configure("even", background="#e0e0e0")
        # p2TxtField.tag_configure("odd", background="#ffffff")
        
        p2YScrollBar.config(command=p2TxtField.yview)
        def submit_movep2(row, col):
            if checkButtonState("player2"):
                try:
                    GAMEINSTANCE.setPlayerMoveInput("player2", row, col)
                    GAMEINSTANCE.updateGameBoard("player2")
                    
                    index = str(row) + ","+ str(col)
                    GAME_UI_ELEMENTS[index].config(text= GAMEINSTANCE.getPlayerAvatar("player2"))
                    
                    # p2TxtField.insert(INSERT, "\n"+str(GAMEINSTANCE.getPlayerMove("player2")))
                    
                    # Enable UI elements
                    GAME_UI_ELEMENTS["scoreTextField"]["state"] = NORMAL
                    PLAYER_UI_ELEMENTS["player2"]["textField"]["state"] = NORMAL

                    # update ui with game changes
                    GAME_UI_ELEMENTS[index].config(text= GAMEINSTANCE.getPlayerAvatar("player2"))
                    GAME_UI_ELEMENTS["scoreTextField"].insert(INSERT, "\n" + player2Data["name"].upper() + " has moved into ROW: " + str(row) +" COL: "+str(col))
                    PLAYER_UI_ELEMENTS["player2"]["textField"].insert(INSERT, "\n"+str(GAMEINSTANCE.getPlayerMove("player2")))

                    # DISABLE
                    GAME_UI_ELEMENTS["scoreTextField"]["state"] = DISABLED
                    PLAYER_UI_ELEMENTS["player2"]["textField"]["state"] = DISABLED
                    
                    deactivatePlayerElements("player2")

                    # Check game win state
                    GAMEINSTANCE.checkWinState("player2")
                    GAMEINSTANCE.checkDrawState()

                    if(not GAMEINSTANCE._winCondition and not GAMEINSTANCE._drawState):
                        GAME_UI_ELEMENTS["scoreTextField"].insert(INSERT, "\nPlayer1's Move.")
                        activatePlayerElements("player1")

                    elif(GAMEINSTANCE._winCondition):
                        deactivatePlayerElements("player1")
                        deactivatePlayerElements("player2")
                        GAME_UI_ELEMENTS["scoreTextField"].insert(INSERT, printWinMessage("player2"))
                        GAMEINSTANCE.playAgain()

                    elif(GAMEINSTANCE._drawState):
                        deactivatePlayerElements("player1")
                        deactivatePlayerElements("player2")
                        GAME_UI_ELEMENTS["scoreTextField"].insert(INSERT, printDrawMessage())
                        GAMEINSTANCE.playAgain()

                    GAMEINSTANCE.drawGameBoard()
                except ValueError:
                    print("\n")
                    print("Invalid move. The board position you've selected is already taken.")
                    print("\n")
                except IndexError:
                    print("\n")
                    print("Invalid move. The board position you've selected is out of bounds.")
                    print("\n")

        p2TxtField['state']=DISABLED
        p2Frame.pack(side=RIGHT)
        p2button_11 = Button(p2Frame,text="1,1",command=lambda: submit_movep2(1,1),height=2,width=5)
        p2button_11.grid(row=4, column=54, sticky=N+W+S+E)
        p2button_12 = Button(p2Frame,text="1,2",command=lambda: submit_movep2(1,2),height=2,width=5)
        p2button_12.grid(row=4, column=55, sticky=N+W+S+E)
        p2button_13 = Button(p2Frame,text="1,3",command=lambda: submit_movep2(1,3),height=2,width=5)
        p2button_13.grid(row=4, column=56, sticky=N+W+S+E)

        # ROW 2
        p2button_21 = Button(p2Frame,text="2,1",command=lambda: submit_movep2(2,1),height=2,width=5)
        p2button_21.grid(row=5, column=54, sticky=N+W+S+E)
        p2button_22 = Button(p2Frame,text="2,2",command=lambda: submit_movep2(2,2),height=2,width=5)
        p2button_22.grid(row=5, column=55, sticky=N+W+S+E)
        p2button_23 = Button(p2Frame,text="2,3",command=lambda: submit_movep2(2,3),height=2,width=5)
        p2button_23.grid(row=5, column=56, sticky=N+W+S+E)

        # ROW 3
        p2button_31 = Button(p2Frame,text="3,1",command=lambda: submit_movep2(3,1),height=2,width=5)
        p2button_31.grid(row=6, column=54, sticky=N+W+S+E)
        p2button_32 = Button(p2Frame,text="3,2",command=lambda: submit_movep2(3,2),height=2,width=5)
        p2button_32.grid(row=6, column=55, sticky=N+W+S+E)
        p2button_33 = Button(p2Frame,text="3,3",command=lambda: submit_movep2(3,3),height=2,width=5)
        p2button_33.grid(row=6, column=56, sticky=N+W+S+E)
        
        PLAYER_UI_ELEMENTS["player2"]["1,1"] = p2button_11
        PLAYER_UI_ELEMENTS["player2"]["1,2"] = p2button_12
        PLAYER_UI_ELEMENTS["player2"]["1,3"] = p2button_13
        
        PLAYER_UI_ELEMENTS["player2"]["2,1"] = p2button_21
        PLAYER_UI_ELEMENTS["player2"]["2,2"] = p2button_22
        PLAYER_UI_ELEMENTS["player2"]["2,3"] = p2button_23

        PLAYER_UI_ELEMENTS["player2"]["3,1"] = p2button_31
        PLAYER_UI_ELEMENTS["player2"]["3,2"] = p2button_32
        PLAYER_UI_ELEMENTS["player2"]["3,3"] = p2button_33

        PLAYER_UI_ELEMENTS["player2"]["textField"] = p2TxtField


# Setup the UI for the log of game data and activity
def setupGameScoreLog(top):
        scoreLogFrame = Frame(top, bd=3, relief=SUNKEN)
        scoreYScrollBar = Scrollbar(scoreLogFrame)
        scoreYScrollBar.grid(row=4, rowspan=3, column=51, sticky=N+S)
        score=Text(scoreLogFrame,  bd=2, height=15, yscrollcommand=scoreYScrollBar.set,
                font=TkFont.Font(family="Helvetica", size=9, weight="bold"), wrap=WORD, pady=11)    
        score.grid(row=5, rowspan=2, column=0, sticky=N+W+S+E, columnspan=1)   
        score.insert(END, 'GAME LOG\n')

        score.tag_configure("even", background="#e0e0e0")
        score.tag_configure("odd", background="#ffffff")

        def hglghtHazzards():
            lastline = score.index("end-1c").split(".")[0]
            tag = "odd"
            for i in range(1, int(lastline)):
                score.tag_add(tag, "%s.0" % i, "%s.0" % (i+1))
                tag = "even" if tag == "odd" else "odd"

        scoreYScrollBar.config(command=score.yview)
        score['state']=DISABLED
        scoreLogFrame.pack(side=BOTTOM)

        GAME_UI_ELEMENTS["scoreTextField"] = score


def clear_default(event):
    event.widget.delete(0, 'end')
    event.widget.unbind('<FocusIn>')


def getUserInput():
    #Create an instance of Tkinter frame
    win= Tk()
    win.title("Y.F. TECH GAMES")
    #Set the geometry of Tkinter frame
    win.geometry("500x250")

    # declaring string variable
    # for storing name and password
    p1_Name=StringVar()
    p1_Avatar=StringVar()

    # declaring string variable
    # for storing name and password
    p2_Name=StringVar()
    p2_Avatar=StringVar()

    p1Label=Label(win, text="Player1 Info", font=("Helvetica 18 bold"))
    p1NameLabel = Label(win, text = "Player1 Name: ", font=('calibre',10, 'bold'))
    p1EntryLabel = Label(win, text = "Player1 Avatar: ", font=('calibre',10, 'bold'))
    
    #Create an Entry widget to accept User Input
    player1NameEntry= Entry(win, width= 40, textvariable = p1_Name)
    player1NameEntry.focus_set()
    player1NameEntry.insert(0, 'Player1 Name')
    player1NameEntry.bind('<FocusIn>', clear_default)
    
    #Create an Entry widget to accept User Input
    player1AvatarEntry= Entry(win, width= 40, textvariable = p1_Avatar)
    player1AvatarEntry.focus_set()
    player1AvatarEntry.insert(0, 'Player1 Avatar')
    player1AvatarEntry.bind('<FocusIn>', clear_default)

    p2Label=Label(win, text="Player2 Info", font=("Helvetica 18 bold"))
    p2NameLabel = Label(win, text = "Player2 Name: ", font=('calibre',10, 'bold'))
    p2EntryLabel = Label(win, text = "Player2 Avatar: ", font=('calibre',10, 'bold'))

    #Create an Entry widget to accept User Input
    player2NameEntry= Entry(win, width= 40, textvariable = p2_Name)
    player2NameEntry.focus_set()
    player2NameEntry.insert(0, 'Player2 Name')
    player2NameEntry.bind('<FocusIn>', clear_default)

    #Create an Entry widget to accept User Input
    player2AvatarEntry= Entry(win, width= 40, textvariable = p2_Avatar)
    player2AvatarEntry.focus_set()
    player2AvatarEntry.insert(0, 'Player2 Avatar')
    player2AvatarEntry.bind('<FocusIn>', clear_default)

    p1Label.grid(row=0,column=0)
    p1NameLabel.grid(row=1,column=0)
    player1NameEntry.grid(row=1,column=1)
    p1EntryLabel.grid(row=2,column=0)
    player1AvatarEntry.grid(row=2,column=1)

    p2Label.grid(row=4,column=0, padx=10, pady=10)
    p2NameLabel.grid(row=5,column=0)
    player2NameEntry.grid(row=5,column=1)
    p2EntryLabel.grid(row=6,column=0)
    player2AvatarEntry.grid(row=6,column=1)

    def character_limit(entry_text):
        if len(entry_text.get()) > 0:
            entry_text.set(entry_text.get()[-1])

    def name_character_limit(entry_text):
            if len(entry_text.get()) > 20:
                entry_text.set(entry_text.get()[19])

    p1_Avatar.trace("w", lambda *args: character_limit(p1_Avatar))
    p2_Avatar.trace("w", lambda *args: character_limit(p2_Avatar))

    p1_Name.trace("w", lambda *args: name_character_limit(p1_Name))
    p2_Name.trace("w", lambda *args: name_character_limit(p2_Name))

    def start_game():
        GAMEINSTANCE._playerDirectory["player1"]["name"] = p1_Name.get()
        GAMEINSTANCE._playerDirectory["player1"]["avatar"] = p1_Avatar.get()
        
        GAMEINSTANCE._playerDirectory["player2"]["name"] = p2_Name.get()
        GAMEINSTANCE._playerDirectory["player2"]["avatar"] = p2_Avatar.get()
        
        win.destroy()

    #Create a Button to validate Entry Widget
    Button(win, text= "START GAME",width= 20, command=start_game).grid(row=8, column=1, padx=20, pady=20)
    win.mainloop()

def setupGameUI(top):
        ##############################################TIC-TAC-TOE GAME VIEW##########################################################
        # setupGameBoardButtons(top)
        frame = Frame(top, bd=3, relief=SUNKEN)
        frame.grid_rowconfigure(0, weight=1, minsize=1)
        frame.grid_columnconfigure(0, weight=2, minsize=1)

        # ROW 1
        button_11 = Button(frame,text="--",command="",height=7,width=15)
        button_11.grid(row=0, column=0, sticky=N+S+W+E)
        button_12 = Button(frame,text="--",command="",height=7,width=15)
        button_12.grid(row=0, column=1, sticky=N+S+W+E)
        button_13 = Button(frame,text="--",command="",height=7,width=15)
        button_13.grid(row=0, column=2, sticky=N+S+W+E)

        # ROW 2
        button_21 = Button(frame,text="--",command="",height=7,width=15)
        button_21.grid(row=1, column=0, sticky=N+S+W+E)
        button_22 = Button(frame,text="--",command="",height=7,width=15)
        button_22.grid(row=1, column=1, sticky=N+S+W+E)
        button_23 = Button(frame,text="--",command="",height=7,width=15)
        button_23.grid(row=1, column=2, sticky=N+S+W+E)

        # ROW 3
        button_31 = Button(frame,text="--",command="",height=7,width=15)
        button_31.grid(row=2, column=0, sticky=N+S+W+E)
        button_32 = Button(frame,text="--",command="",height=7,width=15)
        button_32.grid(row=2, column=1, sticky=N+S+W+E)
        button_33 = Button(frame,text="--",command="",height=7,width=15)
        button_33.grid(row=2, column=2, sticky=N+S+W+E)
        frame.pack()

        GAME_UI_ELEMENTS["1,1"] = button_11
        GAME_UI_ELEMENTS["1,2"] = button_12
        GAME_UI_ELEMENTS["1,3"] = button_13
        
        GAME_UI_ELEMENTS["2,1"] = button_21
        GAME_UI_ELEMENTS["2,2"] = button_22
        GAME_UI_ELEMENTS["2,3"] = button_23

        GAME_UI_ELEMENTS["3,1"] = button_31
        GAME_UI_ELEMENTS["3,2"] = button_32
        GAME_UI_ELEMENTS["3,3"] = button_33
        ##############################################TIC-TAC-TOE GAME VIEW##########################################################
#
# Game Loop No UI
#
# Main Game loop that will control the flow of the game
# The game opbject holds all necessary functions to play the game

    
def main()->int:
    reply = messagebox.askyesno('confirmation', 'Are you sure you want to launch Tic-Tac-Toe ?')
    if reply == True:
        messagebox.showinfo('successful','Enter the Display Name and avatar for Player 1 & 2 next!\n')
        
        getUserInput()
        # setUpGameUI()
        top = Tk()
        top.title("Y.F. TECH GAMES")
        top.resizable(TRUE,TRUE)
        # top.resizable(False,False)
        
        ##############################################TIC-TAC-TOE GAME VIEW##########################################################
        setupGameUI(top)
        ##############################################TIC-TAC-TOE GAME VIEW##########################################################

        ##############################################PLAYER 1 LOG##########################################################
        setupP1Frame(top)
        ##############################################PLAYER 1 LOG##########################################################

        ##############################################PLAYER 2 BUTTONS##########################################################
        setupP2Frame(top)
        ##############################################PLAYER 2 BUTTONS##########################################################
    
        ##############################################SCORE LOG##########################################################
        setupGameScoreLog(top)
        ##############################################SCORE LOG##########################################################
        
        print("POST SETTING UP UI")
        print("SETTING UP MUSIC")
        try:
            play()
        except pygame.error as e:
            print("Caught Pygame error")
            print(e)

        player1Name = GAMEINSTANCE._playerDirectory["player1"]["name"]
        player1Avatar = GAMEINSTANCE._playerDirectory["player1"]["avatar"]

        player2Name = GAMEINSTANCE._playerDirectory["player2"]["name"]
        player2Avatar = GAMEINSTANCE._playerDirectory["player2"]["avatar"]

        # Post setting up UI, we want to set things up to flow as the game begins. 
        # Activate P1's buttons
        GAME_UI_ELEMENTS["scoreTextField"].insert(INSERT, "\nPlayer1 " + player1Name.upper() + "'s Move.")
        activatePlayerElements("player1")
        deactivatePlayerElements("player2")

        top.mainloop()
    else:
        messagebox.showinfo('', 'Maybe next time!')
    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit