from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['id', 'slug', 'published', 'created', 'updated']

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['code'].error_messages ={
            'required': 'Pleace enter book code',
        }
        self.fields['name'].error_messages ={
            'required': 'Pleace enter book name',
        }
        self.fields['price'].error_messages ={
            'required': 'Pleace enter book price',
        }

    def clean(self):
        cd = super(BookForm, self).clean()
        if not cd.get('category'):
            self.add_error('category', 'Please select category name')

        if not cd.get('author'):
            self.add_error('author', 'Please select author name')