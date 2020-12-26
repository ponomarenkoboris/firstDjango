from django.shortcuts import render
from django.http import HttpResponse
from p_library.models import Book, Author, Publisher
from django.template import loader
from django.shortcuts import redirect

# Create your views here.
def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)

def index(request):
    template = loader.get_template('index.html')
    # books_count = Book.objects.all().count()
    books = Book.objects.all()
    publish = Publisher.objects.all()
    numbs = [1,2,3,4,5,6,7,8,9,10]
    biblio_data = {
        'title': 'мою библиотеку',
        'books': books,
        'numbs': numbs,
        'publish': publish,
    }
    return HttpResponse(template.render(biblio_data, request))

def home(request):
    template = loader.get_template('home.html')
    text = Book.objects.all().filter(copy_count__gt=1)
    publisher = Publisher.objects.all()
    text_datd = {
        'text': text,
        'publisher': publisher,
        }
    return HttpResponse(template.render(text_datd))

def publish_list(request):
    template = loader.get_template('publisher.html')
    some_text = 'Hi world!'
    publisher = Publisher.objects.all()
    data = {
        'some_text': some_text,
        'publisher': publisher,
        }
    return HttpResponse(template.render(data))


