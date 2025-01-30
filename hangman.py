from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Hangman")

wordList = ["cat", "dog", "giraffe", "car", "road", "computer"]

hangman_img = ImageTk.PhotoImage(Image.open("images/hangman1.png"))
imgLabel = Label(image=hangman_img)
imgLabel.grid(row=0, column=0, columnspan=5)

number_of_guesses = 0

user_input = StringVar()


def game_over():
    global number_of_guesses
    global hangman_img

    messagebox.showinfo("Game Over", "Your game is over, try again")
    number_of_guesses = 0
    hangman_img = ImageTk.PhotoImage(Image.open("images/hangman1.png"))
    imgLabel = Label(image=hangman_img)
    imgLabel.grid(row=0, column=0, columnspan=5)


def submit():
    global number_of_guesses
    global hangman_img

    number_of_guesses += 1

    hangman_img = ImageTk.PhotoImage(
        Image.open("images/hangman" + str(number_of_guesses + 1) + ".png")
    )
    imgLabel = Label(image=hangman_img)
    imgLabel.grid(row=0, column=0, columnspan=5)

    value = user_input.get()
    print(
        value, number_of_guesses, "images/hangman" + str(number_of_guesses + 1) + ".png"
    )
    user_input.set("")

    if number_of_guesses >= 8:
        root.update_idletasks()
        game_over()
        return


label = Label(root, text="Enter your guess")
entry = Entry(root, textvariable=user_input, width=30)
submit_button = Button(root, text="Submit", command=submit)

label.grid(row=1, column=0)
entry.grid(row=1, column=1)
submit_button.grid(row=1, column=2)

root.mainloop()
