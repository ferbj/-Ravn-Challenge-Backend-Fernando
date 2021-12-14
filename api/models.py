from django.db import models
from django.utils.functional import cached_property
# Create your models here. 

class Author(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.TextField()
    date_of_birth=models.DateTimeField()
    
    class Meta:
        db_table = "authors"
    @cached_property 
    def AuthorName(self):
        str = "Name: {0}"
        return str.format(self.name,self.date_of_birth)
    @cached_property 
    def __str__(self):
        return self.AuthorName()

class Book(models.Model):
    id=models.AutoField(primary_key=True)
    author = models.ForeignKey(Author,null=False,blank=False,on_delete=models.CASCADE)
    isbn=models.TextField()
    
    class Meta:
        db_table = "books"
    @cached_property 
    def Bookname(self):
        str_author = "Author: {0}, Isbn: {1}"
        return str_author.format(self.author,self.isbn)
    @cached_property 
    def __str__(self):
        return self.Bookname()

class SaleItem(models.Model):
    id=models.AutoField(primary_key=True)
    book = models.ForeignKey(Book,null=False,blank=False,on_delete=models.CASCADE)
    customer_name = models.TextField()
    item_price = models.FloatField()
    quantity=models.PositiveIntegerField()

    class Meta:
        db_table = "sale_items"
    @cached_property 
    def Sales(self):
        str = "Custommer: {0}, Price:{1}, Quantity:{2}"
        return str.format(self.customer_name,self.item_price,self.quantity)
    @cached_property 
    def __str__(self):
        return self.Sales()