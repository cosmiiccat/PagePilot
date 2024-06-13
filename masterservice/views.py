from django.shortcuts import render
from django.http import JsonResponse
from utils import custom_exceptions
from django.views.decorators.csrf import csrf_exempt

import json

from masterservice.service.storage import DBAPI
conn = DBAPI()


def ensure(request): 
    try:
        if request.method != "GET":
            raise custom_exceptions.CustomError(f"Method - {request.method} is not Allowed")
        
        response = {
            "success": "true", 
            "status": "online" 
        }
        return JsonResponse(response)
    
    except Exception as e:
        return JsonResponse({"success":"false", "error":f"{e}"})


@csrf_exempt 
def add_book(request):
    try:
        if request.method != "POST":
            raise custom_exceptions.CustomError(f"Method - {request.method} is not Allowed")
        
        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["title", "author", "isbn", "availability"]:
            if key not in req_data.keys():
                raise custom_exceptions.CustomError(f"The parameter {key} in JSON Body is missing")

        conn.add_book(
            title=req_data["title"],
            author=req_data["author"],
            isbn=req_data["isbn"],
            availability=req_data["availability"]
        )
        
        return JsonResponse({"success": "true", "resp": "Book is added to DB"})
    
    except Exception as e:
        return JsonResponse({"success":"false", "error":f"{e}"})
    

@csrf_exempt 
def update_book(request):
    try:
        if request.method != "POST":
            raise custom_exceptions.CustomError(f"Method - {request.method} is not Allowed")
        
        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["query", "kwargs"]:
            if key not in req_data.keys():
                raise custom_exceptions.CustomError(f"The parameter {key} in JSON Body is missing")

        conn.update_book(
            query=req_data["query"],
            kwargs=req_data["kwargs"]
        )
        
        return JsonResponse({"success": "true", "resp": "Book is updated to DB"})
    
    except Exception as e:
        return JsonResponse({"success":"false", "error":f"{e}"})
    
@csrf_exempt 
def delete_book(request):
    try:
        if request.method != "POST":
            raise custom_exceptions.CustomError(f"Method - {request.method} is not Allowed")
        
        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["query"]:
            if key not in req_data.keys():
                raise custom_exceptions.CustomError(f"The parameter {key} in JSON Body is missing")

        conn.delete_book(
            query=req_data["query"]
        )
        
        return JsonResponse({"success": "true", "resp": "Book is deleted to DB"})
    
    except Exception as e:
        return JsonResponse({"success":"false", "error":f"{e}"})
    
@csrf_exempt 
def search_book(request):
    try:
        if request.method != "POST":
            raise custom_exceptions.CustomError(f"Method - {request.method} is not Allowed")
        
        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["query"]:
            if key not in req_data.keys():
                raise custom_exceptions.CustomError(f"The parameter {key} in JSON Body is missing")

        resp = conn.search_book(
            query=req_data["query"]
        )
        
        return JsonResponse({"success": "true", "resp": resp})
    
    except Exception as e:
        return JsonResponse({"success":"false", "error":f"{e}"})
    

@csrf_exempt 
def list_books(request):
    try:
        if request.method != "GET":
            raise custom_exceptions.CustomError(f"Method - {request.method} is not Allowed")

        resp = conn.list_books()
        
        return JsonResponse({"success": "true", "resp": resp})
    
    except Exception as e:
        return JsonResponse({"success":"false", "error":f"{e}"})
    



@csrf_exempt 
def add_user(request):
    try:
        if request.method != "POST":
            raise custom_exceptions.CustomError(f"Method - {request.method} is not Allowed")
        
        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["name", "user_id", "phone", "email"]:
            if key not in req_data.keys():
                raise custom_exceptions.CustomError(f"The parameter {key} in JSON Body is missing")

        conn.add_user(
            name=req_data["name"],
            user_id=req_data["user_id"],
            phone=req_data["phone"],
            email=req_data["email"]
        )
        
        return JsonResponse({"success": "true", "resp": "User is added to DB"})
    
    except Exception as e:
        return JsonResponse({"success":"false", "error":f"{e}"})
    
@csrf_exempt 
def update_user(request):
    try:
        if request.method != "POST":
            raise custom_exceptions.CustomError(f"Method - {request.method} is not Allowed")
        
        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["query", "kwargs"]:
            if key not in req_data.keys():
                raise custom_exceptions.CustomError(f"The parameter {key} in JSON Body is missing")

        conn.update_user(
            query=req_data["query"],
            kwargs=req_data["kwargs"]
        )
        
        return JsonResponse({"success": "true", "resp": "User is updated to DB"})
    
    except Exception as e:
        return JsonResponse({"success":"false", "error":f"{e}"})
    
    
@csrf_exempt 
def delete_user(request):
    try:
        if request.method != "POST":
            raise custom_exceptions.CustomError(f"Method - {request.method} is not Allowed")
        
        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["query"]:
            if key not in req_data.keys():
                raise custom_exceptions.CustomError(f"The parameter {key} in JSON Body is missing")

        conn.delete_user(
            query=req_data["query"]
        )
        
        return JsonResponse({"success": "true", "resp": "User is deleted to DB"})
    
    except Exception as e:
        return JsonResponse({"success":"false", "error":f"{e}"})
    
@csrf_exempt 
def search_user(request):
    try:
        if request.method != "POST":
            raise custom_exceptions.CustomError(f"Method - {request.method} is not Allowed")
        
        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["query"]:
            if key not in req_data.keys():
                raise custom_exceptions.CustomError(f"The parameter {key} in JSON Body is missing")

        resp = conn.search_user(
            query=req_data["query"]
        )
        
        return JsonResponse({"success": "true", "resp": resp})
    
    except Exception as e:
        return JsonResponse({"success":"false", "error":f"{e}"})
    

@csrf_exempt 
def list_users(request):
    try:
        if request.method != "GET":
            raise custom_exceptions.CustomError(f"Method - {request.method} is not Allowed")

        resp = conn.list_users()
        
        return JsonResponse({"success": "true", "resp": resp})
    
    except Exception as e:
        return JsonResponse({"success":"false", "error":f"{e}"})
    



@csrf_exempt 
def issue_book(request):
    try:
        if request.method != "POST":
            raise custom_exceptions.CustomError(f"Method - {request.method} is not Allowed")
        
        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["isbn", "user_id"]:
            if key not in req_data.keys():
                raise custom_exceptions.CustomError(f"The parameter {key} in JSON Body is missing")

        conn.issue_book(
            isbn=req_data["isbn"],
            user_id=req_data["user_id"]
        )
        
        return JsonResponse({"success": "true", "resp": "Book is issued successfully"})
    
    except Exception as e:
        return JsonResponse({"success":"false", "error":f"{e}"})
    
@csrf_exempt 
def return_book(request):
    try:
        if request.method != "POST":
            raise custom_exceptions.CustomError(f"Method - {request.method} is not Allowed")
        
        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["isbn", "user_id"]:
            if key not in req_data.keys():
                raise custom_exceptions.CustomError(f"The parameter {key} in JSON Body is missing")

        conn.return_book(
            isbn=req_data["isbn"],
            user_id=req_data["user_id"]
        )
        
        return JsonResponse({"success": "true", "resp": "Book is returned successfully"})
    
    except Exception as e:
        return JsonResponse({"success":"false", "error":f"{e}"})
    




    