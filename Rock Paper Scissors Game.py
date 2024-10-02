import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
 
# Main Application Window
root = tk.Tk()
root.title("Rock, Paper, Scissors")
 
# Global variables to keep track of the scores
wins = 0
losses = 0
ties = 0
 
# Load images (make sure you have these images in the same directory)
rock_img = ImageTk.PhotoImage(Image.open("rock.png").resize((100, 100)))
paper_img = ImageTk.PhotoImage(Image.open("paper.png").resize((100, 100)))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.png").resize((100, 100)))
images = {"ROCK": rock_img, "PAPER": paper_img, "SCISSORS": scissors_img}
 
def play_game(player_move):
    global wins, losses, ties
    result_label.config(text="Choosing...", font=("Helvetica", 16))
    player_label.config(image=images[player_move])
 
    # Simulate some delay for animation effect
    root.after(1000, reveal_result, player_move)
 
def reveal_result(player_move):
    global wins, losses, ties
    computer_move = random.choice(['ROCK', 'PAPER', 'SCISSORS'])
    computer_label.config(image=images[computer_move])
 
    # Determine the outcome
    if player_move == computer_move:
        result = "It's a tie!"
        ties += 1
    elif (player_move == 'ROCK' and computer_move == 'SCISSORS') or \
         (player_move == 'PAPER' and computer_move == 'ROCK') or \
         (player_move == 'SCISSORS' and computer_move == 'PAPER'):
        result = "You win!"
        wins += 1
    else:
        result = "You lose!"
        losses += 1
 
    result_label.config(text=f"{result}")
    score_label.config(text=f"Wins: {wins} Losses: {losses} Ties: {ties}")
 
def on_click_rock(event):
    play_game('ROCK')
 
def on_click_paper(event):
    play_game('PAPER')
 
def on_click_scissors(event):
    play_game('SCISSORS')
 
def quit_game():
    # Confirm exit
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
 
# Create Labels and Buttons
title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Helvetica", 16))
title_label.pack(pady=10)
 
result_label = tk.Label(root, text="Make your move!", font=("Helvetica", 12))
result_label.pack(pady=10)
 
score_label = tk.Label(root, text=f"Wins: {wins} Losses: {losses} Ties: {ties}", font=("Helvetica", 12))
score_label.pack(pady=10)
 
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
 
# Player and Computer image labels
player_label = tk.Label(root)
player_label.pack(side="left", padx=20)
 
computer_label = tk.Label(root)
computer_label.pack(side="right", padx=20)
 
# Image labels that act as clickable buttons
rock_label = tk.Label(button_frame, image=rock_img)
rock_label.grid(row=0, column=0, padx=5)
rock_label.bind("<Button-1>", on_click_rock)  # Bind click event to the rock image
 
paper_label = tk.Label(button_frame, image=paper_img)
paper_label.grid(row=0, column=1, padx=5)
paper_label.bind("<Button-1>", on_click_paper)  # Bind click event to the paper image
 
scissors_label = tk.Label(button_frame, image=scissors_img)
scissors_label.grid(row=0, column=2, padx=5)
scissors_label.bind("<Button-1>", on_click_scissors)  # Bind click event to the scissors image
 
# Quit button
quit_button = tk.Button(root, text="Quit", width=10, command=quit_game)
quit_button.pack(pady=10)
 
# Start the application
root.mainloop()
