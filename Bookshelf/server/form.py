from django import forms
from .models import User, Book

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


