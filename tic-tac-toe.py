from tkinter import messagebox
import random
import tkinter as tk

Tictactoe = tk.Tk()          
Tictactoe.geometry("800x600")

mode = "player"
Tictactoe.resizable(False, False)

top_frame = tk.Frame(Tictactoe, width=800, height=150, bg="#002147", bd=20 )
top_frame.pack()
top_frame.pack_propagate(False)

left_frame = tk.Frame(Tictactoe, width=200, height=600, bg="black")
left_frame.pack(side="left")
left_frame.pack_propagate(False)

label= tk.Label(top_frame, text="TIC-TAC-TOE GAME!", font=("Century",20), bg="#002147", fg="white" )
label.pack(expand=True) 

mode_frame = tk.Frame(Tictactoe)
mode_frame.pack(pady=10)

player_button = tk.Button(mode_frame, text="2 Player", font=("Century",12), command=lambda:set_mode("player"))
player_button.grid(row=0, column=0, padx=10)

pc_button = tk.Button(mode_frame, text="Play vs PC", font=("Century",12), command=lambda:set_mode("pc"))
pc_button.grid(row=0, column=1, padx=10)

instruction = tk.Label(left_frame, text="Instructions:\n 1) 2 opponents should be there\n2)Each opponent will \ndecide their symbol O or X\n" \
"3)Click the box to mark \nyour position\n4)Person to first align \ntheir symbol in a row,column or\n diagonally will win",
bg="black", fg="white", justify="left",anchor="w")
instruction.pack(pady=20)

board_frame = tk.Frame(Tictactoe, width=450, height=350, bg="blue", bd=5, relief="solid")
board_frame.pack(pady=20)
board_frame.pack_propagate(False)

def set_mode(m):
    global mode
    mode=m

Button = [[None]*3 for _ in range(3)]

for row in range(3):
    for column in range(3):
     Button[row][column] = tk.Button(board_frame, width=5, height=2, font=("Century",20), relief="solid")
     Button[row][column].config(command=lambda r=row, c=column: button_click(r,c))
     Button[row][column].grid(row=row, column=column)

global board
board = [[" " for x in range(3)] for y in range(3)]

sign=0
current_player="X"
def winner(b, l):

    if b[0][0]==l and b[0][1]==l and b[0][2]==l:
        Button[0][0].config(bg="lightblue")
        Button[0][1].config(bg="lightblue")
        Button[0][2].config(bg="lightblue")
        return True

    if b[1][0]==l and b[1][1]==l and b[1][2]==l:
        Button[1][0].config(bg="lightblue")
        Button[1][1].config(bg="lightblue")
        Button[1][2].config(bg="lightblue")
        return True

    if b[2][0]==l and b[2][1]==l and b[2][2]==l:
        Button[2][0].config(bg="lightblue")
        Button[2][1].config(bg="lightblue")
        Button[2][2].config(bg="lightblue")
        return True

    if b[0][0]==l and b[1][0]==l and b[2][0]==l:
        Button[0][0].config(bg="lightblue")
        Button[1][0].config(bg="lightblue")
        Button[2][0].config(bg="lightblue")
        return True

    if b[0][1]==l and b[1][1]==l and b[2][1]==l:
        Button[0][1].config(bg="lightblue")
        Button[1][1].config(bg="lightblue")
        Button[2][1].config(bg="lightblue")
        return True

    if b[0][2]==l and b[1][2]==l and b[2][2]==l:
        Button[0][2].config(bg="lightblue")
        Button[1][2].config(bg="lightblue")
        Button[2][2].config(bg="lightblue")
        return True

 
    if b[0][0]==l and b[1][1]==l and b[2][2]==l:
        Button[0][0].config(bg="lightblue")
        Button[1][1].config(bg="lightblue")
        Button[2][2].config(bg="lightblue")
        return True

  
    if b[0][2]==l and b[1][1]==l and b[2][0]==l:
        Button[0][2].config(bg="lightblue")
        Button[1][1].config(bg="lightblue")
        Button[2][0].config(bg="lightblue")
        return True

def isfull():
    for row in board:
        if " " in row:
            return False
    return True

def disable_board():
    for i in range(3):
        for j in range(3):
            Button[i][j].config(state="disabled")

def button_click(i,j):
    global sign, current_player

    if board[i][j] == " ":
        
        if mode == "pc":
            board[i][j] = "X"
        else:
            if sign % 2 == 0:
                board[i][j] = "X"
            else:
                board[i][j] = "O"

        sign += 1
        Button[i][j].config(text=board[i][j])

        if winner(board,"X"):
            messagebox.showinfo("Winner","Player 1 Wins")
            disable_board()
            return

    if mode == "pc":
        empty_cells=[]
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    empty_cells.append((r,c))
                    
        if empty_cells:
            r,c = random.choice(empty_cells)
            
            board[r][c] = "O"
            Button[r][c].config(text="O")
            sign +=1
            
            if winner(board, "O"):
                messagebox.showinfo("Winner", "Computer Wins")
                disable_board()
                return
                
    if winner(board, "X"):
        box = messagebox.showinfo("Winner", "Player 1 Wins")
        
    elif winner(board, "O"):
        box = messagebox.showinfo("Winner", "Player 2 Wins")
    elif isfull():
        box = messagebox.showinfo("Tie Game", "Tie Game")
        disable_board()
    

def reset_game():
    global board, sign

    sign = 0

    for i in range(3):
        for j in range(3):
            board[i][j] = " "
            Button[i][j].config(text="", bg="SystemButtonFace", state="normal")

reset_btn = tk.Button(Tictactoe, text="Reset Game", font=("Century",14), bg="#002147", fg="white", command=reset_game)
reset_btn.pack(pady=10)


Tictactoe.mainloop()