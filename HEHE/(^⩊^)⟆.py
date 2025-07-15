import tkinter as tk
from tkinter import messagebox
import threading
import os
import time

# 🎵 Music loader (uses pygame)
def play_music():
    try:
        import pygame
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("PERFECT.mp3")
        pygame.mixer.music.play(-1)
    except:
        print("Music not playing ♡ (pygame missing or bg_music.mp3 not found)")

# 🌟 Clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ✍️ Cute typewriter
def slow(text, delay=0.05):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

# 💖 ASCII name with cute emoji
def show_ascii_name():
    clear()
    print(r"""
███╗   ███╗███████╗██╗  ██╗███████╗██████╗ 
████╗ ████║██╔════╝██║  ██║██╔════╝██╔══██╗
██╔████╔██║█████╗  ███████║█████╗  ██████╔╝
██║╚██╔╝██║██╔══╝  ██╔══██║██╔══╝  ██╔══██╗
██║ ╚═╝ ██║███████╗██║  ██║███████╗██║  ██║
╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

           ♡ MEHER ♡  ₍^. .^₎⟆
""")
    time.sleep(2)

# 💕 Hearty animation
def heart_animation():
    frames = [
        "    ♡     ♡\n     ♡ ♡\n      ♡",
        " ♡   ♡   ♡\n    ♡ ♡\n     ♡",
        "   ♡   ♡\n     ♡\n    ♡ ♡",
        "♡ ♡ ♡\n   ♡ ♡\n    ♡"
    ]
    for i in range(6):
        clear()
        print(frames[i % len(frames)])
        time.sleep(0.3)

# 🐾 Magical cute messages
def magical_messages():
    messages = [
        "Hey Meher ฅ^>⩊<^ฅ",
        "You’re the sparkle in this dull world ♡",
        "Your smile can heal any sadness ₍^•⩊•^₎",
        "You matter. You’re special. You are loved (*≧ω≦)",
        "Never forget that you're a Queen ♕ ₍^. .^₎⟆",
        "This is a little gift just for you ♡"
    ]
    for msg in messages:
        slow(msg, delay=0.07)
        time.sleep(1)

# ⏳ Countdown before surprise
def countdown_reveal():
    clear()
    slow("Unlocking your surprise in...", delay=0.08)
    for i in range(5, 0, -1):
        print(f"⏳ {i}")
        time.sleep(1)
    clear()

# 💌 Poem with text emojis
def secret_poem():
    poem = """
💌 To Meher, the most beautiful soul ₍^. .^₎⟆

Roses are red ♡, the sky is blue  
There’s nobody else more magical than you ฅ^>⩊<^ฅ

When you laugh, stars giggle too ♡  
And every moment with you feels new (*≧ω≦)

You are art, melody, and pure grace ₍˶ᵔ ᵕ ᵔ˶₎  
This world is brighter because of your face ₍⩊⩊₎

So this gift is my little way to say,  
You’re deeply loved... more each day ♡
"""
    slow(poem, delay=0.07)

# 🎉 Cute Fireworks
def fireworks():
    for _ in range(3):
        clear()
        print("🎇♡ YOU ARE LOVED ♡🎇")
        time.sleep(0.5)
        clear()
        print("♡ THANK YOU MEHER ₍^. .^₎⟆")
        time.sleep(0.5)

# 🎁 Final Surprise Sequence
def launch_gift():
    threading.Thread(target=play_music).start()
    show_ascii_name()
    heart_animation()
    magical_messages()
    countdown_reveal()
    secret_poem()
    fireworks()
    print("\n🌸 From your best friend... forever ₍^>⩊<^₎♡")
    input("\n(Press Enter to exit...)")

# 🐇 GUI asking love
def start_gui():
    root = tk.Tk()
    root.title("A Cute Question ♡")
    root.geometry("500x300")
    root.config(bg="#fff0f5")

    question = tk.Label(root, text="U ARE MY BESTFRIEND? ₍^. .^₎⟆", font=("Helvetica", 22, "bold"), bg="#fff0f5", fg="#cc0066")
    question.pack(pady=40)

    yes_size = [12]
    triggered = [False]

    def say_yes():
        messagebox.showinfo("Hehe ♡", "Mujhe pata tha ♡ ฅ^>⩊<^ฅ")
        root.destroy()
        launch_gift()

    def say_no():
        yes_size[0] += 3
        yes_btn.config(font=("Helvetica", yes_size[0]))
        if yes_size[0] > 25 and not triggered[0]:
            triggered[0] = True
            messagebox.showinfo("Okay Okay ₍^~^₎", "Chup chap accept kar liya ♡")
            root.after(500, say_yes)

    btn_frame = tk.Frame(root, bg="#fff0f5")
    btn_frame.pack()

    yes_btn = tk.Button(btn_frame, text="YES ♡", font=("Helvetica", yes_size[0]), bg="#ff99cc", fg="white", command=say_yes)
    yes_btn.grid(row=0, column=0, padx=20)

    no_btn = tk.Button(btn_frame, text="NO ₍>﹏<₎", font=("Helvetica", 12), bg="#cccccc", command=say_no)
    no_btn.grid(row=0, column=1, padx=20)

    root.mainloop()

# 🏁 Start it
if __name__ == "__main__":
    start_gui()
