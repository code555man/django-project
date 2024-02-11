from django.shortcuts import render
from .form import ImageForm
from .models import Image

def index(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    images = Image.objects.all()
    return render(request, 'myapp/components/index.html', {'form': form, 'images': images})