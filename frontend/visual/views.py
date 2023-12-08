from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def mecanico_list(request):
    return render(request,'visual/mecanico_list.html')