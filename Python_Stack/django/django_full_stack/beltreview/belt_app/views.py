from django.shortcuts import render,redirect
from belt_app.models import *
import bcrypt

# Create your views here.

def home(request):
    return render(request,'login.html')

def reg_process(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    elif len(User.objects.filter(email=request.POST["email"])) > 0:
        errors["duplicated_email_error"] = "Email is already existed"
        messages.error(request, errors["duplicated_email_error"], extra_tags = "duplicated_email_error")
        return redirect("/")
    else:
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        createUser = User.objects.create(name=request.POST['name'],
                                    alias=request.POST['alias'],
                                    email=request.POST['email'],
                                    pw_hash=pw_hash)
    request.session['user_id'] = createUser.id
    return redirect('/books')

def login_process(request):
    errors = User.objects.loginValidator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value)
            return redirect('/')
    else:
        user = User.objects.get(email=request.POST['login_email'])
        request.session['user_id'] = user.id
        return redirect('/books')

def books(request):
    context = {
        "reg_user": User.objects.get(id=request.session['user_id'])
    }
    return render(request,'books.html',context)

def addbook(request):
    context ={
        "authors": Author.objects.all()

    }
    return render(request,'addbook.html',context)

def newbook(request):
    if "user_id" not in request.session:
        return redirect('/')
    else:
        if request.POST.get("listed_author") != "none":
            select_author_from = request.POST.get('listed_author')
        else:
            select_author_from = request.POST["addauthor"]
            create_author = Author.objects.create(name=select_author_from)
            author_id = create_author.id

        authorname=  Author.objects.get(name=select_author_from)
        author_id = authorname.id
        title=request.POST["title"]
        review = request.POST['review']
        rating= request.POST.get('rating')
        #create author
        
        
        book_author = Author.objects.get(id=author_id)
        this_user = User.objects.get(id=request.session['user_id'])
        #Create books
        this_book = Books.objects.create(
        title = title,
        author = book_author,
        book_owner = this_user
        )
        #Create reviews
        Review.objects.create(review=review, rating=rating, book=this_book,reviewer=this_user)
        return redirect(f"/books/{this_book.id}")

def showbook(request,id):
    if "user_id" not in request.session:
        return redirect('/')
    else:
        this_book = Books.objects.get(id=id)
        logged_in = User.objects.get(id=request.session["user_id"])
        context = {
            "logged_in": User.objects.get(id=request.session["user_id"]),
            "book": Books.objects.get(id=id),
            "reviews":Review.objects.filter(book=this_book).order_by("-created_at")
        }
        return render(request,'showbook.html',context)

def userinfo(request,id):
    context = {
        "user": User.objects.get(id=id),
        "reviews":Review.objects.filter(reviewer=id).order_by("-created_at"),
        "total_reviews": Review.objects.filter(reviewer=id).count()
    }
    return render(request,'userinfo.html',context)

def deletereview(request,id):
    if "user_id" not in request.session:
        return redirect('/')
    else:
        return redirect('/showbook.html')


def logout(request,id):
    request.session['user_id'] = ""
    return redirect('/')
