"""
Valida os dados transformados campos nulos etc
"""

def validate_books(transformed_books):
    """
        Valida os dados dos livros transformados.
    """
    
    valid_books = []
    invalid_books = []
    
    for book in transformed_books:
        
        # bool valida se um objeto possui valor valido ou se esta vazio/nulo e retorna true ou false.
        has_author = bool(book.get("author")) 
        has_title = bool(book.get("title"))
        
        publish_year = book.get("first_publish_year")
        
        is_valid_publish_year = (
            publish_year is None
            or isinstance(publish_year, int)
        )
        
        edition_count = book.get("edition_count")
        is_valid_edition_count = (
            edition_count is None
            or (
                isinstance(edition_count, int)
                and edition_count > 0
            )
        )
        
        is_valid = (
            has_title
            and has_author
            and is_valid_publish_year
            and is_valid_edition_count
        )
        
        if is_valid:
            valid_books.append(book)
        else:
            invalid_books.append(book)
            
    return valid_books, invalid_books

        
