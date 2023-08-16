from django.shortcuts import render, redirect, get_object_or_404
from .form import UserForm, BookForm
from .models import User, Book

def home(request):
    return render(request, 'home.html')


def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
        return render(request, 'register_user.html' , {'form':form})

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users':users})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books':books})

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
        return render(request, 'add_book.html' , {'form':form, 'action': 'Create'})

def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
        return render(request, 'add_book.html' , {'form':form, 'action': 'Update'})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html' , {'book':book})
