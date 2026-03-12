
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, status


# class BookListAPIView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
# class BookDetailAPIView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
# class BookDeleteAPIView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
# class BooksUpdateAPIView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
# class BookListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
# class BooksUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookListAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data={
            'status':f"Returned {len(books)} books",
            'serializer':serializer_data
        }
        return Response(data)

class BookCreateAPIView(APIView):
    def post(self, request):
        data=request.data
        serializer=BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data={
                'status':"Created books are saved to database",
                'books':data
            }
            return Response(data)
        else:
            return Response(
                {
                    'status':"Failed to create book",
                    'message':serializer.errors,
                }
            )

class BookDetailAPIView(APIView):
    def get(self, request, pk):
         try:
            book = Book.objects.get(id=pk)
            seriializer_data=BookSerializer(book).data
            data={
                'status':f"Succesfully fetched book {pk}",
                'book':seriializer_data
                }
            return Response(data,status=status.HTTP_200_OK)
         except Exception :
               return Response(
                {
                        'status':'Book is not exists',
                        'message':"Book not found",
                        },
                status=status.HTTP_404_NOT_FOUND
                )

class BookDeleteAPIView(APIView):
    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response({
                'status':True,
                'message':"Succesfully deleted book",
            },status=status.HTTP_204_NO_CONTENT)
        except :
            return Response(
                {
                    'status':False,
                    'message':"Book not found and  not deleted",
                },
                status=status.HTTP_404_NOT_FOUND
            )

class BookUpdateAPIView(APIView):
    def put(self, request, pk):
        try:
            book = get_object_or_404(Book.objects.all(), pk=pk)
            data=request.data
            serializer=BookSerializer(instance=book,data=data,partial=True)
            if serializer.is_valid():
                book_saved=serializer.save()
                return Response({
                    'status':True,
                    'message':f"Succesfully updated {book_saved} book",
                },
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        'status':False,
                        'message':serializer.errors,
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        except :
            return Response(
                {
                    'status':False,
                    'message':"Book not found and  not updated",
                },
                status=status.HTTP_404_NOT_FOUND
            )

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
