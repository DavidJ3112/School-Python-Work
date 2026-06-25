import tkinter as tk

from general_scripts.init import *


class Calculator:
    def __init__(self):
        self.screen = tk.Tk()
        self.screen.title("Calculator")
        self.screen.geometry("640x640")

        self.CalFrame = tk.Frame(self.screen)
        self.CalFrame.pack(pady=20)

        # Calculator state
        self.current_value = ""
        self.first_number = None
        self.operator = None

        # Display
        self.display_var = tk.StringVar(value="0")

        tk.Entry(
            self.CalFrame,
            textvariable=self.display_var,
            justify="right",
            font=("Arial", 24),
            width=15
        ).grid(row=0, column=0, columnspan=4, pady=(0, 10))

        # Normal buttons
        buttons = [
            ("C", 1, 0),
            ("/", 1, 1),
            ("*", 1, 2),
            ("-", 1, 3),

            ("7", 2, 0),
            ("8", 2, 1),
            ("9", 2, 2),

            ("4", 3, 0),
            ("5", 3, 1),
            ("6", 3, 2),

            ("1", 4, 0),
            ("2", 4, 1),
            ("3", 4, 2),

            (".", 5, 2),
        ]

        for text, row, col in buttons:
            tk.Button(
                self.CalFrame,
                text=text,
                width=6,
                height=3,
                command=lambda n=text: self.Click(n)
            ).grid(
                row=row,
                column=col,
                padx=5,
                pady=5
            )

        # Large +
        tk.Button(
            self.CalFrame,
            text="+",
            width=6,
            height=7,
            command=lambda: self.Click("+")
        ).grid(
            row=2,
            column=3,
            rowspan=2,
            padx=5,
            pady=5,
            sticky="ns"
        )

        # Large =
        tk.Button(
            self.CalFrame,
            text="=",
            width=6,
            height=7,
            command=lambda: self.Click("=")
        ).grid(
            row=4,
            column=3,
            rowspan=2,
            padx=5,
            pady=5,
            sticky="ns"
        )

        # Large 0
        tk.Button(
            self.CalFrame,
            text="0",
            width=14,
            height=3,
            command=lambda: self.Click("0")
        ).grid(
            row=5,
            column=0,
            columnspan=2,
            padx=5,
            pady=5,
            sticky="ew"
        )

        self.screen.mainloop()

    def Click(self, name):
        print(f"Clicked: {name}")

        # Clear
        if name == "C":
            self.current_value = ""
            self.first_number = None
            self.operator = None
            self.display_var.set("0")
            return

        # Number
        if name.isdigit():
            self.current_value += name
            self.display_var.set(self.current_value)
            return

        # Decimal point
        if name == ".":
            if "." not in self.current_value:
                if self.current_value == "":
                    self.current_value = "0."
                else:
                    self.current_value += "."
                self.display_var.set(self.current_value)
            return

        # Operator
        if name in ("+", "-", "*", "/"):
            if self.current_value == "":
                return

            try:
                self.first_number = float(self.current_value)
                self.operator = name
                self.current_value = ""
            except ValueError:
                self.display_var.set("Error")

            return

        # Equals
        if name == "=":
            try:
                if (
                    self.first_number is None
                    or self.operator is None
                    or self.current_value == ""
                ):
                    return

                second_number = float(self.current_value)

                if self.operator == "+":
                    result = self.first_number + second_number

                elif self.operator == "-":
                    result = self.first_number - second_number

                elif self.operator == "*":
                    result = self.first_number * second_number

                elif self.operator == "/":
                    result = self.first_number / second_number

                if result == int(result):
                    result = int(result)

                self.display_var.set(str(result))

                # Allow continued calculations
                self.current_value = str(result)
                self.first_number = None
                self.operator = None

            except ZeroDivisionError:
                self.display_var.set("Cannot divide by 0")

                self.current_value = ""
                self.first_number = None
                self.operator = None

            except Exception as e:
                print(e)

                self.display_var.set("Error")

                self.current_value = ""
                self.first_number = None
                self.operator = None


if __name__ == "__main__":
    Calculator()