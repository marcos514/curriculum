from django.shortcuts import render
from .models import Estudio
from .models import Experiencia
from .models import Lenguajes

def curriculum(request):
    estudios = Estudio.objects.all()
    trabajos = Experiencia.objects.all()
    lenguajes= Lenguajes.objects.all()
    return render(request, 'blog/curriculum.html', {"estudios":estudios,"trabajos":trabajos,"lenguajes":lenguajes})
