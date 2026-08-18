from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"📩 Сообщение от {name} ({email}): {message}")
        return render(request, 'contacts.html', {'success': True})
    return render(request, 'contacts.html')
