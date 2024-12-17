import os
import tkinter as tk
from tkinter import messagebox, simpledialog

def create_directory(name):
    try:
        os.makedirs(name)
        messagebox.showinfo("Sukces", f"Katalog '{name}' został utworzony.")
    except FileExistsError:
        messagebox.showwarning("Błąd", f"Katalog '{name}' już istnieje.")

def list_directories():
    directories = [d for d in os.listdir() if os.path.isdir(d)]
    if directories:
        messagebox.showinfo("Lista katalogów", "\n".join(directories))
    else:
        messagebox.showinfo("Lista katalogów", "Brak katalogów.")

def rename_directory(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        messagebox.showinfo("Sukces", f"Katalog '{old_name}' został zmieniony na '{new_name}'.")
    except FileNotFoundError:
        messagebox.showwarning("Błąd", f"Katalog '{old_name}' nie istnieje.")
    except FileExistsError:
        messagebox.showwarning("Błąd", f"Katalog '{new_name}' już istnieje.")

def delete_directory(name):
    try:
        os.rmdir(name)
        messagebox.showinfo("Sukces", f"Katalog '{name}' został usunięty.")
    except FileNotFoundError:
        messagebox.showwarning("Błąd", f"Katalog '{name}' nie istnieje.")
    except OSError:
        messagebox.showwarning("Błąd", f"Katalog '{name}' nie jest pusty lub nie można go usunąć.")

def main():
    root = tk.Tk()
    root.title("Zarządzanie Katalogami Roków Studiów")

    def on_create():
        name = simpledialog.askstring("Tworzenie katalogu", "Podaj nazwę katalogu:")
        if name:
            create_directory(name)

    def on_list():
        list_directories()

    def on_rename():
        old_name = simpledialog.askstring("Zmiana nazwy katalogu", "Podaj obecną nazwę katalogu:")
        if old_name:
            new_name = simpledialog.askstring("Zmiana nazwy katalogu", "Podaj nową nazwę katalogu:")
            if new_name:
                rename_directory(old_name, new_name)

    def on_delete():
        name = simpledialog.askstring("Usunięcie katalogu", "Podaj nazwę katalogu do usunięcia:")
        if name:
            delete_directory(name)

    def on_exit():
        root.quit()

    tk.Button(root, text="Tworzenie katalogu", command=on_create).pack(fill=tk.X)
    tk.Button(root, text="Wyświetlenie listy katalogów", command=on_list).pack(fill=tk.X)
    tk.Button(root, text="Edycja (zmiana nazwy katalogu)", command=on_rename).pack(fill=tk.X)
    tk.Button(root, text="Usunięcie katalogu", command=on_delete).pack(fill=tk.X)
    tk.Button(root, text="Wyjście z programu", command=on_exit).pack(fill=tk.X)

    root.mainloop()

if __name__ == "__main__":
    main()