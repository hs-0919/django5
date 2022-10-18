from django.shortcuts import render
from myapp.models import Article

# Create your views here.

def main(request):
    return render(request, "main.html")

def show(request):
    # sql = "select * from Article"
    datas= Article.objects.all()   # Django ORM
    print(datas)  # <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>]>
    print(datas[0].name)  # 아메리카노
    
    return render(request, "list.html", {'articles':datas})
