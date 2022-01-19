from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    books_list = Book.objects.all()
    context = {'books_list': books_list}
    return render(request, template, context)

def pub_books_view(request, pub_date):
    template = 'books/pub_books.html'
    dates = []
    for book in Book.objects.all():
        dates.append(f'{book.pub_date.year}-{book.pub_date.month}-{book.pub_date.day}')
    paginator = Paginator(dates, 1)
    page = paginator.page('pub_date')
    print(page)

    pub_books = Book.objects.filter(pub_date=pub_date)
    context = {
        'pub_books': pub_books,
        'page': page,
               }
    return render(request, template, context)
