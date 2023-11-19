from django.contrib import admin
from .models import Book, Category, Author, BookComment

class BookCommentStackedInline(admin.StackedInline):
    model = BookComment
    
class BookTabularInline(admin.TabularInline):
    model = BookComment
    extra = 2
    
class BookAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'price', 'level', 'category', 'published', 'show_img']
    list_filter = ['published']
    search_fields = ['code', 'name']
    prepopulated_fields = {'slug': ['name']}
    
    fieldsets = (
        (None,{'fields': ['code', 'slug', 'name', 'description', 'price', 'level', 'image']}),
        ('Category',{'fields': ['category', 'author'], 'classes': ['collapse']})
    )
    inlines = [ BookTabularInline ]
    
    

admin.site.register(Book,BookAdmin)
admin.site.register(Category)
admin.site.register(Author)