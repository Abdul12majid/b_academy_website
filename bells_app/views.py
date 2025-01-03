from django.shortcuts import render, HttpResponse
from .models import Contact

# Create your views here.
def index(request):
	return render(request, 'index.html', {})


def admission_page(request):
	return render(request, 'admission_page.html', {})

def contact_page(request):
	if request.method == "POST":
		name = request.POST['name']
		email = request.POST['email']
		message = request.POST['message']
		new_contact = Contact.objects.create(name=name, email=email, message=message)
		new_contact.save()
		print("saved")
		return render(request, 'contact_page.html', {})
	return render(request, 'contact_page.html', {})