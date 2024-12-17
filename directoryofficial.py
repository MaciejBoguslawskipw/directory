import os
import shutil

def create_directory(name):
    try:
        os.makedirs(name)
        print(f"Katalog '{name}' został utworzony.")
    except FileExistsError:
        print(f"Katalog '{name}' już istnieje.")

def list_directories():
    directories = [d for d in os.listdir() if os.path.isdir(d)]
    if directories:
        print("Lista katalogów:")
        for directory in directories:
            print(directory)
    else:
        print("Brak katalogów.")

def rename_directory(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"Katalog '{old_name}' został zmieniony na '{new_name}'.")
    except FileNotFoundError:
        print(f"Katalog '{old_name}' nie istnieje.")
    except FileExistsError:
        print(f"Katalog '{new_name}' już istnieje.")

def delete_directory(name):
    try:
        if os.listdir(name):
            confirm = input(f"Katalog '{name}' zawiera pliki. Czy na pewno chcesz go usunąć? (tak/nie): ")
            if confirm.lower() != 'tak':
                print("Usunięcie katalogu zostało anulowane.")
                return
        shutil.rmtree(name)
        print(f"Katalog '{name}' został usunięty.")
    except FileNotFoundError:
        print(f"Katalog '{name}' nie istnieje.")
    except OSError as e:
        print(f"Nie można usunąć katalogu '{name}': {e}")

def copy_directory(src, dst):
    try:
        shutil.copytree(src, dst)
        print(f"Katalog '{src}' został skopiowany do '{dst}'.")
    except FileNotFoundError:
        print(f"Katalog źródłowy '{src}' nie istnieje.")
    except FileExistsError:
        print(f"Katalog docelowy '{dst}' już istnieje.")
    except OSError as e:
        print(f"Nie można skopiować katalogu '{src}' do '{dst}': {e}")

def main():
    while True:
        print("\nZarządzanie Katalogami Roków Studiów")
        print("1. Tworzenie katalogu")
        print("2. Wyświetlenie listy katalogów")
        print("3. Edycja (zmiana nazwy katalogu)")
        print("4. Usunięcie katalogu")
        print("5. Kopiowanie katalogu")
        print("6. Wyjście z programu")
        
        choice = input("Wybierz opcję (1-6): ")
        
        if choice == '1':
            name = input("Podaj nazwę katalogu: ")
            create_directory(name)
        elif choice == '2':
            list_directories()
        elif choice == '3':
            old_name = input("Podaj obecną nazwę katalogu: ")
            new_name = input("Podaj nową nazwę katalogu: ")
            rename_directory(old_name, new_name)
        elif choice == '4':
            name = input("Podaj nazwę katalogu do usunięcia: ")
            delete_directory(name)
        elif choice == '5':
            src = input("Podaj nazwę katalogu źródłowego: ")
            dst = input("Podaj nazwę katalogu docelowego: ")
            copy_directory(src, dst)
        elif choice == '6':
            print("Wyjście z programu.")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()
