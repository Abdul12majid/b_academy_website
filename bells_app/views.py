from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
	return render(request, 'index.html', {})


def admission_page(request):
	return render(request, 'admission_page.html', {})

def contact_page(request):
	return render(request, 'contact_page.html', {})