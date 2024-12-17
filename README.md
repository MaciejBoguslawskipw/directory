# directory3.py

## Przegląd
Ten skrypt jest zaprojektowany do zarządzania i manipulowania katalogami oraz plikami w określonym katalogu. Zapewnia funkcje do listowania, tworzenia, usuwania i wykonywania innych operacji na katalogach i plikach.

## Użycie

1. **Listowanie plików i katalogów**
    - Skrypt może wylistować wszystkie pliki i katalogi w określonym katalogu.
    - Przykład:
      ```python
      list_files(directory_path)
      ```

2. **Tworzenie katalogu**
    - Skrypt pozwala na utworzenie nowego katalogu w określonej ścieżce.
    - Przykład:
      ```python
      create_directory(directory_path, new_directory_name)
      ```

3. **Usuwanie katalogu**
    - Skrypt może usunąć określony katalog.
    - Przykład:
      ```python
      delete_directory(directory_path)
      ```

4. **Inne operacje**
    - Skrypt może zawierać dodatkowe funkcje, takie jak zmiana nazwy plików, przenoszenie plików itp.
    - Przykład:
      ```python
      rename_file(old_file_path, new_file_path)
      move_file(source_path, destination_path)
      ```

## Funkcje

- `list_files(directory_path)`: Wylistowuje wszystkie pliki i katalogi w określonym katalogu.
- `create_directory(directory_path, new_directory_name)`: Tworzy nowy katalog o podanej nazwie w określonej ścieżce.
- `delete_directory(directory_path)`: Usuwa określony katalog.
- `rename_file(old_file_path, new_file_path)`: Zmienia nazwę pliku ze starej ścieżki na nową ścieżkę.
- `move_file(source_path, destination_path)`: Przenosi plik z ścieżki źródłowej do ścieżki docelowej.



