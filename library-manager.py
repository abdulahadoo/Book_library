#library_managment_system

import json
import os

data_file = "library.txt"

def load_library():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    else:
        return[]

def save_library(library):
    with open(data_file, 'w')as file:
        json.dump(library,file)

def add_book(library):
    title  = input('Enter the title of the book: ')
    author = input('Enter the author of the book: ')
    Year   = input('Enter the year of the book: ')
    genre  = input('Enter the genre fo the book: ')
    read   = input('Have you read the book: (Yes/No) ').lower == 'yes'

    new_book = {
        'title' :title,
        'author' :author,
        'year'   :Year,
        'genre'  :genre,
        'read'   :read
    }

    library.append(new_book)
    save_library(library)
    print(f'Book{title}Added succesfuly.')

def remove_book(library):
    title = input("Enter the title book from the library") 
    initial_lenth = len(library)
    library =[book for book in library if book ['title'].lower !=title]
    if len(library) < initial_lenth:
        save_library(library)
        print(f'Book{title} remove succesfuly.')
    else:
        print(f'Book {title} is note found in the library.')

def search_book(library):
    search_by = input("Search by title or author").lower() 
    search_term = input(f"Enter the {search_by} ").lower()

    result = [book for book in library if search_term in book [search_by].lower()]          

    if result:
        for book in result:
            status = "Read" if book ['read'] else "unread"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")

        else:
             print(f"No book found matching '{search_term}' in the {search_by} field.")    

def display_all_books(library):
    if library:
        for book in library:
            status = "Read" if book ['read'] else "unread"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")

    else:
        print("The library is empty.")        

def display_statistics(library):
    total_book = len(library)
    read_books = len([book for book in library if book ['read']]) 
    percentage_read = len(read_books / total_book) * 100 if total_book > 0 else 0

    print(f"Total books:{total_book}")
    print(f"percentage read:{percentage_read:.2f}%")
    
def main():
    library = load_library()
    while True:
        print("Menu")    
        print("1. Add a book")    
        print("2. Remove a book")    
        print("3. Search by library")    
        print("4. Display all book")
        print("4. Display statistics")
        print("6. Exit")


        choice = input("Enter your choice: ")
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("Thank you!")    
            break
        else :
            print("Invalid choice! please try again.")

if __name__ == '__main__':
    main()                          


