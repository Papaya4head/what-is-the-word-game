import random
import tkinter as tk
from tkinter import messagebox

def choose_word():
    words = ["cat", "dog", "car", "programming", "code", "python", "laptop", "word", "phone", "papaya"]
    return random.choice(words)

def word_status(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def update_display(word, guessed_letters):
    """Updates the secret word display with correctly guessed letters and underscores."""
    secret_word_label.config(text=word_status(word, guessed_letters))

def update_attempts(attempts):
    """Updates the attempts remaining label."""
    attempts_label.config(text=f"Attempts Remaining: {attempts}")

def handle_guess(guess):
    """Processes a user's guess, updating display, attempts, and checking for win/loss."""
    global secret_word, guessed_letters, attempts

    if len(guess) != 1 or not guess.isalpha():
        return  # Invalid input (not a single letter or not alphabetic)

    if guess in guessed_letters:
        return  # Letter already guessed

    guessed_letters.append(guess)

    if guess not in secret_word:
        attempts -= 1
        update_attempts(attempts)
        message_label.config(text=f"Incorrect: '{guess}' isn't in the word.")
    else:
        occurrences = secret_word.count(guess)
        message_label.config(text=f"Correct: '{guess}' appears {occurrences} time(s).")

    update_display(secret_word, guessed_letters)

    if "_" not in word_status(secret_word, guessed_letters):
        message_label.config(text="Congratulations! You guessed the word!")
        guess_entry.config(state="disabled")
        guess_button.config(state="disabled")
    elif attempts == 0:
        message_label.config(text=f"You ran out of attempts. The word was: {secret_word}")
        guess_entry.config(state="disabled")
        guess_button.config(state="disabled")

def start_game():
    """Resets the game for a new round."""
    global secret_word, guessed_letters, attempts
    secret_word = choose_word()
    guessed_letters = []
    attempts = 7

    update_display(secret_word, guessed_letters)
    update_attempts(attempts)
    message_label.config(text="")
    guess_entry.config(state="normal")  # Enable guess entry
    guess_button.config(state="normal")  # Enable guess button

# Initialize the game
secret_word = choose_word()
guessed_letters = []
attempts = 7

# Create the main window
root = tk.Tk()
root.title("Word Guessing Game")

# Color schemes
bg_color = "#f0f0f0"
button_color = "#4CAF50"
text_color = "#333333"

# Set background color
root.configure(bg=bg_color)

# Secret word display label
secret_word_label = tk.Label(root, text=word_status(secret_word, guessed_letters), font=("Arial", 20), bg=bg_color, fg=text_color)
secret_word_label.pack(pady=20)

# Attempts remaining label
attempts_label = tk.Label(root, text=f"Attempts Remaining: {attempts}", font=("Arial", 12), bg=bg_color, fg=text_color)
attempts_label.pack()

# Message label for feedback
message_label = tk.Label(root, text="", font=("Arial", 12), bg=bg_color, fg=text_color)
message_label.pack()

# Guess entry
guess_entry = tk.Entry(root, width=10, font=("Arial", 12))
guess_entry.pack(pady=10)

# Guess button with animation effect
def animate_button(widget):
    widget.config(relief="sunken")
    widget.after(100, lambda: widget.config(relief="raised"))

guess_button = tk.Button(root, text="Guess", command=lambda: handle_guess(guess_entry.get().lower()), font=("Arial", 12), bg=button_color, fg="white")
guess_button.pack(pady=10)
guess_button.config(command=lambda: [handle_guess(guess_entry.get().lower()), animate_button(guess_button)])

# Start game button with animation effect
start_game_button = tk.Button(root, text="Start New Game", command=start_game, font=("Arial", 12), bg=button_color, fg="white")
start_game_button.pack(pady=10)
start_game_button.config(command=lambda: [start_game(), animate_button(start_game_button)])

# Run the main event loop
root.mainloop()
