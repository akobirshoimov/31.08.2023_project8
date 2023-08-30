from django.shortcuts import render,get_object_or_404
from .models import Oziq_ovqat,Dokonlar
from django.http import JsonResponse

# Create your views here.
def all(request):
    all = Oziq_ovqat.objects.all()
    result = []
    for i in all:
        result.append({
            'name':i.name,
            'turi':i.type,
            'surogi': i.surogi
        })
    return JsonResponse(result,safe=False)

def detail(request,detail_id):
    each = Dokonlar.objects.get(id=detail_id)
    each = get_object_or_404(Dokonlar,id = detail_id)
    info = f'nomi:{Dokonlar.name},manzili:{Dokonlar.location}' 
    return JsonResponse(info)

