import tkinter as tk
from tkinter import filedialog, messagebox


class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Kladblok - Nieuw bestand")
        self.file_path = None
        self.dirty = False

        #!# TEXT AREA
        self.text = tk.Text(root, wrap="word", undo=True)
        self.text.pack(fill="both", expand=True)

        #!# Scrollbar
        scrollbar = tk.Scrollbar(self.text)
        scrollbar.pack(side="right", fill="y")
        self.text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text.yview)

        #!# Track changes (dirty flag)
        self.text.bind("<<Modified>>", self.on_modified)

        #!# MENU BAR
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)

        #!# Bestand menu
        file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Bestand", menu=file_menu)

        file_menu.add_command(label="Nieuw", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Openen", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Opslaan", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Opslaan als", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Afsluiten", command=self.exit_app)

        #!# Bewerken menu
        edit_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Bewerken", menu=edit_menu)

        edit_menu.add_command(label="Knippen", command=lambda: self.text.event_generate("<<Cut>>"))
        edit_menu.add_command(label="Kopiëren", command=lambda: self.text.event_generate("<<Copy>>"))
        edit_menu.add_command(label="Plakken", command=lambda: self.text.event_generate("<<Paste>>"))

        #!# Help menu
        help_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="Over", command=self.about)

        #!# SHORTCUTS
        root.bind("<Control-n>", lambda e: self.new_file())
        root.bind("<Control-o>", lambda e: self.open_file())
        root.bind("<Control-s>", lambda e: self.save_file())

    def new_file(self):
        if self.check_dirty():
            self.text.delete(1.0, tk.END)
            self.file_path = None
            self.set_title("Nieuw bestand")

    def open_file(self):
        if not self.check_dirty():
            return

        path = filedialog.askopenfilename(
            filetypes=[("Tekstbestanden", "*.txt"), ("Alle bestanden", "*.*")]
        )

        if path:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            self.text.delete(1.0, tk.END)
            self.text.insert(tk.END, content)

            self.file_path = path
            self.set_title(path)

    def save_file(self):
        if self.file_path:
            with open(self.file_path, "w", encoding="utf-8") as f:
                f.write(self.text.get(1.0, tk.END))
            self.mark_saved()
        else:
            self.save_as()

    def save_as(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Tekstbestanden", "*.txt"), ("Alle bestanden", "*.*")]
        )

        if path:
            self.file_path = path
            self.save_file()
            self.set_title(path)

    def exit_app(self):
        if self.check_dirty():
            self.root.destroy()

    def on_modified(self, event=None):
        self.dirty = True
        self.update_title()
        self.text.edit_modified(False)

    def mark_saved(self):
        self.dirty = False
        self.update_title()

    def update_title(self):
        name = self.file_path if self.file_path else "Nieuw bestand"

        if self.dirty:
            name = "*" + name

        self.root.title(f"Kladblok - {name}")

    def set_title(self, path):
        self.file_path = path
        self.dirty = False
        self.update_title()

    def check_dirty(self):
        if self.dirty:
            return messagebox.askyesno(
                "Onopgeslagen wijzigingen",
                "Je hebt onopgeslagen wijzigingen. Doorgaan?"
            )
        return True

    def about(self):
        messagebox.showinfo("Over", "Kladblok in Tkinter - schoolopdracht")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = Notepad(root)
    root.mainloop()