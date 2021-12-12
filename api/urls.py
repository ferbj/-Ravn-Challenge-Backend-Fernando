from rest_framework import routers
from .viewsets import AuthorViewSet,BookViewSet,SaleItemsViewSet

from django.urls import include, path
router = routers.SimpleRouter()
router.register('authors',AuthorViewSet)
router.register('books',BookViewSet)
router.register('saleitems',SaleItemsViewSet)

urlpatterns = router.urls