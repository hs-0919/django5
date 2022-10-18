from django.contrib import admin
from myapp.models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id' ,'code', 'name', 'price', 'pub_date')  # 튜플로 주기
    

admin.site.register(Article, ArticleAdmin)

