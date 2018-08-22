from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
# Create your views here.
def contact(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title" : "contact",
        "form" : contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == 'POST':
        # print(request.POST)
    return render(request, "contact/contact.html",context)