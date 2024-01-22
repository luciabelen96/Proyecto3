from django.shortcuts import render, redirect
from . import models
from . import forms
# Create your views here.

def index(request):
    return render(request, "core/index.html")

def profesor_list(request):
    consulta = models.Profesor.objects.all()
    contexto = {"profesores": consulta}
    return render(request, "core/Profesor_list.html" , contexto)
    

def profesor_creat(request):
    if request.method == "POST":
        form = forms.ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profesor-list")  # Ajusta el nombre según tu configuración de URL
    else:
        form = forms.ProfesorForm()

    return render(request, "core/Profesor_creat.html", {"form": form})

    