import json
from masterservice.service.models import User, Book
from datetime import datetime
from dotenv import load_dotenv
import copy 
import os
from utils import custom_exceptions

load_dotenv()

class DBAPI: 

    def __init__(self): 

        self.booksdb_conn = os.getenv("BOOKSDB_PATH")
        self.usersdb_conn = os.getenv("USERSDB_PATH")
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
    


    def add_user(self, name, user_id, phone, email):

        book = User.schema(
            name=name,
            user_id=user_id,
            phone=phone,
            email=email
        )

        with open(self.usersdb_conn, 'r') as file:
            users = json.load(file)
            users['data'].append(book)
            users['updated_time'] = self.now.strftime("%Y-%m-%d %H:%M:%S")

            with open(self.usersdb_conn, 'w') as file: 
                json.dump(users, file)


    def update_user(self, query, kwargs):

        with open(self.usersdb_conn, 'r') as file:
            users = json.load(file)

            for idx in range(0, len(users['data'])):
                status = True 
                for query_key, query_value in query.items():
                    if users['data'][idx][query_key] != query_value:
                        status = False

                if status == True:
                    for update_key, update_value in kwargs.items(): 
                        users['data'][idx][update_key] = update_value

                    users['updated_time'] = self.now.strftime("%Y-%m-%d %H:%M:%S")

            with open(self.usersdb_conn, 'w') as file: 
                json.dump(users, file)


    def delete_user(self, query): 

        with open(self.usersdb_conn, 'r') as file:
            users = json.load(file)

            new_users = {
                "data": [], 
                "created_time": users['created_time'],
                "updated_time": users['updated_time']
            }

            for idx in range(0, len(users['data'])):
                status = True 
                for query_key, query_value in query.items():
                    if users['data'][idx][query_key] != query_value:
                        status = False

                if status == False:
                    new_users['data'].append(users['data'][idx])
                    new_users['updated_time'] = self.now.strftime("%Y-%m-%d %H:%M:%S")

            with open(self.usersdb_conn, 'w') as file: 
                json.dump(new_users, file)


    def list_users(self): 

        with open(self.usersdb_conn, 'r') as file:
            users = json.load(file)
            return users['data']
        

    def search_user(self, query):

        fetched_users = list()

        with open(self.usersdb_conn, 'r') as file:
            users = json.load(file)
            for idx in range(0, len(users['data'])):
                status = True 
                for query_key, query_value in query.items():
                    if users['data'][idx][query_key] != query_value:
                        status = False

                if status == True:
                    fetched_users.append(users['data'][idx])

        return fetched_users
    

    def issue_book(self, isbn, user_id):

        fetched_book = {}
        fetched_user = {}
        book_query = {
            "isbn": isbn
        }

        user_query = {
            "user_id": user_id
        }

        with open(self.booksdb_conn, 'r') as file:
            books = json.load(file)
            print(books)
            for idx in range(0, len(books['data'])):
                status = True 
                for query_key, query_value in book_query.items():
                    if books['data'][idx][query_key] != query_value:
                        status = False

                if status == True:
                    if books['data'][idx]["availability"] == True:
                        fetched_book = copy.deepcopy(books['data'][idx])
                        books['data'][idx]["availability"] = False

                        with open(self.booksdb_conn, 'w') as file: 
                            json.dump(books, file)
                    else:
                        raise custom_exceptions.CustomError(f"Book with {isbn} is already issued")
                    break


        if fetched_book != {}: 

            with open(self.usersdb_conn, 'r') as file:
                users = json.load(file)
                for idx in range(0, len(users['data'])):
                    status = True 
                    for query_key, query_value in user_query.items():
                        if users['data'][idx][query_key] != query_value:
                            status = False

                    if status == True:
                        fetched_user = copy.deepcopy(users['data'][idx])
                        users['data'][idx]["current_issue"].append(
                            fetched_book["isbn"]
                        )
                        with open(self.usersdb_conn, 'w') as file: 
                            json.dump(users, file)
                        break

            if fetched_user == {}:
                raise custom_exceptions.CustomError(f"User with {user_id} does not exist")


        else: 
            raise custom_exceptions.CustomError(f"Book with {isbn} does not exist")
        
    def return_book(self, isbn, user_id):

        fetched_book = {}
        fetched_user = {}
        book_query = {
            "isbn": isbn
        }

        user_query = {
            "user_id": user_id
        }

        with open(self.booksdb_conn, 'r') as file:
            books = json.load(file)
            print(books)
            for idx in range(0, len(books['data'])):
                status = True 
                for query_key, query_value in book_query.items():
                    if books['data'][idx][query_key] != query_value:
                        status = False

                if status == True:
                    if books['data'][idx]["availability"] == False:
                        fetched_book = copy.deepcopy(books['data'][idx])
                        books['data'][idx]["availability"] = True
                        with open(self.booksdb_conn, 'w') as file: 
                            json.dump(books, file)
                    else:
                        raise custom_exceptions.CustomError(f"Book with {isbn} is not issued")
                    break


        if fetched_book != {}: 

            with open(self.usersdb_conn, 'r') as file:
                users = json.load(file)
                for idx in range(0, len(users['data'])):
                    status = True 
                    for query_key, query_value in user_query.items():
                        if users['data'][idx][query_key] != query_value:
                            status = False

                    if status == True:
                        fetched_user = copy.deepcopy(users['data'][idx])
                        current_issue = list()
                        for issue in users['data'][idx]["current_issue"]:
                            if issue != isbn:
                                current_issue.append(issue)
                        users['data'][idx]["current_issue"] = copy.deepcopy(current_issue)
                        users['data'][idx]["past_issue"].append(
                            isbn
                        )
                        with open(self.usersdb_conn, 'w') as file: 
                            json.dump(users, file)
                        break

            if fetched_user == {}:
                raise custom_exceptions.CustomError(f"User with {user_id} does not exist")

        else: 
            raise custom_exceptions.CustomError(f"Book with {isbn} does not exist")


        



            


    








