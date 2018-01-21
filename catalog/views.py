from django.shortcuts import render
from django.views import generic

# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_avialable = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_genre = Genre.objects.all().count()
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances, 'num_instances_available': num_instances_avialable, 'num_authors': num_authors, 'num_genre': num_genre,},
    )
class BookListView(generic.ListView):
    model = Book
class BookDetailView(generic.DetailView):
    model = Book
