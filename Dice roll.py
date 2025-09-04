import tkinter as tk
import random


class DiceRollerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎲 Dice Rolling Simulator")
        self.root.geometry("400x500")

        self.dice_types = [4, 6, 8, 10, 12, 20, 100]
        self.selected_dice = tk.IntVar(value=6)

        tk.Label(root, text="Choose a Dice:", font=("Arial", 12)).pack(pady=5)
        self.dice_menu = tk.OptionMenu(root, self.selected_dice, *self.dice_types)
        self.dice_menu.pack(pady=5)

        self.roll_button = tk.Button(root, text="Roll Dice", command=self.start_roll, font=("Arial", 12))
        self.roll_button.pack(pady=10)

        self.result_label = tk.Label(root, text="Roll a dice!", font=("Arial", 14), fg="blue")
        self.result_label.pack(pady=10)

        tk.Label(root, text="Roll History:", font=("Arial", 12, "bold")).pack()
        self.history_box = tk.Listbox(root, width=30, height=15)
        self.history_box.pack(pady=5)

        self.clear_button = tk.Button(root, text="Clear History", command=self.clear_history, font=("Arial", 12))
        self.clear_button.pack(pady=10)

        self.animation_count = 0  # for animation steps

    def start_roll(self):
        self.animation_count = 0
        self.animate_roll()

    def animate_roll(self):
        dice_sides = self.selected_dice.get()
        roll = random.randint(1, dice_sides)
        self.result_label.config(text=f"Rolling... {roll}")
        self.animation_count += 1

        if self.animation_count < 15:  # number of "spin" frames
            self.root.after(80, self.animate_roll)  # keep rolling
        else:
            # Final result
            self.result_label.config(text=f"🎲 Rolled a d{dice_sides}: {roll}")
            self.history_box.insert(tk.END, f"d{dice_sides} → {roll}")

    def clear_history(self):
        self.history_box.delete(0, tk.END)
        self.result_label.config(text="Roll a dice!")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiceRollerApp(root)
    root.mainloop()




    
