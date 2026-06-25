# from general_scripts.init import *
import tkinter as tk
import time

from general_scripts.init import *


class ClockApp:
    def __init__(self) -> None:
        self.Window = tk.Tk()
        self.Window.title("Clock App")
        self.Window.geometry("640x640")

        self.current_view = None

        self.menu_frame = tk.Frame(self.Window)
        self.menu_frame.pack(pady=10)

        tk.Button(self.menu_frame, text="Clock", command=self.show_clock).pack(
            side="left", padx=10
        )
        tk.Button(self.menu_frame, text="Stop Watch", command=self.show_stopwatch).pack(
            side="left", padx=10
        )
        tk.Button(self.menu_frame, text="Alarm", command=self.show_alarm).pack(
            side="left", padx=10
        )

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
        self.current_view = self.Alarm(self.content_frame)

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

            self.time_label.config(text=f"Date: {current_date}\nTime: {current_time}")

            self.frame.after(500, self.tick)

    class Alarm:
        def __init__(self, frame):
            self.frame = frame

            self.alarm_time = None

            title = tk.Label(self.frame, text="Alarm Clock", font=("Arial", 24))
            title.pack(pady=20)

            self.clock_label = tk.Label(self.frame, text="", font=("Arial", 28))
            self.clock_label.pack(pady=20)

            selector_frame = tk.Frame(self.frame)
            selector_frame.pack(pady=20)

            self.hour_var = tk.StringVar(value="00")
            self.minute_var = tk.StringVar(value="00")
            self.second_var = tk.StringVar(value="00")

            self.hour_spin = tk.Spinbox(
                selector_frame,
                from_=0,
                to=23,
                wrap=True,
                width=3,
                font=("Arial", 18),
                textvariable=self.hour_var,
                format="%02.0f",
            )
            self.hour_spin.pack(side="left")

            tk.Label(selector_frame, text=":", font=("Arial", 18)).pack(side="left")

            self.minute_spin = tk.Spinbox(
                selector_frame,
                from_=0,
                to=59,
                wrap=True,
                width=3,
                font=("Arial", 18),
                textvariable=self.minute_var,
                format="%02.0f",
            )
            self.minute_spin.pack(side="left")

            tk.Label(selector_frame, text=":", font=("Arial", 18)).pack(side="left")

            self.second_spin = tk.Spinbox(
                selector_frame,
                from_=0,
                to=59,
                wrap=True,
                width=3,
                font=("Arial", 18),
                textvariable=self.second_var,
                format="%02.0f",
            )
            self.second_spin.pack(side="left")

            button_frame = tk.Frame(self.frame)
            button_frame.pack(pady=20)

            tk.Button(button_frame, text="Set Alarm", command=self.set_alarm).pack(
                side="left", padx=5
            )

            tk.Button(button_frame, text="Clear Alarm", command=self.clear_alarm).pack(
                side="left", padx=5
            )

            self.status_label = tk.Label(
                self.frame, text="No alarm set", font=("Arial", 16)
            )
            self.status_label.pack(pady=20)

            self.tick()

        def set_alarm(self):
            self.alarm_time = (
                f"{self.hour_var.get()}:{self.minute_var.get()}:{self.second_var.get()}"
            )

            self.status_label.config(text=f"Alarm set for {self.alarm_time}")

        def clear_alarm(self):
            self.alarm_time = None
            self.status_label.config(text="Alarm cleared")

        def tick(self):
            if not self.frame.winfo_exists():
                return

            current_time = time.strftime("%H:%M:%S")

            self.clock_label.config(text=current_time)

            if self.alarm_time == current_time:
                self.status_label.config(text="⏰ ALARM ⏰")

                self.frame.bell()

                self.alarm_time = None

            self.frame.after(500, self.tick)


if __name__ == "__main__":
    ClockApp()
