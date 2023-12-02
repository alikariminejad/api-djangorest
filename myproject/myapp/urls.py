from django.urls import path, include
from rest_framework import routers
from .views import book_list, book_detail, BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView, BookViewSet, UserLoginView

router = routers.DefaultRouter()
router.register(r'books', BookViewSet, basename="book")


urlpatterns = [
    # path('books/', book_list, name='book_list'),
    # path('books/<int:pk>', book_detail, name='book_detail'),
    # path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    # path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-retrieve-update-destroy'),
    path('', include(router.urls)),
    path('login/', UserLoginView.as_view(), name='login'),
]
