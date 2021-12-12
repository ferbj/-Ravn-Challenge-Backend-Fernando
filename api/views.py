from django.http.response import JsonResponse
from rest_framework import  viewsets
# Create your views here.
from django.shortcuts import render
from django.db import connection
from django.core.cache import cache
class AuthorView(viewsets.ModelViewSet):

    
    def count(request,id=None):
        #authors = cache.get('authors')
        if(request.method=='GET' and id!=None):
            sql= 'SELECT au.id,au.name as author,SUM(sale_items.item_price) as sales_total FROM authors as au ' ' inner join books on books.author_id=au.id ' ' inner join sale_items on books.id=sale_items.book_id ' ' GROUP BY au.id,au.name ' ' ORDER BY sales_total DESC ' ' limit '+str(id)
            with connection.cursor() as cursor:
                try:
                    cursor.execute(sql)
                    columns = [col[0] for col in cursor.description]        
                    authors = [dict(zip(columns, row)) for row in cursor.fetchall()]
                    #cache.set('authors',authors,5)
                    return JsonResponse(authors,safe=False)
                except Exception as e:
                    print(e)
                    cursor.close()
        else:
            sql= 'SELECT au.id,au.name as author,SUM(sale_items.item_price) as sales_total FROM authors as au ' ' inner join books on books.author_id=au.id ' ' inner join sale_items on books.id=sale_items.book_id ' ' GROUP BY au.id,au.name ' ' ORDER BY sales_total DESC ' ' limit 10'
            with connection.cursor() as cursor:
                cursor.execute(sql)
                columns = [col[0] for col in cursor.description]        
                authors = [dict(zip(columns, row)) for row in cursor.fetchall()]
                return JsonResponse(authors,safe=False)

def handler_404(request, exception):
    return render(request, 'errors/404.html',status=404)

def handler_500(request, exception):
    return render(request, 'errors/505.html',status=505)

