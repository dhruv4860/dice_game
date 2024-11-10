import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# ASCII art representation of dice faces
DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}

def roll_dice():
    """Simulate rolling a 6-sided die and return the result."""
    return random.randint(1, 6)

def display_dice(die_value):
    """Return the ASCII art for the given die value."""
    if die_value in DICE_ART:
        return "\n".join(DICE_ART[die_value])
    return ""

def play_game():
    """Roll the dice for both user and computer and display results."""
    user_value = roll_dice()
    computer_value = roll_dice()

    user_dice_art = display_dice(user_value)
    computer_dice_art = display_dice(computer_value)

    result_message = f"You rolled:\n{user_dice_art}\n\nThe computer rolled:\n{computer_dice_art}\n"

    # Determine the winner
    if user_value > computer_value:
        result_message += "user win!"
    elif user_value < computer_value:
        result_message += "The computer wins!"
    else:
        result_message += "It's a tie!"

    messagebox.showinfo("Game Result", result_message)

# Create the main window
root = tk.Tk()
root.title("Dice Rolling Game")



# Load background image
background_image = Image.open(r"C:\Users\Dhruv Rana\OneDrive\Desktop\projects\terminal-dice-roller-main\img\background2.jpg")  
background_photo = ImageTk.PhotoImage(background_image)

# Create a label for the background image
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a button to roll the dice
roll_button = tk.Button(root, text="Roll the Dice", command=play_game, font=('Arial', 16))
roll_button.place(x=100,y=50)

# Run the application
root.mainloop()
