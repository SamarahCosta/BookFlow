"""
Comunicação com a API Open Library

Informações como:
- Requests
- Response JSON
"""

import requests

# importando informações do settings
from src.config.settings import(
    OPEN_LIBRARY_BASE_URL,
    REQUEST_TIMEOUT,
    BOOKS_LIMIT,
)

def search_books(book):
    """
        Busca livros na API Open Library utilizando um termo de pesquisa.

        Args:
            query (str): Termo utilizado para pesquisar os livros.

        Returns:
            dict: Dados brutos retornados pela API.
    """
    
    url = f'{OPEN_LIBRARY_BASE_URL}/search.json'
    
    params = {
        "q": book,
        "limit": BOOKS_LIMIT
    }
    
    response = requests.get(
        url,
        params=params,
        timeout=REQUEST_TIMEOUT
    )
    
    response.raise_for_status() # Caso retorne um erro HTTP, o python gera um erro

    return response.json()