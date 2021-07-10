#from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.root),
    path('addBook', views.addBook),
    path('view_books/<int:b_id>', views.viewBooks),
    path('view_books/add_author_book/<int:b_id>', views.addAuthorBook),
    path('authors', views.author),
    path('addAuthors', views.addAuthor),
    path('view_authors/<int:a_id>', views.viewAuthors),
    path('view_authors/add_book_author/<int:a_id>', views.addBookAuthor),

]
