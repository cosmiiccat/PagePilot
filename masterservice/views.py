from django.shortcuts import render
from django.http import JsonResponse
from utils import custom_exceptions

# Create your views here.


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


