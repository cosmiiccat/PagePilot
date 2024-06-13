from django.db import models
from typecheckers import Type
import uuid

class Book:

    @staticmethod
    def schema(title, author, isbn, availability):
    
        try: 
            title = Type.CharField(title, f"{'Book'}.{'title'}", max_length=255)
            author = Type.CharField(author, f"{'Book'}.{'author'}",max_length=255)
            isbn = Type.CharField(isbn, f"{'Book'}.{'isbn'}",max_length=13)
            availability = Type.BooleanField(availability, f"{'Book'}.{'availability'}")

            return {
                '_id': str(uuid.uuid4()),
                'title': title, 
                'author': author,
                'isbn': isbn, 
                'availability': availability
            }
        
        except Exception as e: 
            return e
        
class User:

    @staticmethod
    def schema(name, user_id, phone, email):
    
        try: 
            name = Type.CharField(name, f"{'User'}.{'name'}", max_length=255)
            user_id = Type.CharField(user_id, f"{'User'}.{'user_id'}",max_length=10)
            phone = Type.CharField(phone, f"{'User'}.{'phone'}",max_length=13)
            email = Type.CharField(email, f"{'User'}.{'email'}",max_length=25)

            return {
                '_id': str(uuid.uuid4()),
                'name': name, 
                'user_id': user_id,
                'phone': phone, 
                'email': email,
                'past_issue': [],
                'current_issue': [] 
            }
        
        except Exception as e: 
            return e



