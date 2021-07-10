from django.shortcuts import render,redirect
from .models import Books, Authors

# Create your views here.
def root(request):# displaying the books and adding a book
    context = {
        'all_books': Books.objects.all(),
    }

    return render(request,'index.html',context)

def addBook(request):# adding a new a book and redirecting to the root
    request.session['title'] = request.POST['title']
    request.session['description'] = request.POST['description']
    newly_created_book = Books.objects.create(title = request.session['title'], desc = request.session['description'])
    
    return redirect('/')

def viewBooks(request, b_id):# Viewing the selected book
    
    book = Books.objects.get(id = b_id)
    author = Authors.objects.get(id = book.id)
    print(book.title)
    request.session['title'] = book.title
    request.session['desc'] = book.desc
    request.session['id'] = b_id
    
    book_authors = book.authors.all()# getting all the authors of the selected book
    print(book_authors, '/'*30)
    
    
    arr = []# initiating an array to save the selected authors id inside
    for author in book_authors:
        arr.append(author.id)
        print(author.id)
    
    print(arr)
    final_authors = Authors.objects.exclude(id__in=arr)# excluding the authors with the selected id's
    
    print(final_authors, '<=' * 10)

    context = {
        'all_books': Books.objects.all(),
        'book_authors': book.authors.all(),
        'all_authors': Authors.objects.all(),
        'final': final_authors,# saving the selected authors in final key to access in the document
    }

    return render(request, 'view_book.html', context)

def addAuthorBook(request, b_id): # adding an author to the selected book
    
    author = Books.objects.get(id = b_id)# getting book with the selected id
    author_id = request.POST['author']
    print(author_id)
    author_to_add = Authors.objects.get(id = author_id)# getting the author with the selected id
    author_to_add.books.add(author)#adding the author to the selected book authors

    return redirect('/view_books/' + format(b_id))


def author(request):# displaying authors and adding an author 
    context = {
        'all_authors': Authors.objects.all(),
        'all_books': Books.objects.all()
    }


    return render(request, 'authors.html',context)

def addAuthor(request):# adding an author 
    
    request.session['f_name'] = request.POST['first_name']
    request.session['l_name'] = request.POST['last_name']
    request.session['notes'] = request.POST['notes']
    newly_created_author = Authors.objects.create(first_name = request.session['f_name'], last_name = request.session['l_name'],notes = request.session['notes'])
    print(newly_created_author, '/*' * 30)

    return redirect('/authors')


def viewAuthors(request, a_id):# viewing the current author details
    
    author = Authors.objects.get(id = a_id)
    print(author.first_name)
    request.session['first_name'] = author.first_name
    request.session['last_name'] = author.last_name
    request.session['notes'] = author.notes
    request.session['id'] = a_id
    
    
    
    author_books = author.books.all()# getting all the authors of the selected book
    print(author_books, '/'*30)
    # for book in author_books:
    #     print(book.id)
    
    arr = []# initiating an array to save the selected authors id inside
    for book in author_books:#for every book in author_books
        
        arr.append(book.id)# add the book id which is still there
        print(book.id)
    print(rest_of_books, '-*-'*30)
    print(arr)
    final_books = Books.objects.exclude(id__in=arr)# excluding the books with the selected id's
    
    print(final_books, '<=' * 10)
    
    
    context = {
        'all_books': Books.objects.all(),
        'author_books': author.books.all(),
        'final': final_books,# saving the selected authors in final key to access in the document
    }

    return render(request, 'view_author.html',context)


def addBookAuthor(request, a_id):# adding a book to the author
    
    author = Authors.objects.get(id = a_id)
    book_id = request.POST['book']
    print(book_id)
    book_to_add = Books.objects.get(id = book_id)
    book_to_add.authors.add(author)

    return redirect('/view_authors/' + format(a_id))