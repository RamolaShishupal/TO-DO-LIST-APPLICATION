from django.shortcuts import render ,redirect
from .models import note
from .forms import *
from django.http import HttpResponse

from django.contrib import messages
# Create your views here.
def home(request):
    all_item= note.objects.all()
    form=Noteform()
    if request.method == 'POST':
        form=Noteform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    contex={'all_item':all_item,'form':form}
    return render(request,'home.html',contex)




def delete(request,note_id):
    item=note.objects.get(pk=note_id)
    item.delete()
    messages.success(request,("Note has been deleted"))
    return redirect('home')

def update(request,pk):
    return render(request,update.html)