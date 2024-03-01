import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Laureate


def home(request):
    return render(request, 'nobels/home.html')


def laureates_list(request):
    laureates = Laureate.objects.all().order_by('-year')
    return render(request, 'nobels/laureates_list.html', {'laureates': laureates})


def laureate_detail(request, id):
    laureate = get_object_or_404(Laureate, pk=id)
    return render(request, 'nobels/laureate_detail.html', {'laureate': laureate})


@csrf_exempt
def create_laureate(request):
    if request.method == "POST":
        data = json.loads(request.body)
        laureate = Laureate.objects.create(
            name=data.get('name'),
            year=data.get('year'),
            contribution=data.get('contribution'),
        )
        return JsonResponse({"id": laureate.id, "name": laureate.name}, status=201)
    else:
        return HttpResponse(status=405)


@csrf_exempt
def delete_laureate(request, id):
    if request.method == "DELETE":
        laureate = get_object_or_404(Laureate, pk=id)
        laureate.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=405)