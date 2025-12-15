import tkinter as tk
import random

root = tk.Tk()
root.title("Rzut kostką")

dice_images = [
   
    tk.PhotoImage(file=f"assets/{i}.png") for i in range(1, 7)
]


def roll_dice():
    result = random.randint(0, 5)
    dice_label.config(image=dice_images[result])
    dice_label.image = dice_images[result]  

dice_label = tk.Label(root, image=dice_images[0])
dice_label.pack(pady=20)

roll_button = tk.Button(root, text="Rzuć kostką", command=roll_dice)
roll_button.pack(pady=10)

root.mainloop()
