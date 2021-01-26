class Book:
    def __init__(self, store_name, books: list):
        self.store_name = store_name
        self.books = books

    def get_book_info(self):
        print(f"*** {self.store_name} ***")
        for book in self.books:
            print(f"{book.get('name')} Price : {book.get('price')}")
