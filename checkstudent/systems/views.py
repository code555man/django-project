from django.shortcuts import render



def check(request):
    return render(request, 'systems/index.html', {'nbar': 'index'})

def setting(request):
    return render(request, 'systems/setting.html', {'nbar': 'setting'})

def login(request):
    return render(request, 'systems/components/login/login.html', {'nbar': 'login'})

def view_data_student(request):
    return render(request, 'systems/components/student/index.html', {'nbar': 'student'})

def save_data_student(request):
    return render(request, 'systems/components/student/save.html')
