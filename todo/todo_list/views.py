from django.shortcuts import render,redirect
from .models import List
from .forms import Listform
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = Listform(request.POST)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('item has been added to a list'))
            return render(request, 'home.html', {'all_items':all_items})

    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items':all_items})


def delete(request, item_id):
    item=List.objects.get(pk=item_id)
    item.delete()
    messages.success(request,{'item has been deleted'})
    return redirect('home')


def cross_off(request, item_id):
    item=List.objects.get(pk=item_id)
    item.completed = True
    item.save()
    return redirect('home')


def uncross(request, item_id):
    item=List.objects.get(pk=item_id)
    item.completed = False
    item.save()
    return redirect('home')
