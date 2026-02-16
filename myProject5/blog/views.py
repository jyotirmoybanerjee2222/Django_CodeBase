from django.shortcuts import render
from datetime import datetime
# Create your views here.

def blog_details(request):
    post={
        "title":"My Second Templates Post",
        "description":"Django is a High-lebel Python Web Framework",
        "author":None,
        "comment_count":5,
        "tags":["Django","Python","Web Development"],
        "created_at": datetime.now(),

        "price":100,
        "number":7,


    }
    return render(request,"blog/blog_details.html",{"post":post})
