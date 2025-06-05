import tkinter as tk
from tkinter import filedialog, messagebox

try:
    import openpyxl
except ImportError:
    openpyxl = None


class ExcelApp:
    def __init__(self, master: tk.Tk):
        self.master = master
        master.title("Excel GUI App")

        self.label = tk.Label(master, text="Bitte Excel-Datei öffnen")
        self.label.pack(pady=10)

        self.open_button = tk.Button(master, text="Datei öffnen", command=self.load_file)
        self.open_button.pack(pady=5)

        self.save_button = tk.Button(master, text="Speichern unter...", command=self.save_file, state=tk.DISABLED)
        self.save_button.pack(pady=5)

        self.wb = None
        self.filename = None

    def load_file(self):
        if not openpyxl:
            messagebox.showerror("Fehlende Abhängigkeit", "openpyxl ist nicht installiert")
            return
        filename = filedialog.askopenfilename(filetypes=[("Excel Dateien", "*.xlsx *.xls")])
        if not filename:
            return
        try:
            self.wb = openpyxl.load_workbook(filename)
            self.filename = filename
            self.label.config(text=f"Geladen: {filename}")
            self.process_workbook()
            self.save_button.config(state=tk.NORMAL)
        except Exception as exc:
            messagebox.showerror("Fehler", f"Konnte Datei nicht laden: {exc}")

    def process_workbook(self):
        if not self.wb:
            return
        sheet = self.wb.active
        sheet['A1'] = 'Verarbeitet'

    def save_file(self):
        if not self.wb:
            return
        new_filename = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Dateien", "*.xlsx")])
        if not new_filename:
            return
        try:
            self.wb.save(new_filename)
            messagebox.showinfo("Erfolg", f"Datei gespeichert unter {new_filename}")
        except Exception as exc:
            messagebox.showerror("Fehler", f"Konnte Datei nicht speichern: {exc}")


def main():
    root = tk.Tk()
    app = ExcelApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
