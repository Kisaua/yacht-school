from django.shortcuts import render
from .forms import ContactForm
from .models import Portfolio


def index(request):
    context = {}
    template = 'yacht01/index.html'
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # print (request.POST['name'])
            context["message"] = True
            form.save()
    else:
        form = ContactForm()

    portfolio = Portfolio.objects.filter(show=True)
    context['portfolio'] = portfolio
    context['form'] = form

    return render(request, template, context)
