from django.shortcuts import render, redirect

from app.forms import CakeForm
from app.models import Cake, Baker


# Create your views here.

def index(request):
    cakes = Cake.objects.all()
    context = {'cakes': cakes}
    return render(request, 'index.html', context=context)


def add(request):
    if request.method == 'POST':
        form = CakeForm(request.POST, request.FILES)
        if form.is_valid():
            cake = form.save(commit=False)
            cake.image = form.cleaned_data['image']
            cake.baker = Baker.objects.filter(user=request.user).first()
            cake.save()
            return redirect('index')

    return render(request, 'add.html', {'form': CakeForm()})
