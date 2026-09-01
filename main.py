import json
from src.extract.open_library import search_books
from src.transform.books_transform import transform_books

def main():
    books_data = search_books("Romance")
    transformed_books = transform_books(books_data)
    
    print(json.dumps(transformed_books, indent=4, ensure_ascii=False))
    
    
if __name__ == "__main__":
    main()