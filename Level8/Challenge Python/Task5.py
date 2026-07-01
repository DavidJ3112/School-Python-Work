import tkinter as tk
from tkinter import colorchooser
from PIL import Image, ImageDraw


class PaintApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Paint App")

        self.width = 900
        self.height = 600

        #!# =========================
        #!# STATE
        #!# =========================
        self.color = "black"
        self.eraser = False
        self.last_x = None
        self.last_y = None

        self.current_stroke = None
        self.strokes: list[list[dict]] = []
        self.redo_stack: list[list[dict]] = []

        #!# =========================
        #!# IMAGE MODEL
        #!# =========================
        self.image = Image.new("RGB", (self.width, self.height), "white")
        self.draw = ImageDraw.Draw(self.image)

        #!# =========================
        #!# GUI LAYOUT
        #!# =========================
        self.toolbar = tk.Frame(root, bg="#!#ddd", height=40)
        self.toolbar.pack(side="top", fill="x")

        self.canvas = tk.Canvas(root, bg="white", width=self.width, height=self.height)
        self.canvas.pack(fill="both", expand=True)

        #!# =========================
        #!# CONTROLS
        #!# =========================
        tk.Button(self.toolbar, text="Color", command=self.pick_color).pack(side="left")
        tk.Button(self.toolbar, text="Eraser", command=self.use_eraser).pack(side="left")
        tk.Button(self.toolbar, text="Undo (Ctrl+Z)", command=self.undo).pack(side="left")
        tk.Button(self.toolbar, text="Redo (Ctrl+Y)", command=self.redo).pack(side="left")

        tk.Label(self.toolbar, text="Brush").pack(side="left")

        self.brush = tk.Scale(self.toolbar, from_=1, to=50, orient="horizontal")
        self.brush.set(5)
        self.brush.pack(side="left")

        #!# =========================
        #!# EVENTS
        #!# =========================
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw_motion)
        self.canvas.bind("<ButtonRelease-1>", self.end_draw)

        #!# hotkeys
        self.root.bind("<Control-z>", lambda e: self.undo())
        self.root.bind("<Control-y>", lambda e: self.redo())

    #!# =========================
    #!# TOOLS
    #!# =========================
    def pick_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.color = color
            self.eraser = False

    def use_eraser(self):
        self.eraser = True

    #!# =========================
    #!# DRAWING
    #!# =========================
    def start_draw(self, event):
        self.last_x = event.x
        self.last_y = event.y
        self.current_stroke = []
        self.redo_stack.clear()

    def draw_motion(self, event):
        if self.last_x is None or self.last_y is None:
            return

        size = int(self.brush.get())
        color = "white" if self.eraser else self.color

        #!# draw on canvas
        line_id = self.canvas.create_line(
            self.last_x,
            self.last_y,
            event.x,
            event.y,
            fill=color,
            width=size,
            capstyle=tk.ROUND,
            smooth=True
        )

        #!# draw on PIL image
        self.draw.line(
            (self.last_x, self.last_y, event.x, event.y),
            fill=color,
            width=size
        )

        #!# store stroke data (not just ids)
        if self.current_stroke is not None:
            self.current_stroke.append({
                "x1": self.last_x,
                "y1": self.last_y,
                "x2": event.x,
                "y2": event.y,
                "color": color,
                "size": size,
                "id": line_id
            })
        self.last_x = event.x
        self.last_y = event.y

    def end_draw(self, event):
        if self.current_stroke:
            self.strokes.append(self.current_stroke)

        self.current_stroke = None
        self.last_x = None
        self.last_y = None

    #!# =========================
    #!# UNDO / REDO
    #!# =========================
    def undo(self):
        if not self.strokes:
            return

        stroke = self.strokes.pop()
        self.redo_stack.append(stroke)

        for part in stroke:
            self.canvas.delete(part["id"])

        self.rebuild_image()

    def redo(self):
        if not self.redo_stack:
            return

        stroke = self.redo_stack.pop()
        self.strokes.append(stroke)

        for part in stroke:
            self.canvas.create_line(
                part["x1"],
                part["y1"],
                part["x2"],
                part["y2"],
                fill=part["color"],
                width=part["size"],
                capstyle=tk.ROUND,
                smooth=True
            )

        self.rebuild_image()

    #!# =========================
    #!# IMAGE REBUILD
    #!# =========================
    def rebuild_image(self):
        self.image = Image.new("RGB", (self.width, self.height), "white")
        self.draw = ImageDraw.Draw(self.image)

        for stroke in self.strokes:
            for part in stroke:
                self.draw.line(
                    (part["x1"], part["y1"], part["x2"], part["y2"]),
                    fill=part["color"],
                    width=part["size"]
                )


#!# =========================
#!# RUN
#!# =========================
if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()