from django.shortcuts import render
from datetime import datetime
# Create your views here.

class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

def home(request):
        context={
            "name":"Mohit Kumar",
            "age":25,
            "skill":["python","django","React"],
            "user":User("Kumar",25),

            "blog":{
                "title":"Django Template Introduction",
                "content":"<b>This Bold</b>",
                "created_at":datetime.now(),
                "author":{
                 "name":"Mohit Kumar",
                },
            },
            "empty_value":None,            
        }

        return render(request,"blog/home.html",context)