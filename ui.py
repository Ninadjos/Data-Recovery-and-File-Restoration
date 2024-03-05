import tkinter as tk
from tkinter import ttk
import winshell

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Bin Master")
        self.geometry("600x400")

        self.label = ttk.Label(self, text="Welcome to the Bin Master!", font=("Helvetica", 14))
        self.label.pack(pady=20)

        self.button = ttk.Button(self, text="Restore All Files", command=self.restore_files)
        self.button.pack(pady=20)

        self.recycle_bin_list = tk.Listbox(self, height=15, width=60)
        self.recycle_bin_list.pack(pady=20)

        self.result_text = tk.Text(self, height=5, width=50)
        self.result_text.pack(pady=20)

    def restore_files(self):
        self.recycle_bin_list.delete(0, tk.END)
        self.result_text.delete(1.0, tk.END)

        for item in winshell.recycle_bin():
            winshell.undelete(item.original_filename())
            self.recycle_bin_list.insert(tk.END, item.original_filename())
            self.result_text.insert(tk.END, "Restored Successfully! -> %r\n" % item.original_filename())

if __name__ == "__main__":
    app = App()
    app.mainloop()