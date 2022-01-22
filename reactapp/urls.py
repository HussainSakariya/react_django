from django.urls import path,include
from .views import *
from rest_framework import routers

router=routers.DefaultRouter()
router.register('books',BooksViewset)

urlpatterns = [
    path('',include(router.urls)),
    # path('',index.as_view(),name='index'),
    path('insert/',insert.as_view(),name='insert'),
    path('edit/<int:pk>/',edit.as_view(),name='edit'),
    path('delete/<int:pk>/',delete.as_view(),name='delete'),
    ]