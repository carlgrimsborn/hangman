from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import random
from collections import Counter

root = Tk()
root.title("Hangman")

word_list = [
    "cat",
    "dog",
    "giraffe",
    "car",
    "road",
    "computer",
    "keyboard",
    "pizza",
    "island",
    "country",
    "car",
]
game_word = random.choice(word_list)
correct_guessed_dict = {}
prev_correct_words = []

hangman_img = ImageTk.PhotoImage(Image.open("images/hangman1.png"))
imgLabel = Label(image=hangman_img)
imgLabel.grid(row=0, column=0)

number_of_guesses = 0

user_input = StringVar()


def validate_win():
    global correct_guessed_dict
    global game_word

    game_word_counter = Counter(game_word)
    return game_word_counter == correct_guessed_dict


def set_guessed_dict(str):
    global correct_guessed_dict
    for c in str:
        if c in game_word:
            correct_guessed_dict[c] = game_word.count(c)
    print(correct_guessed_dict)


def validate_guess(guess_str):
    global correct_guessed_dict

    for c in correct_guessed_dict.keys():
        if c in guess_str:
            return True
    return False


def game_over(completed):
    global number_of_guesses
    global hangman_img
    global game_word
    global correct_guessed_dict
    global word_list
    global middle_frame
    global prev_correct_words
    global completed_lbl
    global completed_words_text

    print("game_word", game_word)
    if completed:
        messagebox.showinfo("Game Completed!", "Congrats. You guessed the right word")
        prev_correct_words.append(game_word)
        completed_words_text = ", ".join(prev_correct_words)
        completed_lbl = Label(
            root, text="Completed words: " + completed_words_text
        ).grid(row=3, column=0)
    else:
        messagebox.showinfo(
            "Game Over", "Your game is over, try again. Right word was: " + game_word
        )

    game_word = random.choice(word_list)
    correct_guessed_dict = {}
    number_of_guesses = 0

    hangman_img = ImageTk.PhotoImage(Image.open("images/hangman1.png"))
    imgLabel = Label(image=hangman_img)
    imgLabel.grid(row=0, column=0)
    middle_frame.grid_forget()
    middle_frame = Frame(root, padx=10, pady=10)
    middle_frame.grid(row=1, column=0)
    renderLabels()


def submit():
    global number_of_guesses
    global hangman_img
    global correct_guessed_dict

    input_value = user_input.get()
    set_guessed_dict(input_value)
    correct_guess = validate_guess(input_value)

    if correct_guess == False:
        root.update_idletasks()
        number_of_guesses += 1
        hangman_img = ImageTk.PhotoImage(
            Image.open("images/hangman" + str(number_of_guesses + 1) + ".png")
        )
        imgLabel = Label(image=hangman_img)
        imgLabel.grid(row=0, column=0)

    renderLabels()

    user_input.set("")
    completed_game = validate_win()

    if completed_game:
        root.update_idletasks()
        game_over(completed=True)
        return
    elif number_of_guesses >= 8:
        root.update_idletasks()
        game_over(completed=False)
        return


middle_frame = Frame(root, padx=10, pady=10)
middle_frame.grid(row=1, column=0)


def renderLabels():
    for i in range(0, len(game_word)):
        lbl_char = ""
        if game_word[i] in correct_guessed_dict:
            lbl_char = game_word[i]
        Label(
            middle_frame,
            text=lbl_char,
            border=2,
            pady=5,
            padx=15,
            font=("Arial", 25),
            relief="solid",
        ).grid(row=0, column=i, pady=10)


renderLabels()

bottom_frame = Frame(root, padx=10, pady=10)
bottom_frame.grid(row=2, column=0, sticky="nsew")

label = Label(bottom_frame, text="Enter your guess")
entry = Entry(bottom_frame, textvariable=user_input)
submit_button = Button(bottom_frame, text="Submit", command=submit)

label.grid(row=0, column=0)
entry.grid(row=0, column=1)
submit_button.grid(row=0, column=2)

root.mainloop()
