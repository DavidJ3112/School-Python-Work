import tkinter as tk
import time

import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
sys.path.append(parent_dir)

from general_scripts.init import *


class ClockApp:
    def __init__(self) -> None:
        self.Window = tk.Tk()
        self.Window.title("Clock App")
        self.Window.geometry("640x640")

        self.current_view = None

        ## Menu
        self.menu_frame = tk.Frame(self.Window)
        self.menu_frame.pack(pady=10)

        ## Menu Buttons
        tk.Button(self.menu_frame, text="Clock", command=self.show_clock).pack(
            side="left", padx=10
        )
        tk.Button(self.menu_frame, text="Stop Watch", command=self.show_stopwatch).pack(
            side="left", padx=10
        )
        tk.Button(self.menu_frame, text="Alarm", command=self.show_alarm).pack(
            side="left", padx=10
        )

        ## Content area — sub-views pack into this frame
        self.content_frame = tk.Frame(self.Window)
        self.content_frame.pack(fill="both", expand=True)

        self.Window.mainloop()

    def clear_view(self):
        """Destroy all widgets in the content frame before switching views."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        self.current_view = None

    def show_clock(self):
        self.clear_view()
        self.current_view = self.Clock(self.content_frame)

    def show_stopwatch(self):
        self.clear_view()
        self.current_view = self.StopWatch(self.content_frame)

    def show_alarm(self):
        self.clear_view()
        # Alarm not yet implemented

    class StopWatch:
        def __init__(self, frame):
            self.frame = frame

            self.start_time = 0
            self.elapsed = 0.0
            self.running = False

            self.time_label = tk.Label(self.frame, font=("Arial", 36), text="0.00")
            self.time_label.pack(pady=80)

            button_frame = tk.Frame(self.frame)
            button_frame.pack()

            tk.Button(button_frame, text="Start", command=self.start).pack(
                side="left", padx=5
            )
            tk.Button(button_frame, text="Pause", command=self.pause).pack(
                side="left", padx=5
            )
            tk.Button(button_frame, text="Reset", command=self.reset).pack(
                side="left", padx=5
            )

            self.tick()

        def start(self):
            if not self.running:
                self.start_time = time.time() - self.elapsed
                self.running = True

        def pause(self):
            if self.running:
                self.elapsed = time.time() - self.start_time
                self.running = False

        def reset(self):
            self.running = False
            self.elapsed = 0.0
            self.time_label.config(text="0.00")

        def tick(self):
            if not self.frame.winfo_exists():
                return
            if self.running:
                self.elapsed = time.time() - self.start_time
                self.time_label.config(text=f"{self.elapsed:.2f}")
            self.frame.after(50, self.tick)

    class Clock:
        def __init__(self, frame):
            self.frame = frame

            self.time_label = tk.Label(self.frame, font=("Arial", 24), text="")
            self.time_label.pack(pady=80)

            self.tick()

        def tick(self):
            if not self.frame.winfo_exists() or not self.time_label.winfo_exists():
                return

            current_date = time.strftime("%Y-%m-%d", time.localtime())
            current_time = time.strftime("%H:%M:%S", time.localtime())

            self.time_label.config(
                text=f"Date: {current_date}\nTime: {current_time}"
            )

            self.frame.after(500, self.tick)

    class Alarm:
        def __init__(self, frame):
            self.frame = frame
            tk.Label(self.frame, text="Alarm — coming soon", font=("Arial", 18)).pack(
                pady=80
            )


if __name__ == "__main__":
    ClockApp()
