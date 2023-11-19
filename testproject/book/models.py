from django.db import models
from django.utils.html import format_html

BOOK_LEVEL_CHOICE = (
    ('B','Basic'),
    ('M','Medium'),
    ('A','Advance'),
)

class Category(models.Model):
    
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Category'
    
class Author(models.Model):
    
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Author'

class Book(models.Model):
        
    code = models.CharField(max_length=10, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=False)  # many to one
    author = models.ManyToManyField(Author, blank=True)  # many to many
    level = models.CharField(max_length=5, null=True, blank=True, choices=BOOK_LEVEL_CHOICE)
    image = models.FileField(upload_to='upload', null=True, blank=True)
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def get_comment_count(self):
        return self.bookcomment_set.count()
    
    def show_img(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" height="40px">')
        return ''
    show_img.allow_tags = True
    # show_img.short_description = 'Image'
        
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Book'
    
class BookComment(models.Model):
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    rating = models.FloatField()
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
    
    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Book Comment'
    