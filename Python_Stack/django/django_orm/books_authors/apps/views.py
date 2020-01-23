from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def home(request):
    context = {
        "all_books": Books.objects.all()
    }
    return render(request,'books.html',context)

def create(request):
    addBooks = Books.objects.create(title = request.POST['title'],description = request.POST['description'])
    return redirect('/')

def view(request,id):
    books = Books.objects.get(id=id)
    context = {
        "book": Books.objects.get(id=id),
        "all_authors": Authors.objects.all(),
        "book_authors": books.author.all()
    }
    return render(request,'view.html',context)

def authors(request):
    context = {

        "all_authors": Authors.objects.all()
    }
    return render(request,'authors.html',context)

def addAuthor(request,id):

    bookId=id
    authorId = request.POST['author']

    this_book = Books.objects.get(id=bookId)
    this_author = Authors.objects.get(id=authorId)

    this_book.author.add(this_author)

    return redirect(f"/book/{id}")

def createAuthor(request):
    addAuthor = Authors.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'],note =request.POST['note'] )
    return redirect('/authors')

def viewAuthor(request,id):
    author = Authors.objects.get(id=id)

    context = {
        "authorInfo": Authors.objects.get(id=id),
        "all_books": Books.objects.all(),
        "author_books": author.books.all()
    }
    return render(request,'viewAuthor.html',context)

def addBook(request,id):
    authorId = id
    addBookId = request.POST['book']

    this_author = Authors.objects.get(id=authorId)
    this_book = Books.objects.get(id=addBookId)

    this_author.books.add(this_book)
    return redirect(f"/author/{id}")