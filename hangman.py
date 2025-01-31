from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import random
import math

root = Tk()
root.title("Hangman")

word_list = [
    # "cat",
    # "dog",
    # "giraffe",
    # "car",
    # "road",
    # "computer",
    # "keyboard",
    # "pizza",
    # "island",
    # "country",
    "car"
]
game_word = random.choice(word_list)

hangman_img = ImageTk.PhotoImage(Image.open("images/hangman1.png"))
imgLabel = Label(image=hangman_img)
imgLabel.grid(row=0, column=0)

number_of_guesses = 0

user_input = StringVar()


def game_over():
    global number_of_guesses
    global hangman_img
    global game_word

    messagebox.showinfo("Game Over", "Your game is over, try again")
    number_of_guesses = 0
    hangman_img = ImageTk.PhotoImage(Image.open("images/hangman1.png"))
    imgLabel = Label(image=hangman_img)
    imgLabel.grid(row=0, column=0)


def submit():
    global number_of_guesses
    global hangman_img

    number_of_guesses += 1

    hangman_img = ImageTk.PhotoImage(
        Image.open("images/hangman" + str(number_of_guesses + 1) + ".png")
    )
    imgLabel = Label(image=hangman_img)
    imgLabel.grid(row=0, column=0)

    value = user_input.get()
    print(
        value, number_of_guesses, "images/hangman" + str(number_of_guesses + 1) + ".png"
    )
    user_input.set("")

    if number_of_guesses >= 8:
        root.update_idletasks()
        game_over()
        return


middle_frame = Frame(root, padx=10, pady=10)
middle_frame.grid(row=1, column=0)

for i in range(0, len(game_word)):
    Label(
        middle_frame,
        text=game_word[i],
        border=2,
        pady=5,
        padx=15,
        font=("Arial", 25),
        relief="solid",
    ).grid(row=0, column=i, pady=10)

bottom_frame = Frame(root, padx=10, pady=10)
bottom_frame.grid(row=2, column=0, sticky="nsew")

label = Label(bottom_frame, text="Enter your guess")
entry = Entry(bottom_frame, textvariable=user_input)
submit_button = Button(bottom_frame, text="Submit", command=submit)

label.grid(row=0, column=0)
entry.grid(row=0, column=1)
submit_button.grid(row=0, column=2)

root.mainloop()
