import json
from masterservice.service.models import User, Book
from datetime import datetime

class DBAPI: 

    def __init__(self): 

        self.booksdb_conn = "masterservice/Database/books.json"
        self.usersdb_conn = "masterservice/Database/users.json"
        self.now = datetime.now()

    def add_book(self, title, author, isbn, availability):

        book = Book.schema(
            title=title,
            author=author,
            isbn=isbn,
            availability=bool(availability)
        )

        with open(self.booksdb_conn, 'r') as file:
            books = json.load(file)
            books['data'].append(book)
            books['updated_time'] = self.now.strftime("%Y-%m-%d %H:%M:%S")

            with open(self.booksdb_conn, 'w') as file: 
                json.dump(books, file)


    def update_book(self, query, kwargs):

        with open(self.booksdb_conn, 'r') as file:
            books = json.load(file)

            for idx in range(0, len(books['data'])):
                status = True 
                for query_key, query_value in query.items():
                    if books['data'][idx][query_key] != query_value:
                        status = False

                if status == True:
                    for update_key, update_value in kwargs.items(): 
                        books['data'][idx][update_key] = update_value

                    books['updated_time'] = self.now.strftime("%Y-%m-%d %H:%M:%S")

            with open(self.booksdb_conn, 'w') as file: 
                json.dump(books, file)


    def delete_book(self, query): 

        with open(self.booksdb_conn, 'r') as file:
            books = json.load(file)

            new_books = {
                "data": [], 
                "created_time": books['created_time'],
                "updated_time": books['updated_time']
            }

            for idx in range(0, len(books['data'])):
                status = True 
                for query_key, query_value in query.items():
                    if books['data'][idx][query_key] != query_value:
                        status = False

                if status == False:
                    new_books['data'].append(books['data'][idx])
                    new_books['updated_time'] = self.now.strftime("%Y-%m-%d %H:%M:%S")

            with open(self.booksdb_conn, 'w') as file: 
                json.dump(new_books, file)


    def list_books(self): 

        with open(self.booksdb_conn, 'r') as file:
            books = json.load(file)
            return books['data']
        

    def search_book(self, query):

        fetched_books = list()

        with open(self.booksdb_conn, 'r') as file:
            books = json.load(file)
            print(books)
            for idx in range(0, len(books['data'])):
                status = True 
                for query_key, query_value in query.items():
                    if books['data'][idx][query_key] != query_value:
                        status = False

                if status == True:
                    fetched_books.append(books['data'][idx])

        return fetched_books

            


    








