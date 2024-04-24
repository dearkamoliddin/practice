from django.shortcuts import render

from books.models import BookModel


# Create your views here.


def home_view(request):
    book = BookModel.objects.all()
    context = {
        'books_list': book
    }
    return render(request, 'home.html', context)
