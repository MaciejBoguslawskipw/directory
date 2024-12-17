import os

def display_directories():
    # Wyświetla listę katalogów w bieżącym katalogu roboczym
    directories = [d for d in os.listdir() if os.path.isdir(d)]
    print("\nKatalogi w bieżącym katalogu roboczym:")
    if directories:
        for directory in directories:
            print(f"- {directory}")
    else:
        print("Brak katalogów w bieżącym katalogu roboczym.")

def create_directory():
    # Tworzy nowy katalog na podstawie wprowadzonej nazwy
    name = input("Podaj nazwę katalogu: ")
    try:
        os.mkdir(name)
        print(f"Katalog '{name}' został utworzony.")
    except FileExistsError:
        print(f"Katalog '{name}' już istnieje.")

def rename_directory():
    # Zmienia nazwę istniejącego katalogu
    old_name = input("Podaj nazwę katalogu do zmiany: ")
    if os.path.isdir(old_name):
        new_name = input(f"Podaj nową nazwę katalogu '{old_name}': ")
        os.rename(old_name, new_name)
        print(f"Katalog '{old_name}' został zmieniony na '{new_name}'.")
    else:
        print(f"Katalog '{old_name}' nie istnieje.")

def delete_directory():
    # Usuwa katalog
    name = input("Podaj nazwę katalogu do usunięcia: ")
    if os.path.isdir(name):
        os.rmdir(name)
        print(f"Katalog '{name}' został usunięty.")
    else:
        print(f"Katalog '{name}' nie istnieje.")

def main():
    while True:
        print("\nWybierz opcję:")
        print("1. Tworzenie katalogu")
        print("2. Wyświetlenie listy katalogów")
        print("3. Edycja (zmiana nazwy katalogu)")
        print("4. Usunięcie katalogu")
        print("5. Wyjście z programu")
        
        choice = input("Wybór: ")
        
        if choice == '1':
            create_directory()
        elif choice == '2':
            display_directories()
        elif choice == '3':
            rename_directory()
        elif choice == '4':
            delete_directory()
        elif choice == '5':
            print("Zakończenie programu.")
            break
        else:
            print("Niepoprawny wybór, spróbuj ponownie.")

if __name__ == "__main__":
    main()
