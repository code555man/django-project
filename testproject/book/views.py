from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Category, Book
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .forms import BookForm
from django.template.defaultfilters import slugify
# from django.contrib.auth.decorators import login_required

# @login_required
def index(request):
    categories = Category.objects.all()
    books = Book.objects.filter(published=True)
    
    categ_id = request.GET.get('categoryid')
    if categ_id:
        books = books.filter(category_id=categ_id)
        
    paginator = Paginator(books,5)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    
    return render(request, 'book/index.html',{
        'books': books,
        'categories': categories,
        'categ_id': categ_id,
    })
    
def detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book/detail.html',{
        'book': book,
    })
    
def book_add(request):
    form = BookForm()
    if request.method =='POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.slug = slugify(book.name)
            book.published=True
            book.save()
            form.save_m2m()
            messages.success(request, 'Save success')
            return HttpResponseRedirect(reverse('book:index', kwargs={}))
        messages.error(request, 'Save Failed!')
    return render(request, 'book/add.html',{
        'form': form,
    })

def cars_add(request, slug):
    book = get_object_or_404(Book, slug=slug)
    card_item = request.session.get('card_items') or []
    
    duplicated = False
    for c in card_item:
        if c.get('slug') == book.slug:
            c['qty'] == int(c.get('qty') or '1') + 1
            duplicated = True
            
    if not duplicated:
        card_item.append({
            'id': book.id,
            'slug': book.slug,
            'name': book.name,
            'price': book.price,
            'qty': 1,
        })
    request.session['card_items'] = card_item
    return HttpResponseRedirect(reverse('book:card_list',kwargs={}))

def card_list(request):
    card_item = request.session.get('card_items') or []
    
    total_qty = 0
    for c in card_item:
        total_qty = total_qty + c.get('qty')
        
    request.session['card_qty'] = total_qty
    return render(request, 'book/card.html', {
        'card_items': card_item,
    })
    

def card_delete(request, slug):
    card_item = request.session.get('card_items') or []
    for i in range(len(card_item)):
        if card_item[i]['slug'] == slug:
            del card_item[i]
            break
        
    request.session['card_items'] = card_item
    return HttpResponseRedirect(reverse('book:card_list', kwargs={}))
