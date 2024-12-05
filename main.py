# https://www.github.com/ninjaytxz/Shrimp-Detector-Meme
import tkinter as tk
from tkinter import PhotoImage, messagebox
import threading
import pygame  # For playing sound

pygame.mixer.init()

def show_popup():
    response = messagebox.askquestion("Shrimp Detector", "Are you a shrimp?")
    if response == 'yes': #'No' doesn't do anything
        show_image_and_sound()

def play_sound():
    pygame.mixer.music.load("assets/laugh.mp3")  # Load the sound file
    pygame.mixer.music.play()  # Play the sound

def show_image_and_sound():
    new_window = tk.Toplevel()
    new_window.title("HAHA SHRIMP")
    new_window.geometry("1200x680")
    icon2 = PhotoImage(file="assets/shrimp.png")
    new_window.iconphoto(False, icon2)

    # Load and display the image
    image = PhotoImage(file="assets/shrimplol.png")
    label = tk.Label(new_window, image=image)
    label.image = image  # Prevent garbage collection
    label.pack()

    new_window.after(0, lambda: threading.Thread(target=play_sound, daemon=True).start())

root = tk.Tk()
root.geometry("800x540")
icon = PhotoImage(file="assets/shrimp.png")
root.iconphoto(False, icon)
root.resizable(False, False)

# Load and display the background image
image = PhotoImage(file="assets/shrimp detector.png")
canvas = tk.Canvas(root, width=800, height=540)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=image, anchor="nw")

button = tk.Button(root, text="start detection", font=("Arial", 17), command=show_popup)
button_window = canvas.create_window(420, 406, anchor="center", window=button, height=80, width=180)


root.title("Shrimp Detector")
root.mainloop()
