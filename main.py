import json
from src.extract.open_library import search_books
from src.transform.books_transform import transform_books
from src.validate.data_quality import validate_books

def main():
    books_data = search_books("Romance")
    transformed_books = transform_books(books_data)
    valid_books, invalid_books = validate_books(transformed_books)
    
    
    print("Livros validos:\n" + json.dumps(valid_books, indent=4, ensure_ascii=False))
    print("-"*15)
    print("Livros inválidos:\n" + json.dumps(invalid_books, indent=4, ensure_ascii=False))
    
if __name__ == "__main__":
    main()