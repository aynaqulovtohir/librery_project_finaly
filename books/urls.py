from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import BookListAPIView,BookCreateAPIView,BookDetailAPIView,BookDeleteAPIView,BookUpdateAPIView,BookViewSet


router = SimpleRouter()
router.register(r'books', BookViewSet,basename='books')

urlpatterns = [
    # path('books/<int:pk>', BookDetailAPIView.as_view()),
    # path('books/create/', BookListCreateAPIView.as_view()),
    # path('books/<int:pk>/delete/', BookDeleteAPIView.as_view()),
    # path('books/<int:pk>/update/', BooksUpdateAPIView.as_view()),
    # path('books/updatedelete/<int:pk>/', BooksUpdateDeleteAPIView.as_view()),

    #
    # path('books/', BookListAPIView.as_view()),
    # path('books/create/',BookCreateAPIView.as_view()),
    # path('books/<int:pk>/', BookDetailAPIView.as_view()),
    # path('books/<int:pk>/delete/',BookDeleteAPIView.as_view()),
    # path('books/<int:pk>/update/',BookUpdateAPIView.as_view()),
]

urlpatterns += router.urls
