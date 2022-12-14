from typing import Optional

from fastapi import FastAPI

app = FastAPI()


BOOKS = {
    'book_1': {
        'title': 'Title one',
        'author': 'Author one'
    },
    'book_2': {
        'title': 'Title two',
        'author': 'Author two'
    },
    'book_3': {
        'title': 'Title three',
        'author': 'Author three'
    },
    'book_4': {
        'title': 'Title four',
        'author': 'Author four'
    },
    'book_5': {
        'title': 'Title five',
        'author': 'Author five'
    },
}


@app.get("/")
async def read_all_books(skip_book: Optional[str] = None):
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS


@app.get("/read_book/")
async def read_book_query(book_name: str):
    return BOOKS[book_name]


@app.get("/{book_name}")
async def get_book(book_name: str):
    return BOOKS[book_name]


@app.post("/")
async def create_book(book_title: str, book_author: str):
    current_book_id = 0

    if len(BOOKS) > 0:
        for book in BOOKS:
            x = int(book.split('_')[-1])
            if x > current_book_id:
                current_book_id = x

    BOOKS[f'book_{current_book_id + 1}'] = {'title': book_title, 'author': book_author}
    return BOOKS[f'book_{current_book_id + 1}']


@app.put("/{book_name}")
async def update_book(book_name: str, book_title: str, book_author: str):
    book_information = {'title': book_title, 'author': book_author}
    BOOKS[book_name] = book_information
    return book_information


@app.delete("/delete_book/")
async def delete_book_query(book_name: str):
    del BOOKS[book_name]
    return f'Book {book_name} deleted'


@app.delete("/{book_name}")
async def delete_book(book_name: str):
    del BOOKS[book_name]
    return f'Book {book_name} deleted'
