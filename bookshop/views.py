from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, BooksCategory, Books, BooksAuthor, Review
from .forms import Bookform


def main(request):
    author = Author.objects.all()
    books = Books.objects.all()
    context = {
        'author': author,
        'books': books,
    }
    return render(request, 'index.html', context=context)


def get_books(request, pk=None):
    if pk is not None:
        books = Books.objects.filter(pk=pk)
    else:
        books = Books.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books.html', context=context)


def detail(request, pk):
    book = Books.objects.get(pk=pk)
    reviews = Review.objects.filter(book=pk)
    context = {
        'book': book,
        'reviews': reviews
    }
    return render(request, 'detail.html', context=context)


def get_author(request, pk=None):
    if pk is not None:
        authors = Author.objects.filter(pk=pk)
    else:
        authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'author.html', context=context)


def add_books(request):
    form = Bookform(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('bookshop:main')
    context = {
        'form': form
    }
    return render(request, 'create.html', context=context)


def update_books(request, pk):
    book = get_object_or_404(Books, pk=pk)
    if request.method == 'POST':
        form = Bookform(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('bookshop:main')
    else:
        form = Bookform(instance=book)
    context = {'form': form}
    return render(request, 'update.html', context)


def delete_books(request, pk):
    book = get_object_or_404(Books, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('bookshop:main')
    return render(request, 'delete.html', {'book': book})

