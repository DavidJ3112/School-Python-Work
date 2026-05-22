import tkinter as tk
# from PIL import *
import time

import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
sys.path.append(parent_dir)

from general_scripts.init import *



class StopWatch:
    def __init__(self):
        self.Window = tk.Tk()
        self.Window.title("Stop Watch")
        self.Window.geometry("640x640")

        ## Var Config
        self.prv_time = -1
        self.start_time = 0
        self.elapsed = 0
        self.running = False

        ## Lables
        self.time_label = tk.Label(self.Window, font=("Arial", 16), text= "0.0")
        self.time_label.pack(pady=200)

        ## Buttons
        button_frame = tk.Frame(self.Window)
        button_frame.pack()

        self.start_btn = tk.Button(button_frame, text="Start", command=self.StartTimer)
        self.start_btn.pack(side="left", padx=5)

        self.pause_btn = tk.Button(button_frame, text="Pause", command=self.PauseTimer)
        self.pause_btn.pack(side="left", padx=5)

        self.reset_btn = tk.Button(button_frame, text="Reset", command=self.ResetTimer)
        self.reset_btn.pack(side="left", padx=5)

        self.tick()
        self.Window.mainloop()

    def StartTimer(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed
            self.running = True

    def PauseTimer(self):
        if self.running:
            self.elapsed = time.time() - self.start_time
            self.running = False

    def ResetTimer(self):
        self.running = False
        self.elapsed = 0
        self.time_label.config(text="0.00")

    def tick(self):
        if self.running:
            self.elapsed = time.time() - self.start_time
            self.time_label.config(text=f"{self.elapsed:.2f}")

        self.Window.after(50, self.tick)



if __name__ == "__main__":
    SW = StopWatch()