"""
Transformar os dados brutos retornados pela API.

Responsável por:

- Selecionar
- Organizar
- Padronizar
"""

def transform_books(books_data):
    """
        Transforma os dados brutos retornados pela API Open Library.

        Args:
            books_data (dict): Dados brutos retornados pela API.

        Returns:
            list: Lista contendo os livros com os dados transformados.
    """
    
    transformed_books = []
    books = books_data.get("docs", [])
    
    for book in books:
        transformed_book = {
            "author": ",".join(book.get("author_name", [])),
            "title": book.get("title"),
            "first_publish_year": book.get("first_publish_year"),
            "edition_count": book.get("edition_count"),
            "language": ",".join(book.get("language", []))
            
        }
        
        transformed_books.append(transformed_book)
    
    return transformed_books
        
    